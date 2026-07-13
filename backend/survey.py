"""
Survey Definitions

Contains only survey data.
No business logic should exist here.
"""

SURVEYS = {
    "product_finder": {

        "start": "product",

        "nodes": {

            # -------------------------------------------------
            # Product Category
            # -------------------------------------------------

            "product": {

                "question": "What product are you looking for?",

                "key": "product",

                "options": [

                    {
                        "text": "RF Connectors",
                        "value": "RF Connectors",
                        "next": "rf_connectors"
                    },

                    {
                        "text": "Cable Assemblies",
                        "value": "Cable Assemblies",
                        "next": "cable_assemblies"
                    },

                    {
                        "text": "Microwave Components",
                        "value": "Microwave Components",
                        "next": "microwave_components"
                    },

                    {
                        "text": "Antennas",
                        "value": "Antennas",
                        "next": "antennas"
                    },

                    {
                        "text": "Waveguides",
                        "value": "Waveguides",
                        "next": "waveguides"
                    },

                    {
                        "text": "RF Adaptors",
                        "value": "RF Adaptors",
                        "next": "rf_adaptors"
                    },

                    {
                        "text": "Filters",
                        "value": "Filters",
                        "next": "filters"
                    },

                    {
                        "text": "Installation Tools & Kits",
                        "value": "Installation Tools & Kits",
                        "next": "installation_tools"
                    },

                    {
                        "text": "Test & Measurement",
                        "value": "Test & Measurement",
                        "next": "test_measurement"
                    }

                ]

            },

            # -------------------------------------------------
            # RF Connectors
            # -------------------------------------------------

            "rf_connectors": {

                "question": "Which RF Connector?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "SMA",
                        "value": "SMA",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "RP-SMA",
                        "value": "RP-SMA",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "N-Type",
                        "value": "N-Type",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "TNC",
                        "value": "TNC",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "BNC",
                        "value": "BNC",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "SMB",
                        "value": "SMB",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "MCX",
                        "value": "MCX",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "MMCX",
                        "value": "MMCX",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "7/16 DIN",
                        "value": "7/16 DIN",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "UHF (PL-259)",
                        "value": "UHF (PL-259)",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "F-Type",
                        "value": "F-Type",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Cable Assemblies
            # -------------------------------------------------

            "cable_assemblies": {

                "question": "Which type of Cable Assembly?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Standard Coaxial Jumper",
                        "value": "Standard Coaxial Jumper",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Low PIM Test Cable",
                        "value": "Low PIM Test Cable",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Custom Length Assembly",
                        "value": "Custom Length Assembly",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Right-Angle Assembly",
                        "value": "Right-Angle Assembly",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Armored / Outdoor Assembly",
                        "value": "Armored / Outdoor Assembly",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "IBS / DAS Cable Assembly",
                        "value": "IBS / DAS Cable Assembly",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Microwave Components
            # -------------------------------------------------

            "microwave_components": {

                "question": "Which Microwave Component?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Attenuator",
                        "value": "Attenuator",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Power Divider / Splitter",
                        "value": "Power Divider / Splitter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Coupler",
                        "value": "Coupler",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Combiner",
                        "value": "Combiner",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Duplexer",
                        "value": "Duplexer",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Diplexer",
                        "value": "Diplexer",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Balun",
                        "value": "Balun",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Bias Tee",
                        "value": "Bias Tee",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block",
                        "value": "DC Block",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Dummy Load",
                        "value": "Dummy Load",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "RF Switch",
                        "value": "RF Switch",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Surge Arrester",
                        "value": "Surge Arrester",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Antennas
            # -------------------------------------------------

            "antennas": {

                "question": "Which Antenna?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Omni / Dome Antenna",
                        "value": "Omni / Dome Antenna",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Panel / Directional Antenna",
                        "value": "Panel / Directional Antenna",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Whip Antenna",
                        "value": "Whip Antenna",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Horn Antenna",
                        "value": "Horn Antenna",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Log Periodic",
                        "value": "Log Periodic",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "HF / VHF / UHF Antenna",
                        "value": "HF / VHF / UHF Antenna",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "GPS Antenna",
                        "value": "GPS Antenna",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "IoT / LoRa / RFID Antenna",
                        "value": "IoT / LoRa / RFID Antenna",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Waveguides
            # -------------------------------------------------

            "waveguides": {

                "question": "Which Waveguide product?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Waveguide Adapters",
                        "value": "Waveguide Adapters",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Bends",
                        "value": "Waveguide Bends",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Flexible Waveguide",
                        "value": "Flexible Waveguide",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Twist",
                        "value": "Waveguide Twist",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide-to-Coax Transition",
                        "value": "Waveguide-to-Coax Transition",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # RF Adaptors
            # -------------------------------------------------

            "rf_adaptors": {

                "question": "Which RF Adaptor?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Same-Series Adapter",
                        "value": "Same-Series Adapter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Between-Series Adapter",
                        "value": "Between-Series Adapter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Right-Angle Adapter",
                        "value": "Right-Angle Adapter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Bulkhead Adapter",
                        "value": "Bulkhead Adapter",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Filters
            # -------------------------------------------------

            "filters": {

                "question": "Which type of Filter?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Bandpass Filter",
                        "value": "Bandpass Filter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Bandstop / Notch Filter",
                        "value": "Bandstop / Notch Filter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Low-Pass Filter",
                        "value": "Low-Pass Filter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "High-Pass Filter",
                        "value": "High-Pass Filter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Cavity Filter",
                        "value": "Cavity Filter",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Installation Tools & Kits
            # -------------------------------------------------

            "installation_tools": {

                "question": "Which Installation product?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "IBS / DAS Installation Kit",
                        "value": "IBS / DAS Installation Kit",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Crimping Tool",
                        "value": "Crimping Tool",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Cable Stripping Tool",
                        "value": "Cable Stripping Tool",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Torque Wrench",
                        "value": "Torque Wrench",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Termination Kit",
                        "value": "Termination Kit",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Test & Measurement
            # -------------------------------------------------

            "test_measurement": {

                "question": "Which Test & Measurement product?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Oscilloscope",
                        "value": "Oscilloscope",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Spectrum Analyzer",
                        "value": "Spectrum Analyzer",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Signal Generator",
                        "value": "Signal Generator",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "RF Power Meter",
                        "value": "RF Power Meter",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Site Master / Cable & Antenna Analyzer",
                        "value": "Site Master / Cable & Antenna Analyzer",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Calibration Kit",
                        "value": "Calibration Kit",
                        "price": None,
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Quantity
            # -------------------------------------------------

            "quantity": {

                "question": "How many units do you need?",

                "key": "quantity",

                "type": "text",

                "validate": "quantity",

                "min": 1,

                "max": 9999,

                "default": 1,

                "next": "email"

            },

            # -------------------------------------------------
            # Email
            # -------------------------------------------------

            "email": {

                "question": "Please enter your email address.",

                "key": "email",

                "type": "text",

                "validate": "email",

                "next": "complete"

            },

            # -------------------------------------------------
            # End
            # -------------------------------------------------

            "complete": {

                "message": (
                    "Thank you! Your request has been recorded. "
                    "Our team will contact you shortly."
                )

            }

        }

    }

}


# ==================================================
# Pricing
#
# Every leaf option above now has a "price" field, currently set to
# None on purpose — I don't have Synergy Telecom's real price list, and
# shipping guessed numbers to real customers requesting quotes would be
# worse than not showing a price at all. survey_engine.py already
# handles None gracefully (falls back to "Price available on request"
# and skips the subtotal math). Fill in real per-unit prices (in INR)
# here once you have them and pricing/quantity math switches on
# automatically — no other code changes needed.
#
# Example: "price": 45.00
# ==================================================

CURRENCY = "₹"


# ==================================================
# Category -> product page URL
#
# Used to build the "View this product online" action once a survey
# finishes. The RF Connectors / Cable Assemblies / Antennas / RF
# Adaptors links below are verified against rfconnector.in's real
# showroom structure. The rest are best-guess paths on synergytpl.com —
# confirm and swap in the real URLs before relying on them.
# ==================================================

CATEGORY_URLS = {
    "RF Connectors": "https://rfconnector.in/product_showroom/rf_connector",
    "Cable Assemblies": "https://rfconnector.in/product_showroom/cable_assembly",
    "Antennas": "https://rfconnector.in/product_showroom/antenna",
    "RF Adaptors": "https://rfconnector.in/product_showroom/rf_adaptor",

    # TODO: verify these against the live site structure
    "Microwave Components": "https://synergytpl.com/microwave-components",
    "Waveguides": "https://synergytpl.com/waveguides",
    "Filters": "https://synergytpl.com/filters",
    "Installation Tools & Kits": "https://synergytpl.com/installation-tools",
    "Test & Measurement": "https://synergytpl.com/test-measurement",

    "_default": "https://www.rfconnector.in/product_showroom"
}