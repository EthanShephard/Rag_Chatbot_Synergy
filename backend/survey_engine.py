import re
import json
from pathlib import Path
from datetime import datetime, timezone

from ollama import Client

from backend.survey import SURVEYS, CATEGORY_URLS, CURRENCY


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Small/fast model — narrating a step or drafting a short email doesn't
# need the 8b RAG model's latency.
DRAFT_MODEL = "qwen2.5:3b"

SALES_EMAIL = "sales@synergytpl.com"

LEADS_FILE = Path(__file__).resolve().parent / "database" / "leads.jsonl"
LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)

_draft_client = Client(host="http://127.0.0.1:11434")


class SurveyEngine:

    def __init__(self):
        self.survey = SURVEYS["product_finder"]

    def start(self, session):
        """
        Starts a survey.
        """

        start_node = self.survey["start"]

        session["survey"] = {
            "active": True,
            "current": start_node,
            "answers": {}
        }

        return self._build_response(start_node)

    def handle(self, session, answer):
        """
        Handles one survey answer and returns the next question.
        """

        survey_state = session["survey"]

        current_node = survey_state["current"]

        node = self.survey["nodes"][current_node]

        # ----------------------------
        # Text Input (email / quantity)
        # ----------------------------

        if node.get("type") == "text":

            cleaned = answer.strip()

            if node.get("validate") == "email":

                if not EMAIL_RE.match(cleaned):
                    return {
                        "type": "survey",
                        "finished": False,
                        "question": "That doesn't look like a valid email — mind double-checking and resending it?",
                        "input": "text"
                    }

            elif node.get("validate") == "quantity":

                min_q = node.get("min", 1)
                max_q = node.get("max", 9999)

                if not cleaned.isdigit() or not (min_q <= int(cleaned) <= max_q):
                    return {
                        "type": "survey",
                        "finished": False,
                        "question": f"Please enter a whole number between {min_q} and {max_q}.",
                        "input": "quantity",
                        "min": min_q,
                        "max": max_q,
                        "default": node.get("default", min_q)
                    }

                cleaned = int(cleaned)

            survey_state["answers"][node["key"]] = cleaned

            next_node = node["next"]
            selection_label = str(cleaned)

        # ----------------------------
        # Button Input
        # ----------------------------

        else:

            selected = None

            for option in node["options"]:

                if option["value"] == answer:

                    selected = option
                    break

            if selected is None:

                # Re-send the same question instead of dead-ending the
                # chat — a bare {"error": ...} with no "question" key
                # doesn't get tagged as a survey response on the
                # frontend, so the user would see nothing happen at all.
                return {
                    "type": "survey",
                    "finished": False,
                    "question": node["question"],
                    "quickReplies": [
                        {"text": option["text"], "value": option["value"]}
                        for option in node["options"]
                    ]
                }

            survey_state["answers"][node["key"]] = selected["value"]

            next_node = selected["next"]
            selection_label = selected["text"]

        # ----------------------------
        # Survey Finished
        # ----------------------------

        if next_node == "complete":

            survey_state["active"] = False

            return self._build_completion(survey_state["answers"])

        survey_state["current"] = next_node

        return self._build_response(next_node, previous_selection=selection_label)

    def is_active(self, session):

        return (
            "survey" in session
            and session["survey"]["active"]
        )

    def _build_response(self, node_name, previous_selection=None):

        node = self.survey["nodes"][node_name]

        if node.get("type") == "text":

            narrated = self._narrate_text_prompt(node, previous_selection)

            response = {
                "type": "survey",
                "finished": False,
                "question": narrated,
                "input": "quantity" if node.get("validate") == "quantity" else "text"
            }

            if node.get("validate") == "quantity":
                response["min"] = node.get("min", 1)
                response["max"] = node.get("max", 9999)
                response["default"] = node.get("default", 1)

        else:

            narrated = self._narrate_options(node, previous_selection)

            response = {
                "type": "survey",
                "finished": False,
                "question": narrated,
                "quickReplies": [
                    {"text": option["text"], "value": option["value"]}
                    for option in node["options"]
                ]
            }

        return response

    # ----------------------------------------------------
    # LLM narration — every step gets a short generated
    # reply, grounded strictly in the node's own data so it
    # can't invent products, prices, or specs.
    # ----------------------------------------------------

    def _narrate_options(self, node, previous_selection):

        options_list = ", ".join(o["text"] for o in node["options"])
        fallback = self._fallback_options_text(node, previous_selection, options_list)

        context = (
            f'The customer just selected "{previous_selection}". '
            if previous_selection else ""
        )

        prompt = f"""{context}Present this exact list of {len(node['options'])} options and nothing else, then ask: "{node['question']}"

Options (use these exact names only — do not add, remove, merge, or invent any): {options_list}

Rules:
- One short, friendly reply: a lead-in line, then the options as a plain list.
- Do not invent specs, prices, or stock information.
- Do not add options beyond the list above.
- Under 70 words."""

        return self._generate(prompt, fallback)

    def _narrate_text_prompt(self, node, previous_selection):

        fallback = (
            f"Got it. {node['question']}" if previous_selection
            else node["question"]
        )

        context = (
            f'The customer just told you: "{previous_selection}". '
            if previous_selection else ""
        )

        prompt = f"""{context}Now ask them, in one short friendly sentence: "{node['question']}"
Do not invent information. Do not answer on their behalf. Do not mention price or stock."""

        return self._generate(prompt, fallback)

    def _narrate_completion(self, answers):

        subcategory = answers.get("subcategory", "")
        quantity = answers.get("quantity", "")

        fallback = (
            f"Thanks — that's {quantity} unit(s) of {subcategory} noted. "
            "Would you like to visit our website or send us an email request for it?"
        )

        prompt = f"""The customer just finished a product inquiry for {quantity} unit(s) of "{subcategory}".
Write one short, warm sentence thanking them for the inquiry, then ask whether they'd like to
visit our website or send an email request regarding the product they chose.
Do not mention price, stock, or specs. Under 40 words."""

        return self._generate(prompt, fallback)

    def _generate(self, prompt, fallback):

        try:

            response = _draft_client.chat(
                model=DRAFT_MODEL,
                stream=False,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Jack, a friendly Synergy Telecom sales assistant "
                            "guiding a customer through a product picker. Only use the "
                            "exact information given to you in the user message — never "
                            "invent products, prices, or specs."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            text = response["message"]["content"].strip()

            return text if text else fallback

        except Exception:

            # Ollama unreachable/slow — never let narration block the survey
            return fallback

    def _fallback_options_text(self, node, previous_selection, options_list):

        lead = (
            f"You selected {previous_selection}, we have:"
            if previous_selection else node["question"]
        )

        return f"{lead}\n\n{options_list}"

    # ----------------------------------------------------
    # Completion
    # ----------------------------------------------------

    def _build_completion(self, answers):
        """
        Survey is done. Ask the customer how they'd like to proceed —
        the drafted email itself is only generated into the mailto
        action's body, not dumped into the chat as its own message.
        """

        self._log_lead(answers)

        closing_message = self._narrate_completion(answers)
        draft = self._draft_email(answers)

        category = answers.get("product", "")
        website = CATEGORY_URLS.get(
            category,
            CATEGORY_URLS.get("_default")
        )

        subject_item = answers.get("subcategory") or category

        return {
            "type": "survey_complete",
            "finished": True,
            "message": closing_message,
            "answers": answers,
            "actions": [
                {
                    "id": "email",
                    "label": "📧 Email us this request",
                    "mailto": SALES_EMAIL,
                    "subject": f"Inquiry: {subject_item}",
                    "body": draft
                },
                {
                    "id": "website",
                    "label": "🌐 View this product online",
                    "url": website
                }
            ]
        }

    def _draft_email(self, answers):

        category = answers.get("product", "")
        subcategory = answers.get("subcategory", "")
        quantity = answers.get("quantity", 1)
        email = answers.get("email", "")

        pricing_line = self._pricing_line(subcategory, quantity)

        prompt = f"""Write a short, professional purchase-inquiry email on behalf of a customer, addressed to the Synergy Telecom sales team.

Customer email: {email}
Product category: {category}
Specific item: {subcategory}
Quantity requested: {quantity}
Pricing note to include verbatim: {pricing_line}

Rules:
- Under 110 words.
- Do not invent specs, pricing, or stock availability beyond the pricing note given above.
- Mention the quantity requested.
- Sign off with the customer's email address.
- Return ONLY the email body. No subject line, no preamble, no markdown."""

        fallback = self._fallback_email(category, subcategory, quantity, email, pricing_line)

        return self._generate(prompt, fallback)

    def _fallback_email(self, category, subcategory, quantity, email, pricing_line):

        item = subcategory or category

        return (
            f"Hello,\n\n"
            f"I'm interested in {quantity} unit(s) of {item}. "
            f"Could you please share a quote and confirm availability?\n\n"
            f"{pricing_line}\n\n"
            f"Thanks,\n{email}"
        )

    def _pricing_line(self, subcategory_value, quantity):

        option = self._find_leaf_option(subcategory_value)
        unit_price = option.get("price") if option else None

        if unit_price is None:
            return "Pricing: to be confirmed by our sales team."

        try:
            total = unit_price * int(quantity)
        except (TypeError, ValueError):
            total = unit_price

        return (
            f"Unit price: {CURRENCY}{unit_price:,.2f} — "
            f"estimated total for {quantity} unit(s): {CURRENCY}{total:,.2f} "
            f"(subject to confirmation)."
        )

    def _find_leaf_option(self, value):

        for node in self.survey["nodes"].values():

            for option in node.get("options", []):

                if option["value"] == value:
                    return option

        return None

    def _log_lead(self, answers):

        try:
            with open(LEADS_FILE, "a", encoding="utf-8") as f:
                f.write(
                    json.dumps({
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        **answers
                    }) + "\n"
                )

        except Exception:
            # Lead logging is a nice-to-have, never fatal
            pass


survey_engine = SurveyEngine()