import re
import json
import os
from pathlib import Path
from datetime import datetime, timezone

# CHANGED: DeepSeek uses an OpenAI-compatible endpoint, not Ollama's client.
from openai import OpenAI
from filelock import FileLock

from backend.survey import SURVEYS, CATEGORY_URLS, CONNECTOR_TYPE_URLS, CURRENCY
# CHANGED: OLLAMA_HOST no longer needed here — drop it from backend.config
# if nothing else in the project still uses it.


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# CHANGED: qwen2.5:3b -> deepseek-v4-flash. Same reasoning as before —
# narrating a step or drafting a short email doesn't need a big/slow model,
# and Flash is DeepSeek's small, cheap tier.
DRAFT_MODEL = "deepseek-v4-flash"

SALES_EMAIL = "info@rfconnector.in"

LEADS_FILE = Path(__file__).resolve().parent / "database" / "leads.jsonl"
LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)
LEADS_LOCK = FileLock(str(LEADS_FILE) + ".lock")

# CHANGED: Ollama's `Client(host=OLLAMA_HOST)` -> OpenAI-style client
# pointed at DeepSeek's base_url, reading the key from DEEPSEEK_API_KEY.
_draft_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


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

        item = answers.get("product_variant") or answers.get("subcategory", "")
        quantity = answers.get("quantity", "")

        fallback = (
            f"Thanks — that's {quantity} unit(s) of {item} noted. "
            "Would you like to visit our website or send us an email request for it?"
        )

        prompt = f"""The customer just finished a product inquiry for {quantity} unit(s) of "{item}".
Write one short, warm sentence thanking them for the inquiry, then ask whether they'd like to
visit our website or send an email request regarding the product they chose.
Do not mention price, stock, or specs. Under 40 words."""

        return self._generate(prompt, fallback)

    def _generate(self, prompt, fallback):

        try:

            # CHANGED: Ollama's `client.chat(...)` -> OpenAI-style
            # `client.chat.completions.create(...)`. Also disabled
            # DeepSeek's "thinking" mode — these are short, templated
            # narration/drafting tasks with no need for hidden
            # chain-of-thought, and thinking tokens bill at the output
            # rate even though they're never shown to the user.
            response = _draft_client.chat.completions.create(
                model=DRAFT_MODEL,
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
                ],
                extra_body={"thinking": {"type": "disabled"}},
            )

            # CHANGED: OpenAI-style response shape —
            # `response.choices[0].message.content` instead of Ollama's
            # `response["message"]["content"]`.
            text = response.choices[0].message.content.strip()

            return text if text else fallback

        except Exception:

            # DeepSeek unreachable/slow — never let narration block the survey
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
        subcategory = answers.get("subcategory", "")

        # Prefer the connector-type-specific showroom page (e.g. the
        # exact SMA page) over the generic RF Connectors landing page,
        # falling back to the category-level URL when we don't have a
        # dedicated page for that specific connector type.
        website = (
            CONNECTOR_TYPE_URLS.get(subcategory)
            or CATEGORY_URLS.get(category, CATEGORY_URLS.get("_default"))
        )

        # The most specific thing the customer picked: the exact leaf
        # product (e.g. "SMA F RA LMR 100 CRIMP GP") if the survey drilled
        # that deep, otherwise whatever they described in their own words,
        # otherwise the connector type/category itself.
        subject_item = (
            answers.get("product_variant")
            or subcategory
            or category
        )

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
        product_variant = answers.get("product_variant", "")
        quantity = answers.get("quantity", 1)
        email = answers.get("email", "")

        # The exact item the customer wants quoted. If the survey drilled
        # down to a specific leaf SKU, that's the precise thing to quote —
        # not the connector-type category above it.
        exact_item = product_variant or subcategory or category

        # Datasheets only exist for the RF Connector leaf-product flow.
        # For every other category (Antennas, Cable Assemblies, etc.) or
        # a free-text connector description, there was never a datasheet
        # to begin with — so say nothing rather than raising a "missing"
        # flag that reads as an error to the customer.
        datasheet_url = self._find_datasheet_url(product_variant) if product_variant else None
        pricing_line = self._pricing_line(product_variant or subcategory, quantity)

        datasheet_line = (
            f"Datasheet URL for this exact item: {datasheet_url}\n" if datasheet_url else ""
        )

        pricing_block = (
            f"Pricing note, written from the buyer's own voice (include naturally, don't just paste it): {pricing_line}\n"
            if pricing_line else ""
        )

        prompt = f"""Write a short, professional purchase-inquiry email on behalf of a customer, addressed to the Synergy Telecom sales team.

Customer email: {email}
Product category: {category}
Connector type: {subcategory}
EXACT item requested (quote this precise part — do not generalize or substitute a different variant): {exact_item}
Quantity requested: {quantity}
{pricing_block}{datasheet_line}
Rules:
- Under 120 words.
- You MUST state the EXACT item text above, verbatim, so the sales team quotes the correct variant — do not paraphrase, shorten, or generalize the part name.
- Include the datasheet URL only if one is given above, phrased as the buyer citing it themselves to confirm they mean this exact part (e.g. "here's the datasheet for the exact part I need: {{url}}") — never phrase it as the company directing the buyer to look at "their" datasheet, since the buyer is the one sending this link, not receiving it. Do not mention datasheets at all if none is given, and never say one is missing.
- Include the pricing note only if one is given above, written as something the buyer themselves would say (e.g. "I saw it listed at X" or "please confirm the price") — never phrase it as the company describing its own confirmation process, and never invent a price if none is given.
- Do not invent specs, pricing, or stock availability beyond what's given above.
- Mention the quantity requested.
- Sign off with the customer's email address.
- Return ONLY the email body. No subject line, no preamble, no markdown."""

        fallback = self._fallback_email(exact_item, quantity, email, pricing_line, datasheet_url)

        return self._generate(prompt, fallback)

    def _fallback_email(self, exact_item, quantity, email, pricing_line, datasheet_url):

        datasheet_part = f"\nDatasheet: {datasheet_url}\n" if datasheet_url else ""
        pricing_part = f"\n{pricing_line}\n" if pricing_line else ""

        return (
            f"Hello,\n\n"
            f"I'm interested in {quantity} unit(s) of the following exact item:\n"
            f"{exact_item}\n"
            f"{datasheet_part}"
            f"{pricing_part}\n"
            f"Could you please share a quote and confirm availability?\n\n"
            f"Thanks,\n{email}"
        )

    def _pricing_line(self, subcategory_value, quantity):

        option = self._find_leaf_option(subcategory_value)
        unit_price = option.get("price") if option else None

        # No price on file — say nothing. "Could you share a quote" already
        # covers this; a fabricated "to be confirmed by our sales team"
        # line reads as the company talking about itself in the customer's
        # own outgoing email, which is backwards.
        if unit_price is None:
            return ""

        try:
            total = unit_price * int(quantity)
        except (TypeError, ValueError):
            total = unit_price

        # Written from the buyer's voice, referencing a price they saw
        # listed — not the company describing its own confirmation process.
        return (
            f"Based on the listed unit price of {CURRENCY}{unit_price:,.2f}, "
            f"I estimate the total for {quantity} unit(s) at {CURRENCY}{total:,.2f} "
            f"— please confirm before I proceed."
        )

    def _find_leaf_option(self, value):

        for node in self.survey["nodes"].values():

            for option in node.get("options", []):

                if option["value"] == value:
                    return option

        return None

    def _find_datasheet_url(self, product_variant_value):

        option = self._find_leaf_option(product_variant_value)
        return option.get("datasheet_url") if option else None

    def _log_lead(self, answers):

        try:
            with LEADS_LOCK:
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
