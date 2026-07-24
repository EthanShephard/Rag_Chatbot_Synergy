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
                    },

                    {
                        "text": "Masts",
                        "value": "Masts",
                        "next": "masts"
                    }

                ]

            },

            # -------------------------------------------------
            # RF Connectors — full connector-type list, each
            # branching into its own leaf-product picker (or a
            # free-text fallback where we don't have a granular
            # catalog list scraped for that type).
            # -------------------------------------------------

            "rf_connectors": {

                "question": "Which RF Connector type?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "1.85mm",
                        "value": "1.85mm",
                        "next": "connector_1_85mm"
                    },

                    {
                        "text": "2.4mm",
                        "value": "2.4mm",
                        "next": "connector_2_4mm"
                    },

                    {
                        "text": "2.92mm",
                        "value": "2.92mm",
                        "next": "connector_2_92mm"
                    },

                    {
                        "text": "3.5mm",
                        "value": "3.5mm",
                        "next": "connector_3_5mm"
                    },

                    {
                        "text": "BMA",
                        "value": "BMA",
                        "next": "connector_bma"
                    },

                    {
                        "text": "BNC",
                        "value": "BNC",
                        "next": "connector_bnc"
                    },

                    {
                        "text": "BQ",
                        "value": "BQ",
                        "next": "connector_bq"
                    },

                    {
                        "text": "C",
                        "value": "C",
                        "next": "connector_c"
                    },

                    {
                        "text": "C4",
                        "value": "C4",
                        "next": "connector_c4"
                    },

                    {
                        "text": "Circular Connector",
                        "value": "Circular Connector",
                        "next": "connector_circular_connector"
                    },

                    {
                        "text": "CRC9",
                        "value": "CRC9",
                        "next": "connector_crc9"
                    },

                    {
                        "text": "DIN / 4.3-1.0",
                        "value": "DIN / 4.3-1.0",
                        "next": "connector_din_4_3_1_0"
                    },

                    {
                        "text": "F Type",
                        "value": "F Type",
                        "next": "connector_f_type"
                    },

                    {
                        "text": "High Freq Connector",
                        "value": "High Freq Connector",
                        "next": "connector_high_freq_connector"
                    },

                    {
                        "text": "HN",
                        "value": "HN",
                        "next": "connector_hn"
                    },

                    {
                        "text": "KMX3",
                        "value": "KMX3",
                        "next": "connector_kmx3"
                    },

                    {
                        "text": "L9",
                        "value": "L9",
                        "next": "connector_l9"
                    },

                    {
                        "text": "MCX",
                        "value": "MCX",
                        "next": "connector_mcx"
                    },

                    {
                        "text": "Microdot",
                        "value": "Microdot",
                        "next": "connector_microdot"
                    },

                    {
                        "text": "MMCX",
                        "value": "MMCX",
                        "next": "connector_mmcx"
                    },

                    {
                        "text": "N-Type",
                        "value": "N-Type",
                        "next": "connector_n_type"
                    },

                    {
                        "text": "NEX10 (Feeder Cable)",
                        "value": "NEX10 (Feeder Cable)",
                        "next": "connector_nex10_feeder_cable"
                    },

                    {
                        "text": "QMA",
                        "value": "QMA",
                        "next": "connector_qma"
                    },

                    {
                        "text": "QN",
                        "value": "QN",
                        "next": "connector_qn"
                    },

                    {
                        "text": "RP-SMA",
                        "value": "RP-SMA",
                        "next": "connector_rp_sma"
                    },

                    {
                        "text": "SAA",
                        "value": "SAA",
                        "next": "connector_saa"
                    },

                    {
                        "text": "SMA",
                        "value": "SMA",
                        "next": "connector_sma"
                    },

                    {
                        "text": "SMB",
                        "value": "SMB",
                        "next": "connector_smb"
                    },

                    {
                        "text": "SMC",
                        "value": "SMC",
                        "next": "connector_smc"
                    },

                    {
                        "text": "SMP",
                        "value": "SMP",
                        "next": "connector_smp"
                    },

                    {
                        "text": "SMZ",
                        "value": "SMZ",
                        "next": "connector_smz"
                    },

                    {
                        "text": "SSMA",
                        "value": "SSMA",
                        "next": "connector_ssma"
                    },

                    {
                        "text": "SSMB",
                        "value": "SSMB",
                        "next": "connector_ssmb"
                    },

                    {
                        "text": "TNC",
                        "value": "TNC",
                        "next": "connector_tnc"
                    },

                    {
                        "text": "TQ",
                        "value": "TQ",
                        "next": "connector_tq"
                    },

                    {
                        "text": "Triaxial",
                        "value": "Triaxial",
                        "next": "connector_triaxial"
                    },

                    {
                        "text": "UHF",
                        "value": "UHF",
                        "next": "connector_uhf"
                    }

                ]

            },

            # ---- 1.85mm ----

            "connector_1_85mm": {

                "question": "Please describe the exact 1.85mm connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- 2.4mm ----

            "connector_2_4mm": {

                "question": "Please describe the exact 2.4mm connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- 2.92mm ----

            "connector_2_92mm": {

                "question": "Please describe the exact 2.92mm connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- 3.5mm ----

            "connector_3_5mm": {

                "question": "Please describe the exact 3.5mm connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- BMA ----

            "connector_bma": {

                "question": "Please describe the exact BMA connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- BNC ----

            "connector_bnc": {

                "question": "Which BNC connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "BNC M RG 59 Compression",
                        "value": "BNC M RG 59 Compression",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/conncector/BNC_M_RG_59_Compression.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Bnc m rg 141 crimp",
                        "value": "Bnc m rg 141 crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/conncector/Bnc_m_rg_141_crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M LMR 400 CLAMP",
                        "value": "BNC M LMR 400 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_M_LMR_400_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC female four hole",
                        "value": "BNC female four hole",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_female_four_hole.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Bnc f LMR 200 clamp",
                        "value": "Bnc f LMR 200 clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/conncector/Bnc_f_LMR_200_clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Male Crimp Connector For RG59 Cable",
                        "value": "BNC Male Crimp Connector For RG59 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Male_Crimp_Connector_For_RG59_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M RG 59 Plastic hood",
                        "value": "BNC M RG 59 Plastic hood",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_M_RG_59_Plastic_hood.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Female BH For BT3002 Cable",
                        "value": "BNC Female BH For BT3002 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Female_BH_For_BT3002_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC F BT 3002 CRIMP",
                        "value": "BNC F BT 3002 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_F_BT_3002_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Male for RG 59 CP Crimped",
                        "value": "BNC Male for RG 59 CP Crimped",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Male_for_RG_59_CP_Crimped.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Bnc m lmr 100 crimp",
                        "value": "Bnc m lmr 100 crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/conncector/Bnc_m_lmr_100_crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC F LMR 240 CRIMP",
                        "value": "BNC F LMR 240 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_F_LMR_240_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M RG 11 CRIMP",
                        "value": "BNC M RG 11 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_M_RG_11_CRIMP.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M RG 59 CPS",
                        "value": "BNC M RG 59 CPS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_M_RG_59_CPS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC F LMR 100 CRIMP",
                        "value": "BNC F LMR 100 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_F_LMR_100_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC F 4 HOLE",
                        "value": "BNC F 4 HOLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_F_4_HOLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Male for BT 3002 CPS",
                        "value": "BNC Male for BT 3002 CPS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Male_for_BT_3002_CPS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M 4 HOLE",
                        "value": "BNC M 4 HOLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_M_4_HOLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC female BH SOLDER",
                        "value": "BNC female BH SOLDER",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_female_BH_SOLDER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Female BH For BT3002 CPS",
                        "value": "BNC Female BH For BT3002 CPS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Female_BH_For_BT3002_CPS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Male for BT 3002 Cable",
                        "value": "BNC Male for BT 3002 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Male_for_BT_3002_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC Male for BT 3002 Crimp",
                        "value": "BNC Male for BT 3002 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_Male_for_BT_3002_Crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M RG 59 CLAMP",
                        "value": "BNC M RG 59 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/BNC/BNC_M_RG_59_CLAMP.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- BQ ----

            "connector_bq": {

                "question": "Please describe the exact BQ connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- C ----

            "connector_c": {

                "question": "Please describe the exact C connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- C4 ----

            "connector_c4": {

                "question": "Please describe the exact C4 connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- Circular Connector ----

            "connector_circular_connector": {

                "question": "Please describe the exact Circular Connector connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- CRC9 ----

            "connector_crc9": {

                "question": "Which CRC9 connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "CRC9 LMR100",
                        "value": "CRC9 LMR100",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/CRC9/CRC9_LMR100.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- DIN / 4.3-1.0 ----

            "connector_din_4_3_1_0": {

                "question": "Which DIN / 4.3-1.0 connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "DIN M RA FOR 1 2 LDF",
                        "value": "DIN M RA FOR 1 2 LDF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_RA_FOR_1_2_LDF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Din Male Right Angle For 1 2 Cable",
                        "value": "Din Male Right Angle For 1 2 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/Din_Male_Right_Angle_For_1_2_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Male Connector for 7-8 Super Flex Cable",
                        "value": "7-16 DIN Male Connector for 7-8 Super Flex Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/7-16_DIN_Male_Connector_for_7-8_Super_Flex_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 3 10 female clamp connector for halfinch superflex",
                        "value": "4 3 10 female clamp connector for halfinch superflex",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/minidin/4_3_10_female_clamp_connector_for_halfinch_superflex.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Din F Male For 7 8 Cable",
                        "value": "Din F Male For 7 8 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/Din_F_Male_For_7_8_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Male 1 2 Cable",
                        "value": "DIN Male 1 2 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Male_1_2_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "43 10 M for 12 SF Solder",
                        "value": "43 10 M for 12 SF Solder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/DIN1-2/43_10_M_for_12_SF_Solder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Female 4 Hole PANEL",
                        "value": "DIN Female 4 Hole PANEL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Female_4_Hole_PANEL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DINM-DINMRA",
                        "value": "DINM-DINMRA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DINM-DINMRA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Din male half inch ldf solder connector",
                        "value": "Din male half inch ldf solder connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din/Din_male_half_inch_ldf_solder_connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M 7 8 Alu Clamp",
                        "value": "N M 7 8 Alu Clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/DIN7-8/N_M_7_8_Alu_Clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M LMR 240 CRIMP",
                        "value": "DIN M LMR 240 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_LMR_240_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN F for 1 4 SF Cable",
                        "value": "DIN F for 1 4 SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/din1-4/DIN_F_for_1_4_SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M for 1 4 SF Cable",
                        "value": "DIN M for 1 4 SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_for_1_4_SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Female Connector For 1-4In fleixible Cable",
                        "value": "7-16 DIN Female Connector For 1-4In fleixible Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/7-16_DIN_Female_Connector_For_1-4In_fleixible_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M FOR 1 4 SF",
                        "value": "DIN M FOR 1 4 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/din1-4/DIN_M_FOR_1_4_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Male 4 Hole PANEL",
                        "value": "DIN Male 4 Hole PANEL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Male_4_Hole_PANEL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 3 10 female connecftor for half inch flexible cable",
                        "value": "4 3 10 female connecftor for half inch flexible cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/minidin/4_3_10_female_connecftor_for_half_inch_flexible_cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN MALE 7BY8 CLAMP1",
                        "value": "DIN MALE 7BY8 CLAMP1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din/DIN_MALE_7BY8_CLAMP1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M LMR 200 CRIMP",
                        "value": "DIN M LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Male Right Angle Connector For 1-4In Superflexible Cable",
                        "value": "7-16 DIN Male Right Angle Connector For 1-4In Superflexible Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/7-16_DIN_Male_Right_Angle_Connector_For_1-4In_Superflexible_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Male 1 2SF Cable",
                        "value": "DIN Male 1 2SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Male_1_2SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Female Connector for 7-8 Flex Cable",
                        "value": "7-16 DIN Female Connector for 7-8 Flex Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/DIN_7-8/7-16_DIN_Female_Connector_for_7-8_Flex_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN F CRIMP FOR LMR 400",
                        "value": "DIN F CRIMP FOR LMR 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_F_CRIMP_FOR_LMR_400.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN F FOR 1 2 SF",
                        "value": "DIN F FOR 1 2 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_F_FOR_1_2_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M FOR 1 2 SF",
                        "value": "DIN M FOR 1 2 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_FOR_1_2_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Male Right Angle Connector For 1-4 flexible Cable",
                        "value": "7-16 DIN Male Right Angle Connector For 1-4 flexible Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/din1-4/7-16_DIN_Male_Right_Angle_Connector_For_1-4_flexible_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN F 32mm SQ Mount Connector with Receptacle",
                        "value": "DIN F 32mm SQ Mount Connector with Receptacle",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_F_32mm_SQ_Mount_Connector_with_Receptacle.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M FOR 1 4 LDF",
                        "value": "DIN M FOR 1 4 LDF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_FOR_1_4_LDF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Male Connector for 7-8 Foam Feeder Cable",
                        "value": "7-16 DIN Male Connector for 7-8 Foam Feeder Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/7-16_DIN_Male_Connector_for_7-8_Foam_Feeder_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DINM-DINM",
                        "value": "DINM-DINM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DINM-DINM.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN FEMALE BULKHEAD RIGHT ANGLE LMR 200 CRIMP CONNECTOR",
                        "value": "DIN FEMALE BULKHEAD RIGHT ANGLE LMR 200 CRIMP CONNECTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din/DIN_FEMALE_BULKHEAD_RIGHT_ANGLE_LMR_200_CRIMP_CONNECTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "mini din male clamp connector for halfinch",
                        "value": "mini din male clamp connector for halfinch",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/mini_din_male_clamp_connector_for_halfinch.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Connector RG-401 Cable",
                        "value": "DIN Connector RG-401 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Connector_RG-401_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 3 10 female solder connector for halfinch superflex",
                        "value": "4 3 10 female solder connector for halfinch superflex",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/minidin/4_3_10_female_solder_connector_for_halfinch_superflex.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Female Bulkhead Connector For RG402 141In Cable",
                        "value": "DIN Female Bulkhead Connector For RG402 141In Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Female_Bulkhead_Connector_For_RG402_141In_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "7-16 DIN Female Connector for 7-8 Super Flex Cable",
                        "value": "7-16 DIN Female Connector for 7-8 Super Flex Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/7-16_DIN_Female_Connector_for_7-8_Super_Flex_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN F for 1 2 Feeder",
                        "value": "DIN F for 1 2 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_F_for_1_2_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 3 10 male connecftor for half inch flexible cable",
                        "value": "4 3 10 male connecftor for half inch flexible cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/din_new/minidin/4_3_10_male_connecftor_for_half_inch_flexible_cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN female 1 1 4 Cable",
                        "value": "DIN female 1 1 4 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_female_1_1_4_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4.3 1.0 (M) %20for 12 SF Sollar",
                        "value": "4.3 1.0 (M) %20for 12 SF Sollar",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/4.3_1.0_%28M%29_%20for_12_SF_Sollar.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN Male St LMR 400 Crimp Type",
                        "value": "DIN Male St LMR 400 Crimp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_Male_St_LMR_400_Crimp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN F FOR 1 5 8 LDF",
                        "value": "DIN F FOR 1 5 8 LDF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_F_FOR_1_5_8_LDF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Din Male For 7 8 Cable",
                        "value": "Din Male For 7 8 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/Din_Male_For_7_8_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN M LMR 500 CLAMP",
                        "value": "DIN M LMR 500 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/DIN/DIN_M_LMR_500_CLAMP.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- F Type ----

            "connector_f_type": {

                "question": "Please describe the exact F Type connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- High Freq Connector ----

            "connector_high_freq_connector": {

                "question": "Please describe the exact High Freq Connector connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- HN ----

            "connector_hn": {

                "question": "Which HN connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "HN Male Connector RG217",
                        "value": "HN Male Connector RG217",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/HN/HN_Male_Connector_RG217.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HN(F) 4 HOLE PANNEL MOUNT",
                        "value": "HN(F) 4 HOLE PANNEL MOUNT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/HN/HN(F)_4_HOLE_PANNEL_MOUNT.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- KMX3 ----

            "connector_kmx3": {

                "question": "Which KMX3 connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "KMX3 Male",
                        "value": "KMX3 Male",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/KMX3/KMX3_Male.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- L9 ----

            "connector_l9": {

                "question": "Which L9 connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "L9 F RA BT",
                        "value": "L9 F RA BT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/L9_CONNECTOR/L9_F_RA_BT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1.6 5.6 Male Crimp Connector For BT3002 Cable",
                        "value": "1.6 5.6 Male Crimp Connector For BT3002 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/L9_CONNECTOR/1.6_5.6_Male_Crimp_Connector_For_BT3002_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "L9 M BT CPS",
                        "value": "L9 M BT CPS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/L9_CONNECTOR/L9_M_BT_CPS.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- MCX ----

            "connector_mcx": {

                "question": "Which MCX connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "MCX F PCB MOUNT 50 OHM",
                        "value": "MCX F PCB MOUNT 50 OHM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MCX/MCX_F_PCB_MOUNT_50_OHM.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MCX F SR 085 SF 85 RG405",
                        "value": "MCX F SR 085 SF 85 RG405",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MCX/MCX_F_SR_085_SF_85_RG405.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MCX M PCB MOUNT 50 OHM",
                        "value": "MCX M PCB MOUNT 50 OHM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MCX/MCX_M_PCB_MOUNT_50_OHM.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MCX M RA BT 3002 CRIMP",
                        "value": "MCX M RA BT 3002 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MCX/MCX_M_RA_BT_3002_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MCX F R A PCB MOUNT 50 OHM",
                        "value": "MCX F R A PCB MOUNT 50 OHM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MCX/MCX_F_R_A_PCB_MOUNT_50_OHM.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- Microdot ----

            "connector_microdot": {

                "question": "Which Microdot connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "10 32 microdot connector RG316",
                        "value": "10 32 microdot connector RG316",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/Microdotconnector/10_32_microdot_connector_RG316.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- MMCX ----

            "connector_mmcx": {

                "question": "Which MMCX connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "MMCX Female PCB",
                        "value": "MMCX Female PCB",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MMCX/MMCX_Female_PCB.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MMCX M R A RG 316",
                        "value": "MMCX M R A RG 316",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MMCX/MMCX_M_R_A_RG_316.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MMCX M ST RG 316",
                        "value": "MMCX M ST RG 316",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/MMCX/MMCX_M_ST_RG_316.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- N-Type ----

            "connector_n_type": {

                "question": "Which N-Type connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N M RA for 1 2 Superflex Cable",
                        "value": "N M RA for 1 2 Superflex Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_for_1_2_Superflex_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F FN BH LMR 100 CRIMP",
                        "value": "N F FN BH LMR 100 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_FN_BH_LMR_100_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "n m 1-2 sf",
                        "value": "n m 1-2 sf",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N_1-2/n_m_1-2_sf.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M LMR 300 CRIMP",
                        "value": "N M LMR 300 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_LMR_300_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female FOR 1 2 FLX CABLE",
                        "value": "N Female FOR 1 2 FLX CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_FOR_1_2_FLX_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female FN BH LMR 300 CLAMP",
                        "value": "N Female FN BH LMR 300 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_FN_BH_LMR_300_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M for 7 8 Feeder",
                        "value": "N M for 7 8 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_for_7_8_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F for 1 4 SF",
                        "value": "N F for 1 4 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_for_1_4_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for 1 4 SF Cable",
                        "value": "N Male for 1 4 SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_1_4_SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female RA for LMR240 Cable Crimp Type",
                        "value": "N Female RA for LMR240 Cable Crimp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_RA_for_LMR240_Cable_Crimp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RG 6 CRIMP",
                        "value": "N M RG 6 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RG_6_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M R A 1 2 LDF",
                        "value": "N M R A 1 2 LDF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_R_A_1_2_LDF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female LMR 200 CRIMP",
                        "value": "N Female LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE RA CLAMP LMR300",
                        "value": "N MALE RA CLAMP LMR300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_RA_CLAMP_LMR300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F for 1 5 8 Feeder",
                        "value": "N F for 1 5 8 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_for_1_5_8_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE CLAMP RG217",
                        "value": "N MALE CLAMP RG217",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_CLAMP_RG217.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female CRIMP LMR400 CABLE",
                        "value": "N Female CRIMP LMR400 CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_CRIMP_LMR400_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M for 1 4 Feeder",
                        "value": "N M for 1 4 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_for_1_4_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M 1-4 FLEX",
                        "value": "N M 1-4 FLEX",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N-1-4/N_M_1-4_FLEX.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 1-4 F",
                        "value": "N F 1-4 F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N-1-4/N_F_1-4_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RG 141 SUCO",
                        "value": "N M RG 141 SUCO",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RG_141_SUCO.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for RG58 Cable Clamp Type",
                        "value": "N Male for RG58 Cable Clamp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_RG58_Cable_Clamp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female 4 hole 175mm",
                        "value": "N Female 4 hole 175mm",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_4_hole_175mm.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female LMR 200 CRIMP CPS%20backup",
                        "value": "N Female LMR 200 CRIMP CPS%20backup",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_LMR_200_CRIMP_CPS%20backup.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M LMR 400 CRIMP",
                        "value": "N M LMR 400 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_LMR_400_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F FN BH LMR 100 CPS",
                        "value": "N F FN BH LMR 100 CPS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_FN_BH_LMR_100_CPS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F for RG 213 Crimp",
                        "value": "N F for RG 213 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_for_RG_213_Crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for 1 1 4 Feeder Cable",
                        "value": "N Male for 1 1 4 Feeder Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_1_1_4_Feeder_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male LMR 600 Clamp type",
                        "value": "N Male LMR 600 Clamp type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_LMR_600_Clamp_type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F for 7 8 Feeder",
                        "value": "N F for 7 8 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/n-7-8/N_F_for_7_8_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RG 11 CRIMP",
                        "value": "N M RG 11 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RG_11_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M Right Angle Connector For Rg 402 SM 141 Cable",
                        "value": "N M Right Angle Connector For Rg 402 SM 141 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_Right_Angle_Connector_For_Rg_402_SM_141_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female BH for Splitter",
                        "value": "N Female BH for Splitter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_BH_for_Splitter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F for 13 8 Feeder",
                        "value": "N F for 13 8 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_for_13_8_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for LMR 400 Clamp Type",
                        "value": "N Male for LMR 400 Clamp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_LMR_400_Clamp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE CLAMP LMR300",
                        "value": "N MALE CLAMP LMR300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_CLAMP_LMR300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F FN BH LMR 100 CLAMP",
                        "value": "N F FN BH LMR 100 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_FN_BH_LMR_100_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male Rightangle LMR 300 Clamp",
                        "value": "N Male Rightangle LMR 300 Clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_Rightangle_LMR_300_Clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M R A 1 4 SF",
                        "value": "N M R A 1 4 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_R_A_1_4_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for LMR300 CLAMP",
                        "value": "N Male for LMR300 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_LMR300_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F Flange connector",
                        "value": "N F Flange connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_Flange_connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 4 HOLE 25MM",
                        "value": "N F 4 HOLE 25MM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_4_HOLE_25MM.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female for 1 2 SF Cable",
                        "value": "N Female for 1 2 SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_for_1_2_SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M R A RG 141 SUCO",
                        "value": "N M R A RG 141 SUCO",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_R_A_RG_141_SUCO.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M for 1 4 SF",
                        "value": "N M for 1 4 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_for_1_4_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE CLAMP LMR900",
                        "value": "N MALE CLAMP LMR900",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_CLAMP_LMR900.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female LMR 200 CRIMP CONNECTOR",
                        "value": "N Female LMR 200 CRIMP CONNECTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_LMR_200_CRIMP_CONNECTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F FN BH LMR 200 CRIMP",
                        "value": "N F FN BH LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_FN_BH_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "sma lmr 100 clamp",
                        "value": "sma lmr 100 clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/new%20connector/sma_lmr_100_clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M 4 HOLE",
                        "value": "N M 4 HOLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_4_HOLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female SQ Flange 19Sq mm",
                        "value": "N Female SQ Flange 19Sq mm",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_SQ_Flange_19Sq_mm.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F FOR 1-2 FLEX CLAMP TYPE",
                        "value": "N F FOR 1-2 FLEX CLAMP TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N_1-2/N_F_FOR_1-2_FLEX_CLAMP_TYPE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M FOR 141 SOCO CABLE",
                        "value": "N M FOR 141 SOCO CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_FOR_141_SOCO_CABLE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA LMR 200 CRIMP HEX",
                        "value": "N M RA LMR 200 CRIMP HEX",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_LMR_200_CRIMP_HEX.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female FOR 1 4 LDF CABLE",
                        "value": "N Female FOR 1 4 LDF CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_FOR_1_4_LDF_CABLE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA 1-4 SF",
                        "value": "N M RA 1-4 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N-1-4/N_M_RA_1-4_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female Bulkhead Crimp Connector For RG316 Cable",
                        "value": "N Female Bulkhead Crimp Connector For RG316 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_Bulkhead_Crimp_Connector_For_RG316_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for 13 8 Cable",
                        "value": "N Male for 13 8 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_13_8_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE RA CRIMP LMR400",
                        "value": "N MALE RA CRIMP LMR400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_RA_CRIMP_LMR400.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for 1 2 SF Cable",
                        "value": "N Male for 1 2 SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_1_2_SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N male for Rg213 Cable Clamp Type",
                        "value": "N male for Rg213 Cable Clamp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_male_for_Rg213_Cable_Clamp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE FLANGE MOUNT CONNECTOR FOR RG402 141 CABLE",
                        "value": "N FEMALE FLANGE MOUNT CONNECTOR FOR RG402 141 CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_FEMALE_FLANGE_MOUNT_CONNECTOR_FOR_RG402_141_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA LMR 200 CRIMP",
                        "value": "N M RA LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 7-8 SF",
                        "value": "N F 7-8 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/n-7-8/N_F_7-8_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA 1-4 F",
                        "value": "N M RA 1-4 F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N-1-4/N_M_RA_1-4_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA LMR 200 CLAMP",
                        "value": "N M RA LMR 200 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_LMR_200_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male for 1 2 Cable",
                        "value": "N Male for 1 2 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_for_1_2_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE CLAMP LMR600",
                        "value": "N MALE CLAMP LMR600",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_CLAMP_LMR600.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female BH Crimp for RG 58 Cable Crimp Type",
                        "value": "N Female BH Crimp for RG 58 Cable Crimp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_BH_Crimp_for_RG_58_Cable_Crimp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M LMR 200 CRIMP",
                        "value": "N M LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female Panel Connector For Receptacle Solder Cup",
                        "value": "N Female Panel Connector For Receptacle Solder Cup",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_Panel_Connector_For_Receptacle_Solder_Cup.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA CLAM LMR400",
                        "value": "N M RA CLAM LMR400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_CLAM_LMR400.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N male Clamp for 3 8 SF",
                        "value": "N male Clamp for 3 8 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_male_Clamp_for_3_8_SF_.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE CRIMP LMR240",
                        "value": "N MALE CRIMP LMR240",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_MALE_CRIMP_LMR240.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N F Sq Flange 19mm",
                        "value": "N F Sq Flange 19mm",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_Sq_Flange_19mm.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 4 HOLE LMR 200 CRIMP",
                        "value": "N F 4 HOLE LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_4_HOLE_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 4 HOLE RG 86",
                        "value": "N F 4 HOLE RG 86",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_4_HOLE_RG_86.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female CRIMP LMR300 CABLE",
                        "value": "N Female CRIMP LMR300 CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_CRIMP_LMR300_CABLE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 4 HOLE LMR 200 CLAMP",
                        "value": "N F 4 HOLE LMR 200 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_4_HOLE_LMR_200_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M for 1 5 8 Feeder",
                        "value": "N M for 1 5 8 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_for_1_5_8_Feeder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F FN BH RG 141 SUCO",
                        "value": "N F FN BH RG 141 SUCO",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_F_FN_BH_RG_141_SUCO.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M for RG 213 Crimp",
                        "value": "N M for RG 213 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_for_RG_213_Crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA LMR 100 CRIMP",
                        "value": "N M RA LMR 100 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_LMR_100_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Femal Clamp Connector For LMR400 Cable",
                        "value": "N Femal Clamp Connector For LMR400 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Femal_Clamp_Connector_For_LMR400_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N male RA for LMR 400 Cable Clamp",
                        "value": "N male RA for LMR 400 Cable Clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_male_RA_for_LMR_400_Cable_Clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M 7-8 F",
                        "value": "N M 7-8 F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/n-7-8/N_M_7-8_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female Bulkhead Right Angle Crimp Connector For LMR200 Cable",
                        "value": "N Female Bulkhead Right Angle Crimp Connector For LMR200 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_Bulkhead_Right_Angle_Crimp_Connector_For_LMR200_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N Connector",
                        "value": "N Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female 4 hole LMR 100 Crimp",
                        "value": "N Female 4 hole LMR 100 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_4_hole_LMR_100_Crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male 1 2 Cable",
                        "value": "N Male 1 2 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_1_2_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Female for LMR 400 Clamp Type",
                        "value": "N Female for LMR 400 Clamp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Female_for_LMR_400_Clamp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M RA LMR 240 CLAMP",
                        "value": "N M RA LMR 240 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_RA_LMR_240_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male Connector For RG402 141In Cable",
                        "value": "N Male Connector For RG402 141In Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_Male_Connector_For_RG402_141In_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N m 1 2",
                        "value": "N m 1 2",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/n_new/N_1-2/N_m_1_2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "PROTECTIVE CAP FOR N",
                        "value": "PROTECTIVE CAP FOR N",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/PROTECTIVE_CAP_FOR_N.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M CLAMP LMR 240",
                        "value": "N M CLAMP LMR 240",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_CLAMP_LMR_240.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N male RA for Rg213 Cable Clamp Type",
                        "value": "N male RA for Rg213 Cable Clamp Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_male_RA_for_Rg213_Cable_Clamp_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M for 13 8 Feeder",
                        "value": "N M for 13 8 Feeder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_M_for_13_8_Feeder.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- NEX10 (Feeder Cable) ----

            "connector_nex10_feeder_cable": {

                "question": "Which NEX10 (Feeder Cable) connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "NEX10 M 14SF CL",
                        "value": "NEX10 M 14SF CL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/NEX10_Connector_For_Feeder_Cable/NEX10_M_14SF_CL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "NEX10 M 12SF CL",
                        "value": "NEX10 M 12SF CL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/NEX10_Connector_For_Feeder_Cable/NEX10_M_12SF_CL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "NEX10 M 12SF SL",
                        "value": "NEX10 M 12SF SL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/NEX10_Connector_For_Feeder_Cable/NEX10_M_12SF_SL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "NEX10 M 14SF SL",
                        "value": "NEX10 M 14SF SL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/NEX10_Connector_For_Feeder_Cable/NEX10_M_14SF_SL.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- QMA ----

            "connector_qma": {

                "question": "Which QMA connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "QMA(M) R A LMR-240 CRIMP",
                        "value": "QMA(M) R A LMR-240 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/QMA/QMA(M)_R_A_LMR-240_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "QMA Connector for RG 58 Cable",
                        "value": "QMA Connector for RG 58 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/QMA/QMA_Connector_for_RG_58_Cable.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- QN ----

            "connector_qn": {

                "question": "Which QN connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "QN right angle male for soco 141 rg402",
                        "value": "QN right angle male for soco 141 rg402",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/QN/QN_right_angle_male_for_soco_141_rg402.PDF",
                        "next": "quantity"
                    }

                ]

            },

            # ---- RP-SMA ----

            "connector_rp_sma": {

                "question": "Please describe the exact RP-SMA connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- SAA ----

            "connector_saa": {

                "question": "Which SAA connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.0 2.3 Male Crimp Connector For BT3002 Cable",
                        "value": "1.0 2.3 Male Crimp Connector For BT3002 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SAA/1.0_2.3_Male_Crimp_Connector_For_BT3002_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "1.0 2.3 Male Solder Pin Crimp Connector For BT3002 Cable",
                        "value": "1.0 2.3 Male Solder Pin Crimp Connector For BT3002 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SAA/1.0_2.3_Male_Solder_Pin_Crimp_Connector_For_BT3002_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "SMZ M FN BH SOLDER GP",
                        "value": "SMZ M FN BH SOLDER GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SAA/SMZ_M_FN_BH_SOLDER_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Saa Male RG 179",
                        "value": "Saa Male RG 179",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SAA/Saa_Male_RG_179.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1.0 2.3 Male Crimp Connector RG59 Cable",
                        "value": "1.0 2.3 Male Crimp Connector RG59 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SAA/1.0_2.3_Male_Crimp_Connector_RG59_Cable.PDF",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SMA ----

            "connector_sma": {

                "question": "Which SMA connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMA F 4 HOLE RG 86 SUCO",
                        "value": "SMA F 4 HOLE RG 86 SUCO",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_4_HOLE_RG_86_SUCO.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA LMR 400 CRIMP GP",
                        "value": "SMA M RA LMR 400 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_LMR_400_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Male 4 Hole",
                        "value": "SMA Male 4 Hole",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Male_4_Hole.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F FN BH LMR 100 CRIMP GP",
                        "value": "SMA F FN BH LMR 100 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_FN_BH_LMR_100_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M Clamp for 3 8 SF",
                        "value": "SMA M Clamp for 3 8 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_Clamp_for_3_8_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F BH with Solder Pot",
                        "value": "SMA F BH with Solder Pot",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_BH_with_Solder_Pot.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F BH PCB MOUNT",
                        "value": "SMA F BH PCB MOUNT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_BH_PCB_MOUNT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Male Right Angle Clamp LMR 300 Specs",
                        "value": "SMA Male Right Angle Clamp LMR 300 Specs",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Male_Right_Angle_Clamp_LMR_300_Specs.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "sma f bulkhead 1.13",
                        "value": "sma f bulkhead 1.13",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/sma_jack_for_1.13/sma_f_bulkhead_1.13.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Male Right Angle Connector For RG405 Cable",
                        "value": "SMA Male Right Angle Connector For RG405 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Male_Right_Angle_Connector_For_RG405_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RG 59 CRIMP GP",
                        "value": "SMA M RG 59 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RG_59_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M 2 HOLE G P",
                        "value": "SMA M 2 HOLE G P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA__M_2_HOLE_G_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M R A RG 141 SUCO G P",
                        "value": "SMA M R A RG 141 SUCO G P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_R_A_RG_141_SUCO_G_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RP LMR 100 CRIMP GP",
                        "value": "SMA M RP LMR 100 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RP_LMR_100_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F PCB MOUNT GP",
                        "value": "SMA F PCB MOUNT GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_PCB_MOUNT_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RP LMR 200 CRIMP GP",
                        "value": "SMA M RP LMR 200 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RP_LMR_200_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Female RP Rightangle PCB Mount",
                        "value": "SMA Female RP Rightangle PCB Mount",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Female_RP_Rightangle_PCB_Mount.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M PCB MOUNT G P",
                        "value": "SMA M PCB MOUNT G P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_PCB_MOUNT_G_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M LMR 200 CRIMP N P",
                        "value": "SMA M LMR 200 CRIMP N P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_LMR_200_CRIMP_N_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F RG 86 CRIMP GP",
                        "value": "SMA F RG 86 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_RG_86_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M SUCO 85 G P",
                        "value": "SMA M SUCO 85 G P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_SUCO_85_G_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RG 141 SUCO G P",
                        "value": "SMA M RG 141 SUCO G P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RG_141_SUCO_G_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA RG 59 CRIMP GP",
                        "value": "SMA M RA RG 59 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_RG_59_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA for RG 58 Cable",
                        "value": "SMA M RA for RG 58 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_for_RG_58_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Female Rightangle PCB Mount",
                        "value": "SMA Female Rightangle PCB Mount",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Female_Rightangle_PCB_Mount.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Female Straight Edge Mount Connector For P.C.B",
                        "value": "SMA Female Straight Edge Mount Connector For P.C.B",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Female_Straight_Edge_Mount_Connector_For_P.C.B.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA LMR 100 CRIMP GP",
                        "value": "SMA M RA LMR 100 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_LMR_100_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA LMR 400 CLAMP",
                        "value": "SMA M RA LMR 400 CLAMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_LMR_400_CLAMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Male Crimp Connector For LMR200 Cable",
                        "value": "SMA Male Crimp Connector For LMR200 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Male_Crimp_Connector_For_LMR200_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA RP LMR 200 CRIMP GP",
                        "value": "SMA M RA RP LMR 200 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_RP_LMR_200_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F 4 Hole",
                        "value": "SMA F 4 Hole",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_4_Hole.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F for RG58 Cable",
                        "value": "SMA F for RG58 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_for_RG58_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M LMR 400 CRIMP GP",
                        "value": "SMA M LMR 400 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_LMR_400_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Male Right Angle Clamp Connector For LMR300 Cable",
                        "value": "SMA Male Right Angle Clamp Connector For LMR300 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Male_Right_Angle_Clamp_Connector_For_LMR300_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F RA LMR 100 CRIMP GP",
                        "value": "SMA F RA LMR 100 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_RA_LMR_100_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M LMR 100 CRIMP",
                        "value": "SMA M LMR 100 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_LMR_100_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F 2 Hole",
                        "value": "SMA F 2 Hole",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_2_Hole.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Female Rightangle BH PCB Mount",
                        "value": "SMA Female Rightangle BH PCB Mount",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Female_Rightangle_BH_PCB_Mount.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M R A LMR 200 CRIMP",
                        "value": "SMA M R A LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_R_A_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M R A PCB MOUNT G P",
                        "value": "SMA M R A PCB MOUNT G P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_R_A_PCB_MOUNT_G_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F 4 HOLE RG 141 GP SUCO",
                        "value": "SMA F 4 HOLE RG 141 GP SUCO",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_4_HOLE_RG_141_GP_SUCO.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA RG 86 SUCO GP",
                        "value": "SMA M RA RG 86 SUCO GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_M_RA_RG_86_SUCO_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F RA LMR 200 CRIMP GP",
                        "value": "SMA F RA LMR 200 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_F_RA_LMR_200_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA Male Connector For RG405 086In Cable",
                        "value": "SMA Male Connector For RG405 086In Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMA/SMA_Male_Connector_For_RG405_086In_Cable.PDF",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SMB ----

            "connector_smb": {

                "question": "Which SMB connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMB F BT 3002 CRIMP GP",
                        "value": "SMB F BT 3002 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMB/SMB_F_BT_3002_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMB F RA BT 3002 CRIMP GP",
                        "value": "SMB F RA BT 3002 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMB/SMB_F_RA_BT_3002_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMB M RA BT CRIMP",
                        "value": "SMB M RA BT CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMB/SMB_M_RA_BT_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMB Female RA for BT 3002 Crimp",
                        "value": "SMB Female RA for BT 3002 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMB/SMB_Female_RA_for_BT_3002_Crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMB Double Male to Female T Shape Adaptor",
                        "value": "SMB Double Male to Female T Shape Adaptor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMB/SMB_Double_Male_to_Female_T_Shape_Adaptor.PDF",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SMC ----

            "connector_smc": {

                "question": "Which SMC connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMC F LMR 100 CRIMP GP",
                        "value": "SMC F LMR 100 CRIMP GP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMC/SMC_F_LMR_100_CRIMP_GP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMC F RA LMR 100 Crimp",
                        "value": "SMC F RA LMR 100 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMC/SMC_F_RA_LMR_100_Crimp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMC F RA LMR 200 Crimp",
                        "value": "SMC F RA LMR 200 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMC/SMC_F_RA_LMR_200_Crimp.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SMP ----

            "connector_smp": {

                "question": "Which SMP connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMA (F) Sq. Flange Receptical With Cylindrical",
                        "value": "SMA (F) Sq. Flange Receptical With Cylindrical",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/smp/SMA_(F)_Sq._Flange_Receptical_With_Cylindrical.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMP screw on male receptacle",
                        "value": "SMP screw on male receptacle",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/smp/SMP_screw_on_male_receptacle.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMP (M) Sq. Flange With Receptical Catchers",
                        "value": "SMP (M) Sq. Flange With Receptical Catchers",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/smp/SMP_(M)_Sq._Flange_With_Receptical_Catchers.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMP (M) in thred in receptacle",
                        "value": "SMP (M) in thred in receptacle",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/smp/SMP_(M)_in_thred_in_receptacle.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SMZ ----

            "connector_smz": {

                "question": "Which SMZ connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMZ BT43 Female Crimp Connector For RG179 Cable",
                        "value": "SMZ BT43 Female Crimp Connector For RG179 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SMZ/SMZ_BT43_Female_Crimp_Connector_For_RG179_Cable.PDF",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SSMA ----

            "connector_ssma": {

                "question": "Which SSMA connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SSMA M RG 316 Crimp",
                        "value": "SSMA M RG 316 Crimp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SSMA/SSMA_M_RG_316_Crimp.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- SSMB ----

            "connector_ssmb": {

                "question": "Which SSMB connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SSMB F LMR 100 CRIMP",
                        "value": "SSMB F LMR 100 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/SSMB/SSMB_F_LMR_100_CRIMP.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- TNC ----

            "connector_tnc": {

                "question": "Which TNC connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "TNC F FN BH LMR 100 REDUCING",
                        "value": "TNC F FN BH LMR 100 REDUCING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_F_FN_BH_LMR_100_REDUCING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male for RG 58 Cable",
                        "value": "TNC Male for RG 58 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_for_RG_58_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC F RG 59 CRIMP",
                        "value": "TNC F RG 59 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_F_RG_59_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC M LMR 240 CRIMP",
                        "value": "TNC M LMR 240 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_M_LMR_240_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC F 4 HOLE",
                        "value": "TNC F 4 HOLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_F_4_HOLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male for LMR 240 Clamp",
                        "value": "TNC Male for LMR 240 Clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_for_LMR_240_Clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC M LMR 300 CRIMP",
                        "value": "TNC M LMR 300 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_M_LMR_300_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male Clamp Connector For LMR400 Cable",
                        "value": "TNC Male Clamp Connector For LMR400 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_Clamp_Connector_For_LMR400_Cable.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male For 1 2 Feeder Cable",
                        "value": "TNC Male For 1 2 Feeder Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_For_1_2_Feeder_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC M 1 2 SF",
                        "value": "TNC M 1 2 SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_M_1_2_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male for LMR-400 Cable Clamp",
                        "value": "TNC Male for LMR-400 Cable Clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_for_LMR-400_Cable_Clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC M Right Angle Connector For Rg 402 141 Cable",
                        "value": "TNC M Right Angle Connector For Rg 402 141 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_M_Right_Angle_Connector_For_Rg_402_141_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC MALE RG223",
                        "value": "TNC MALE RG223",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_MALE_RG223.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male St Clamp for LMR 400 Cable",
                        "value": "TNC Male St Clamp for LMR 400 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_St_Clamp_for_LMR_400_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC M ST CLAMP FOR RG 300",
                        "value": "TNC M ST CLAMP FOR RG 300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_M_ST_CLAMP_FOR_RG_300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC Male for RG58 Cable",
                        "value": "TNC Male for RG58 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/TNC/TNC_Male_for_RG58_Cable.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- TQ ----

            "connector_tq": {

                "question": "Please describe the exact TQ connector you need (gender, angle, cable type, mount) so we can quote it precisely.",

                "key": "product_variant",

                "type": "text",

                "next": "quantity"

            },

            # ---- Triaxial ----

            "connector_triaxial": {

                "question": "Which Triaxial connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "BNC Triax Straight Male Plug 2 Lug Clamp",
                        "value": "BNC Triax Straight Male Plug 2 Lug Clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/triaxial_connector/BNC_Triax_Straight_Male_Plug_2_Lug_Clamp.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # ---- UHF ----

            "connector_uhf": {

                "question": "Which UHF connector variant would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "UHF F 4 HOLE",
                        "value": "UHF F 4 HOLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/UHF/UHF_F_4_HOLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "UHF M LMR 200 CRIMP",
                        "value": "UHF M LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/UHF/UHF_M_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MINI UHF M LMR 200 CRIMP",
                        "value": "MINI UHF M LMR 200 CRIMP",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/UHF/MINI_UHF_M_LMR_200_CRIMP.pdf",
                        "next": "quantity"
                    }

                ]

            },
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
            # Masts
            # -------------------------------------------------

            "masts": {

                "question": "Which type of Mast?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Locking Telescopic Mast",
                        "value": "Locking Telescopic Mast",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Pneumatic Telescopic Mast",
                        "value": "Pneumatic Telescopic Mast",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "CCTV Mast",
                        "value": "CCTV Mast",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Lighting Mast / Tower",
                        "value": "Lighting Mast / Tower",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Mobile Trailer Mast Tower System",
                        "value": "Mobile Trailer Mast Tower System",
                        "price": None,
                        "next": "quantity"
                    },

                    {
                        "text": "Mast Accessories (Tripods, Compressors, Jacks, etc.)",
                        "value": "Mast Accessories",
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
    "Masts": "https://www.rfconnector.in/product_showroom/telescopic_mast",

    # TODO: verify these against the live site structure
    "Microwave Components": "https://synergytpl.com/microwave-components",
    "Waveguides": "https://synergytpl.com/waveguides",
    "Filters": "https://synergytpl.com/filters",
    "Installation Tools & Kits": "https://synergytpl.com/installation-tools",
    "Test & Measurement": "https://synergytpl.com/test-measurement",

    "_default": "https://www.rfconnector.in/product_showroom"
}

# ==================================================
# Connector-type -> specific showroom page URL
#
# Overrides CATEGORY_URLS's generic RF Connectors link with the exact
# connector-type page once the customer has picked a specific type
# (e.g. SMA -> /product_showroom/sma_connector instead of the generic
# RF Connectors landing page). Falls back to CATEGORY_URLS["RF Connectors"]
# for any type not in this dict.
# ==================================================

CONNECTOR_TYPE_URLS = {"BNC": "https://rfconnector.in/product_showroom/bnc_connector", "CRC9": "https://rfconnector.in/product_showroom/crc9_connector", "DIN / 4.3-1.0": "https://rfconnector.in/product_showroom/din_connector", "MCX": "https://rfconnector.in/product_showroom/mcx_connector", "MMCX": "https://rfconnector.in/product_showroom/mmcx_connector", "N-Type": "https://rfconnector.in/product_showroom/n_type_connector", "QMA": "https://rfconnector.in/product_showroom/qma_connector", "SAA": "https://rfconnector.in/product_showroom/saa_connector", "SMA": "https://rfconnector.in/product_showroom/sma_connector", "SMB": "https://rfconnector.in/product_showroom/smb_connector", "SMC": "https://rfconnector.in/product_showroom/smc_connector", "SMZ": "https://rfconnector.in/product_showroom/smz_connector", "SSMB": "https://rfconnector.in/product_showroom/ssmb_connector", "TNC": "https://rfconnector.in/product_showroom/tnc_connector", "UHF": "https://rfconnector.in/product_showroom/uhf_connector", "SMP": "https://rfconnector.in/product_showroom/smp_connector", "F Type": "https://rfconnector.in/product_showroom/f_type_connector", "Circular Connector": "https://rfconnector.in/product_showroom/circular_connector", "1.85mm": "https://rfconnector.in/product_showroom/185mm_connector", "2.4mm": "https://rfconnector.in/product_showroom/24mm_connector", "2.92mm": "https://rfconnector.in/product_showroom/292mm_connectors", "3.5mm": "https://rfconnector.in/product_showroom/35mm_connector"}
