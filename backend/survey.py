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

            # -------------------------------------------------
            # Which type of Cable Assembly?
            # -------------------------------------------------

            "cable_assemblies": {

                "question": "Which type of Cable Assembly?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Coaxial Cables",
                        "value": "Coaxial Cables",
                        "next": "cable_assemblies_coaxial_cables"
                    },

                    {
                        "text": "New Cable",
                        "value": "New Cable",
                        "next": "cable_assemblies_new_cable"
                    },

                    {
                        "text": "Other Cable Assemblies Items",
                        "value": "Other Cable Assemblies Items",
                        "next": "cable_assemblies_other_items"
                    },

                    {
                        "text": "Signal Cable",
                        "value": "Signal Cable",
                        "next": "cable_assemblies_signal_cable"
                    },

                    {
                        "text": "Technical Sheet",
                        "value": "Technical Sheet",
                        "next": "cable_assemblies_technical_sheet"
                    }

                ]

            },

            "cable_assemblies_coaxial_cables": {

                "question": "Which Coaxial Cables product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "hsfx 50 1",
                        "value": "hsfx 50 1",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsfx_50_1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 190",
                        "value": "hfwp 190",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_190.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfbp 142",
                        "value": "hfbp 142",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfbp_142.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfxp 120",
                        "value": "hfxp 120",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfxp_120.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfbx 142",
                        "value": "hfbx 142",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfbx_142.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hsft 50 5.2",
                        "value": "hsft 50 5.2",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsft_50_5.2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "h sfcj 50 7",
                        "value": "h sfcj 50 7",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/h_sfcj_50_7.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Semi Rigid SR 085 Cable",
                        "value": "Semi Rigid SR 085 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/Semi_Rigid_Cable/Semi_Rigid_SR_085_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfbx 304",
                        "value": "hfbx 304",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfbx_304.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 311",
                        "value": "hfwp 311",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_311.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "h sfcj 50 3",
                        "value": "h sfcj 50 3",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/h_sfcj_50_3.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 142",
                        "value": "hfwp 142",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_142.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfx 086",
                        "value": "hfx 086",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfx_086.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfbp 205",
                        "value": "hfbp 205",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfbp_205.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 178 Cable",
                        "value": "RG 178 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_178_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SUCO FORM 141 CU",
                        "value": "SUCO FORM 141 CU",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/SUCO_FORM/SUCO_FORM_141_CU.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "hfxp 047",
                        "value": "hfxp 047",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfxp_047.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hybx 400",
                        "value": "hybx 400",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hybx_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 316 DS Cable",
                        "value": "RG 316 DS Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_316_DS_Cable_.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 214 Cable",
                        "value": "RG 214 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_214_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 190D",
                        "value": "hfwp 190D",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_190D.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hsfx 50 5.3",
                        "value": "hsfx 50 5.3",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsfx_50_5.3.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 2 LDF CABLE",
                        "value": "1 2 LDF CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/Feeder_Cable/1_2_LDF_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Datasheet PCM CABLE",
                        "value": "Datasheet PCM CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/PCM_Cables/Datasheet_PCM_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 58 Coaxial Cable1",
                        "value": "RG 58 Coaxial Cable1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_58_Coaxial_Cable1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 4 LDF Cable",
                        "value": "1 4 LDF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/Feeder_Cable/1_4_LDF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfbx 316",
                        "value": "hfbx 316",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfbx_316.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 90",
                        "value": "hfwp 90",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_90.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hybx 240",
                        "value": "hybx 240",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hybx_240.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hsft 50 1",
                        "value": "hsft 50 1",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsft_50_1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 205",
                        "value": "hfwp 205",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_205.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "h sfcj 50 5",
                        "value": "h sfcj 50 5",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/h_sfcj_50_5.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Semi Rigid SR-250 Cable",
                        "value": "Semi Rigid SR-250 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/Semi_Rigid_Cable/Semi_Rigid_SR-250_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hybx 300",
                        "value": "hybx 300",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hybx_300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfbp 304",
                        "value": "hfbp 304",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfbp_304.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5D 8D FB Cable",
                        "value": "5D 8D FB Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/5D_8D_FB_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 217 Cable.",
                        "value": "RG 217 Cable.",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_217_Cable..pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfx 141",
                        "value": "hfx 141",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfx_141.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "12 PAIR PCM CABLE",
                        "value": "12 PAIR PCM CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/PCM_Cables/12_PAIR_PCM_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfwp 142D",
                        "value": "hfwp 142D",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfwp_142D.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "h sfcj 50 9",
                        "value": "h sfcj 50 9",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/h_sfcj_50_9.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 59 Coaxial Cable",
                        "value": "RG 59 Coaxial Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_59_Coaxial_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfxp 150",
                        "value": "hfxp 150",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfxp_150.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hsft 50 2",
                        "value": "hsft 50 2",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsft_50_2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hsft 50 3",
                        "value": "hsft 50 3",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsft_50_3.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 142 Cable",
                        "value": "RG 142 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_142_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hfxp 216",
                        "value": "hfxp 216",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hfxp_216.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "hsfx 50 3",
                        "value": "hsfx 50 3",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/high_frequency_cable/hsfx_50_3.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 179 Cable",
                        "value": "RG 179 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/RG_Cable/RG_179_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SUCO FORM 86",
                        "value": "SUCO FORM 86",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cables/Coaxial_Cables/High_Freq_Cables/SUCO_FORM_86.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SUCO FLEX 300",
                        "value": "SUCO FLEX 300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/Coaxial_Cables/High_Freq_Cables/SUCO_FLEX_300.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "cable_assemblies_new_cable": {

                "question": "Which New Cable product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Leaky Cables 7 8",
                        "value": "Leaky Cables 7 8",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/Leaky_Cables_7_8.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 217 Cable.",
                        "value": "RG 217 Cable.",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_217_Cable..pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 8 LDF Cable1",
                        "value": "7 8 LDF Cable1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/7_8_LDF_Cable1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SR047 M17",
                        "value": "SR047 M17",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SR047_M17.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 405 COAXIAL CABLE",
                        "value": "RG 405 COAXIAL CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_405_COAXIAL_CABLE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 240",
                        "value": "HLF 240",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_240.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SR034.95",
                        "value": "SR034.95",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SR034.95.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 400 UF Cable",
                        "value": "HLF 400 UF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_400_UF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CAT 6 LAN CABLE",
                        "value": "CAT 6 LAN CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/CAT_6_LAN_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 59 Coaxial Cable",
                        "value": "RG 59 Coaxial Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_59_Coaxial_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CAT 5 LAN CABLE",
                        "value": "CAT 5 LAN CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/CAT_5_LAN_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Semi Rigid SR 141 Cable",
                        "value": "Semi Rigid SR 141 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/Semi_Rigid_SR_141_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "137MM Cable",
                        "value": "137MM Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/137MM_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 2 LDF CABLE",
                        "value": "1 2 LDF CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/1_2_LDF_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 400 Cable",
                        "value": "RG 400 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_400_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 8 feeder aluminium cable1",
                        "value": "7 8 feeder aluminium cable1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/7_8_feeder_aluminium_cable1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG-6 HDC",
                        "value": "RG-6 HDC",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG-6_HDC.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG223 Cable",
                        "value": "RG223 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG223_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 174 Cable",
                        "value": "RG 174 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_174_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BT3002 Cable1",
                        "value": "BT3002 Cable1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/BT3002_Cable1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SUCO FORM 86",
                        "value": "SUCO FORM 86",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SUCO_FORM_86.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "14 AWG 2 CORE AUDIO SPEAKER CABLE",
                        "value": "14 AWG 2 CORE AUDIO SPEAKER CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/14_AWG_2_CORE_AUDIO_SPEAKER_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SM 250",
                        "value": "SM 250",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SM_250.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 142 CABLE",
                        "value": "RG 142 CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_142_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 214 Cable",
                        "value": "RG 214 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_214_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 8 super flex cable1",
                        "value": "7 8 super flex cable1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/7_8_super_flex_cable1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SR047 M17 70",
                        "value": "SR047 M17 70",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SR047_M17_70.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 300",
                        "value": "HLF 300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 1 4 Flex cable",
                        "value": "1 1 4 Flex cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/1_1_4_Flex_cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "113MM Cable",
                        "value": "113MM Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/113MM_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 500 Cable",
                        "value": "HLF 500 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_500_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SUCO FORM 141 CU",
                        "value": "SUCO FORM 141 CU",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SUCO_FORM_141_CU.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 188 Cable backup",
                        "value": "RG 188 Cable backup",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_188_Cable%20backup.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 5 8SF cable",
                        "value": "1 5 8SF cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/1_5_8SF_cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 316 Cable",
                        "value": "RG 316 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_316_Cable_.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 8 Aluminium Flexible Cable Plane",
                        "value": "7 8 Aluminium Flexible Cable Plane",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/7_8_Aluminium_Flexible_Cable_Plane.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Semi Flexible SF 141 Cable",
                        "value": "Semi Flexible SF 141 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/Semi_Flexible_SF_141_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG8 Cable",
                        "value": "RG8 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG8_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "18 Pair Alarm Cable",
                        "value": "18 Pair Alarm Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/18_Pair_Alarm_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 100",
                        "value": "HLF 100",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_100.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 200",
                        "value": "HLF 200",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_200.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 58 Coaxial Cable1",
                        "value": "RG 58 Coaxial Cable1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_58_Coaxial_Cable1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Datasheet PCM CABLE (1)",
                        "value": "Datasheet PCM CABLE (1)",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/Datasheet_PCM_CABLE%20(1).pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 400",
                        "value": "HLF 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 600 Cable",
                        "value": "HLF 600 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_600_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 900",
                        "value": "HLF 900",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_900.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SUCO FLEX 300",
                        "value": "SUCO FLEX 300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SUCO_FLEX_300.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 141 RG 402 COAXIAL CABLE",
                        "value": "RG 141 RG 402 COAXIAL CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_141_RG_402_COAXIAL_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5D 8D FB Cable (1)",
                        "value": "5D 8D FB Cable (1)",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/5D_8D_FB_Cable%20(1).pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Leaky Cables 1 1 4",
                        "value": "Leaky Cables 1 1 4",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/Leaky_Cables_1_1_4.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SR086 M17",
                        "value": "SR086 M17",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SR086_M17.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 179 Cable",
                        "value": "RG 179 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_179_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 4 ldf cable (2)",
                        "value": "1 4 ldf cable (2)",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/1_4_ldf_cable%20(2).pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 213 Cable",
                        "value": "RG 213 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_213_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 178 Cable",
                        "value": "RG 178 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/RG_178_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 195",
                        "value": "HLF 195",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/HLF_195.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SR034",
                        "value": "SR034",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/new_cable/SR034.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "cable_assemblies_other_items": {

                "question": "Which Other Cable Assemblies Items product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "RG223 Cable",
                        "value": "RG223 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cables/RG223_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA(M) to SMA(F) with Rg141 Cable",
                        "value": "SMA(M) to SMA(F) with Rg141 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/SMA(M)_to_SMA(F)_with_Rg141_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WC02 Flexible Cable Assembly",
                        "value": "WC02 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/WC02_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 1.13 CABLE",
                        "value": "RG 1.13 CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/RG_1.13_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 600 Cable",
                        "value": "HLF 600 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_600_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WC01 Flexible Cable Assembly",
                        "value": "WC01 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/WC01_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 195",
                        "value": "HLF 195",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_195.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SLB360 292M 292M 10M Cable",
                        "value": "SLB360 292M 292M 10M Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/SLB360_292M_292M_10M_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "18GHz WC04 Flexible Cable Assembly",
                        "value": "18GHz WC04 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/18GHz_WC04_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "40GHz WC17 Flexible Cable Assembly with Armor",
                        "value": "40GHz WC17 Flexible Cable Assembly with Armor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/40GHz_WC17_Flexible_Cable_Assembly_with_Armor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "JUMPER CABLE",
                        "value": "JUMPER CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/jumper_cable_testreport/JUMPER_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M to N M half inch",
                        "value": "N M to N M half inch",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Cable_Assembly/N_M_to_N_M_half_inch.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC-POWER CABLE",
                        "value": "DC-POWER CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Power_Cable/DC-POWER_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 240",
                        "value": "HLF 240",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_240.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG-11 CCS",
                        "value": "RG-11 CCS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/RG-11_CCS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "40GHz WC16 Flexible Cable Assembly with Armor",
                        "value": "40GHz WC16 Flexible Cable Assembly with Armor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/40GHz_WC16_Flexible_Cable_Assembly_with_Armor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 400 Flexible Cable Assembly",
                        "value": "RG 400 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/RG_400_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "26.5GHz WC13 Flexible Cable Assembly",
                        "value": "26.5GHz WC13 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/26.5GHz_WC13_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 8 LDF Cable",
                        "value": "7 8 LDF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/7_8_LDF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RG 400 Flexible Cable Assembly 12.4GHz",
                        "value": "RG 400 Flexible Cable Assembly 12.4GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/RG_400_Flexible_Cable_Assembly_12.4GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N(F) 4Hole to SMA(M) RA with Rg141 1meter",
                        "value": "N(F) 4Hole to SMA(M) RA with Rg141 1meter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/N(F)_4Hole_to_SMA(M)_RA_with_Rg141_1meter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "141 Multi-Flex Cable Assembly",
                        "value": "141 Multi-Flex Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/141_Multi-Flex_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "18GHz WC03 Flexible Cable Assembly",
                        "value": "18GHz WC03 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/18GHz_WC03_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "26.5GHz SB 142I Flexible Cable Assembly",
                        "value": "26.5GHz SB 142I Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/26.5GHz_SB_142I_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "40GHz WC21 Semi-rigid Cable Assembly",
                        "value": "40GHz WC21 Semi-rigid Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/40GHz_WC21_Semi-rigid_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BT3002 Cable",
                        "value": "BT3002 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/BT3002_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "141 Multi-Flex Cable Assembly 33GHz",
                        "value": "141 Multi-Flex Cable Assembly 33GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/141_Multi-Flex_Cable_Assembly_33GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 300",
                        "value": "HLF 300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 400",
                        "value": "HLF 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 4 SF Cable",
                        "value": "1 4 SF Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/1_4_SF_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 100",
                        "value": "HLF 100",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_100.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N(F)to N(F) with RG 141 1Mtr",
                        "value": "N(F)to N(F) with RG 141 1Mtr",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/N(F)to_N(F)_with_RG_141_1Mtr.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 8 Feeder Aluminium cable",
                        "value": "7 8 Feeder Aluminium cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/7_8_Feeder_Aluminium_cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "26.5GHz SS402 Flexible Cable Assembly",
                        "value": "26.5GHz SS402 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/26.5GHz_SS402_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1 2 SF CABLE",
                        "value": "1 2 SF CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/1_2_SF_CABLE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "AISG RET Control Cable Assemblies DIN Male to DIN Female",
                        "value": "AISG RET Control Cable Assemblies DIN Male to DIN Female",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembalies/AISG_RET_Control_Cable_Assemblies_DIN_Male_to_DIN_Female.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Jumper Cable",
                        "value": "Jumper Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/jumper_cable_testreport/Jumper_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "AISG RET CONTROL CABLE SPLITTER DIN MALE TO DIN FEMALE DIN MALE",
                        "value": "AISG RET CONTROL CABLE SPLITTER DIN MALE TO DIN FEMALE DIN MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembalies/AISG_RET_CONTROL_CABLE_SPLITTER_DIN_MALE_TO_DIN_FEMALE_DIN_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "AISG RET CONTROL CABLE AISG FEMALE TO DB9 MALE",
                        "value": "AISG RET CONTROL CABLE AISG FEMALE TO DB9 MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembalies/AISG_RET_CONTROL_CABLE_AISG_FEMALE_TO_DB9_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "78 Leaky Cable",
                        "value": "78 Leaky Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/78_Leaky_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 200",
                        "value": "HLF 200",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_200.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "26.5GHz WC12 Flexible Cable Assembly",
                        "value": "26.5GHz WC12 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/26.5GHz_WC12_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "40GHz WC20 Flexible Cable Assembly",
                        "value": "40GHz WC20 Flexible Cable Assembly",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/40GHz_WC20_Flexible_Cable_Assembly.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HLF 500 Cable",
                        "value": "HLF 500 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/HLF_500_Cable.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "cable_assemblies_signal_cable": {

                "question": "Which Signal Cable product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "signal cable",
                        "value": "signal cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Cable/signal_cable/signal_cable.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "cable_assemblies_technical_sheet": {

                "question": "Which Technical Sheet product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMA TO SMA SPACS",
                        "value": "SMA TO SMA SPACS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/Technical_Sheet/SMA_TO_SMA_SPACS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M TO TNC M RA SPACS",
                        "value": "SMA M TO TNC M RA SPACS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/Technical_Sheet/SMA_M_TO_TNC_M_RA_SPACS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M TO SMA M RA SPACS",
                        "value": "SMA M TO SMA M RA SPACS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/Technical_Sheet/SMA_M_TO_SMA_M_RA_SPACS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA TO SMA M RA SPACS",
                        "value": "SMA M RA TO SMA M RA SPACS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/Technical_Sheet/SMA_M_RA_TO_SMA_M_RA_SPACS.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Which Microwave Component?
            # -------------------------------------------------

            "microwave_components": {

                "question": "Which Microwave Component?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Attenuator",
                        "value": "Attenuator",
                        "next": "microwave_components_attenuator"
                    },

                    {
                        "text": "Balun",
                        "value": "Balun",
                        "next": "microwave_components_balun"
                    },

                    {
                        "text": "Bias T",
                        "value": "Bias T",
                        "next": "microwave_components_bias_t"
                    },

                    {
                        "text": "Combiner",
                        "value": "Combiner",
                        "next": "microwave_components_combiner"
                    },

                    {
                        "text": "Directional Coupler",
                        "value": "Directional Coupler",
                        "next": "microwave_components_directional_coupler"
                    },

                    {
                        "text": "DPDT",
                        "value": "DPDT",
                        "next": "microwave_components_dpdt"
                    },

                    {
                        "text": "Dummy Load",
                        "value": "Dummy Load",
                        "next": "microwave_components_dummy_load"
                    },

                    {
                        "text": "HIGH FREQ Adaptor",
                        "value": "HIGH FREQ Adaptor",
                        "next": "microwave_components_high_freq_adaptor"
                    },

                    {
                        "text": "HIGH FREQ Attanuator",
                        "value": "HIGH FREQ Attanuator",
                        "next": "microwave_components_high_freq_attanuator"
                    },

                    {
                        "text": "HIGH FREQ Connector",
                        "value": "HIGH FREQ Connector",
                        "next": "microwave_components_high_freq_connector"
                    },

                    {
                        "text": "Other Microwave Components Items",
                        "value": "Other Microwave Components Items",
                        "next": "microwave_components_other_items"
                    },

                    {
                        "text": "SP10T",
                        "value": "SP10T",
                        "next": "microwave_components_sp10t"
                    },

                    {
                        "text": "SP10T Terminated",
                        "value": "SP10T Terminated",
                        "next": "microwave_components_sp10t_terminated"
                    },

                    {
                        "text": "SP3T",
                        "value": "SP3T",
                        "next": "microwave_components_sp3t"
                    },

                    {
                        "text": "SP3T Terminated",
                        "value": "SP3T Terminated",
                        "next": "microwave_components_sp3t_terminated"
                    },

                    {
                        "text": "SP4T",
                        "value": "SP4T",
                        "next": "microwave_components_sp4t"
                    },

                    {
                        "text": "SP4T Terminated",
                        "value": "SP4T Terminated",
                        "next": "microwave_components_sp4t_terminated"
                    },

                    {
                        "text": "SP5T",
                        "value": "SP5T",
                        "next": "microwave_components_sp5t"
                    },

                    {
                        "text": "SP5T Terminated",
                        "value": "SP5T Terminated",
                        "next": "microwave_components_sp5t_terminated"
                    },

                    {
                        "text": "SP6T",
                        "value": "SP6T",
                        "next": "microwave_components_sp6t"
                    },

                    {
                        "text": "SP6T Terminated",
                        "value": "SP6T Terminated",
                        "next": "microwave_components_sp6t_terminated"
                    },

                    {
                        "text": "SP8T",
                        "value": "SP8T",
                        "next": "microwave_components_sp8t"
                    },

                    {
                        "text": "SP8T Terminated",
                        "value": "SP8T Terminated",
                        "next": "microwave_components_sp8t_terminated"
                    },

                    {
                        "text": "SP9T",
                        "value": "SP9T",
                        "next": "microwave_components_sp9t"
                    },

                    {
                        "text": "SP9T Terminated",
                        "value": "SP9T Terminated",
                        "next": "microwave_components_sp9t_terminated"
                    },

                    {
                        "text": "SPDT",
                        "value": "SPDT",
                        "next": "microwave_components_spdt"
                    },

                    {
                        "text": "SPDT Termineted",
                        "value": "SPDT Termineted",
                        "next": "microwave_components_spdt_termineted"
                    },

                    {
                        "text": "Splitters",
                        "value": "Splitters",
                        "next": "microwave_components_splitters"
                    },

                    {
                        "text": "SURG Arrester",
                        "value": "SURG Arrester",
                        "next": "microwave_components_surg_arrester"
                    }

                ]

            },

            "microwave_components_attenuator": {

                "question": "Which Attenuator product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "30db 2watt N Attenuator",
                        "value": "30db 2watt N Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/30db_2watt_N_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 30DB 20W N MF 3GHZ",
                        "value": "ATT 30DB 20W N MF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_30DB_20W_N_MF_3GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 30dB 3Ghz",
                        "value": "ATT 10W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0 90 dB 10 dB N M F Step Att",
                        "value": "0 90 dB 10 dB N M F Step Att",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/STEP_ATT/0_90_dB_10_dB_N_M_F_Step_Att.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "10db 2watt N Attenuator",
                        "value": "10db 2watt N Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/10db_2watt_N_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 15dB 3Ghz",
                        "value": "ATT 5W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 03dB 3Ghz",
                        "value": "ATT 50W 03dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_03dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 5dB 3Ghz",
                        "value": "ATT 5W 5dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_5dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 30dB 18Ghz",
                        "value": "ATT 2W 30dB 18Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/SMA_Attenuator/ATT_2W_30dB_18Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0 90 dB 1 dB N F F Step Att",
                        "value": "0 90 dB 1 dB N F F Step Att",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/STEP_ATT/0_90_dB_1_dB_N_F_F_Step_Att.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 10dB 3Ghz",
                        "value": "ATT 25W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "200W NMF DC18GHz Coaxial Attenuator",
                        "value": "200W NMF DC18GHz Coaxial Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/200W_NMF_DC18GHz_Coaxial_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 06dB 3Ghz",
                        "value": "ATT 200W 06dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_06dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 20dB 3Ghz",
                        "value": "ATT 10W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 3DB 20W N MF 3GHZ",
                        "value": "ATT 3DB 20W N MF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_3DB_20W_N_MF_3GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 10dB 6Ghz",
                        "value": "ATT 2W 10dB 6Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_10dB_6Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 10dB 18Ghz",
                        "value": "ATT 2W 10dB 18Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_10dB_18Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 5dB 3Ghz",
                        "value": "ATT 10W 5dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_5dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2db F M F F Attenuator",
                        "value": "2db F M F F Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/F_Attenuator/2db_F_M_F_F_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 40DB 20W N MF 3GHZ",
                        "value": "ATT 40DB 20W N MF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_40DB_20W_N_MF_3GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 15dB 3Ghz",
                        "value": "ATT 25W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 20dB 8GhzS",
                        "value": "ATT 2W 20dB 8GhzS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_20dB_8GhzS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 3dB 3Ghz",
                        "value": "ATT 10W 3dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_3dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 15dB 3Ghz",
                        "value": "ATT 2W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 15DB 20W N MF 3GHZ",
                        "value": "ATT 15DB 20W N MF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_15DB_20W_N_MF_3GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 20dB 3Ghz",
                        "value": "ATT 50W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 20dB 3GhzS",
                        "value": "ATT 2W 20dB 3GhzS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_20dB_3GhzS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 40dB 3Ghz",
                        "value": "ATT 25W 40dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_40dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 06dB 3Ghz",
                        "value": "ATT 50W 06dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_06dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 15dB 3Ghz",
                        "value": "ATT 10W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0 90 dB 1 dB N M F Step Att",
                        "value": "0 90 dB 1 dB N M F Step Att",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/STEP_ATT/0_90_dB_1_dB_N_M_F_Step_Att.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 30dB 3Ghz",
                        "value": "ATT 5W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 20dB 3Ghz",
                        "value": "ATT 25W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 03dB 3Ghz",
                        "value": "ATT 200W 03dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_03dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 6dB 3Ghz",
                        "value": "ATT 10W 6dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_6dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 10dB 3Ghz",
                        "value": "ATT 10W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_10W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1db F M F F Attenuator",
                        "value": "1db F M F F Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/F_Attenuator/1db_F_M_F_F_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5db F M F F Attenuator",
                        "value": "5db F M F F Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/F_Attenuator/5db_F_M_F_F_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 15dB 3Ghz",
                        "value": "ATT 50W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 40dB 3Ghz",
                        "value": "ATT 200W 40dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_40dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 20dB 18Ghz",
                        "value": "ATT 2W 20dB 18Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_20dB_18Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0 90 dB 10 dB N F F Step Att",
                        "value": "0 90 dB 10 dB N F F Step Att",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/STEP_ATT/0_90_dB_10_dB_N_F_F_Step_Att.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 20dB 3Ghz",
                        "value": "ATT 1W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_1W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 20dB 3Ghz",
                        "value": "ATT 200W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 30dB 3Ghz",
                        "value": "ATT 50W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 10dB 3Ghz",
                        "value": "ATT 200W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 10dB 3Ghz",
                        "value": "ATT 50W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 5dB 3Ghz",
                        "value": "ATT 100W 5dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_5dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 15dB 3Ghz",
                        "value": "ATT 100W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 1dB 3Ghz",
                        "value": "ATT 1W 1dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/SMA_Attenuator/ATT_1W_1dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 20DB 20W N MF 3GHZ",
                        "value": "ATT 20DB 20W N MF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_20DB_20W_N_MF_3GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0 30 dB 1 dB N F F Step Att",
                        "value": "0 30 dB 1 dB N F F Step Att",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/STEP_ATT/0_30_dB_1_dB_N_F_F_Step_Att.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 3dB 3Ghz",
                        "value": "ATT 2W 3dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_3dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 15dB 3Ghz",
                        "value": "ATT 200W 15dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_15dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 40dB 3Ghz",
                        "value": "ATT 100W 40dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_40dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 3dB 3GhzS",
                        "value": "ATT 1W 3dB 3GhzS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/SMA_Attenuator/ATT_1W_3dB_3GhzS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 6dB 3Ghz",
                        "value": "ATT 5W 6dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_6dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 6dB 3Ghz",
                        "value": "ATT 2W 6dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_6dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 10dB 3Ghz",
                        "value": "ATT 100W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 02dB 03Ghz",
                        "value": "ATT 1W 02dB 03Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/SMA_Attenuator/ATT_1W_02dB_03Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "20db 2watt N Attenuator",
                        "value": "20db 2watt N Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/20db_2watt_N_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 20dB 3Ghz",
                        "value": "ATT 2W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 6dB 18GhzS",
                        "value": "ATT 1W 6dB 18GhzS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_1W_6dB_18GhzS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 50W 40dB 3Ghz",
                        "value": "ATT 50W 40dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_50W_40dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 30DB 30W N MF 3GHZ",
                        "value": "ATT 30DB 30W N MF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_30DB_30W_N_MF_3GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0 99 dB 1dB N F F step attanuator",
                        "value": "0 99 dB 1dB N F F step attanuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/STEP_ATT/0_99_dB_1dB_N_F_F_step%20attanuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 20dB 6Ghz",
                        "value": "ATT 2W 20dB 6Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_20dB_6Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 30dB 3Ghz",
                        "value": "ATT 100W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 5dB 3Ghz",
                        "value": "ATT 2W 5dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_5dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 3dB 3Ghz",
                        "value": "ATT 100W 3dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_3dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 30dB 3Ghz",
                        "value": "ATT 200W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 3dB 3Ghz",
                        "value": "ATT 5W 3dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_3dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 200W 05dB 3Ghz",
                        "value": "ATT 200W 05dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_200W_05dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 06dB 3Ghz",
                        "value": "ATT 25W 06dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_06dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 6DB 20W NF 3GHZ",
                        "value": "ATT 6DB 20W NF 3GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/2watt_n_attenuator/ATT_6DB_20W_%20NF%203GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 20dB 3Ghz",
                        "value": "ATT 5W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 10dB 3Ghz",
                        "value": "ATT 2W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5W 10dB 3Ghz",
                        "value": "ATT 5W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_5W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 30dB 6Ghz",
                        "value": "ATT 2W 30dB 6Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_2W_30dB_6Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "10db F M F F Attenuator",
                        "value": "10db F M F F Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/F_Attenuator/10db_F_M_F_F_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2W 30dB 3Ghz",
                        "value": "ATT 2W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/SMA_Attenuator/ATT_2W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "15db F M F F Attenuator",
                        "value": "15db F M F F Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/F_Attenuator/15db_F_M_F_F_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 30dB 3Ghz",
                        "value": "ATT 25W 30dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_30dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 06dB 3Ghz",
                        "value": "ATT 100W 06dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_06dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "300W NMF DC6GHz Coaxial Attenuator",
                        "value": "300W NMF DC6GHz Coaxial Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/300W_NMF_DC6GHz_Coaxial_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "200W NMF DC6GHz Coaxial Attenuator",
                        "value": "200W NMF DC6GHz Coaxial Attenuator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/200W_NMF_DC6GHz_Coaxial_Attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 25W 03dB 3Ghz",
                        "value": "ATT 25W 03dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_25W_03dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 100W 20dB 3Ghz",
                        "value": "ATT 100W 20dB 3Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Attenuator/N_ATTANUTER/ATT_100W_20dB_3Ghz.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_balun": {

                "question": "Which Balun product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "BNC M TO KRONE BALUN",
                        "value": "BNC M TO KRONE BALUN",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/BNC_M_TO_KRONE_BALUN.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "24port Impedance Converter 1 loop E1",
                        "value": "24port Impedance Converter 1 loop E1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/24port_Impedance_Converter_1_loop_E1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "L9 Female to IDC balun",
                        "value": "L9 Female to IDC balun",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/L9_Female_to_IDC_balun.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC WIRE WRAP converter",
                        "value": "BNC WIRE WRAP converter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/BNC_WIRE_WRAP_converter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2SMZ F TO RJ45 BALUN DF with SMZ",
                        "value": "2SMZ F TO RJ45 BALUN DF with SMZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/2SMZ_F_TO_RJ45_BALUN_DF_with_SMZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Double L9 Male to RJ45 Balun Box 25mm",
                        "value": "Double L9 Male to RJ45 Balun Box 25mm",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/Double_L9_Male_to_RJ45_Balun_Box_25mm.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Balun1",
                        "value": "Balun1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/Balun1.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "100 pair 110 rack mounted patch panel",
                        "value": "100 pair 110 rack mounted patch panel",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/100_pair_110_rack_mounted_patch_panel.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC M 50 TO BNC F 75 OHM",
                        "value": "BNC M 50 TO BNC F 75 OHM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/BNC_M_50_TO_BNC_F_75_OHM.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "Balun2",
                        "value": "Balun2",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/Balun2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMZ M SNAP BALUN 11P 75 120ohm",
                        "value": "SMZ M SNAP BALUN 11P 75 120ohm",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/SMZ_M_SNAP_BALUN_11P_75_120ohm.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "l9 ww balun B2681",
                        "value": "l9 ww balun B2681",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/l9_ww_balun_B2681.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "75ohm 120ohm impedance converter 16 E1 balun panel 19 rack",
                        "value": "75ohm 120ohm impedance converter 16 E1 balun panel 19 rack",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/75ohm_120ohm_impedance_converter_16_E1_balun_panel_19_rack.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "16 e1 bnc female patch panel",
                        "value": "16 e1 bnc female patch panel",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Balun/other_balun/16_e1_bnc_female_patch_panel.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_bias_t": {

                "question": "Which Bias T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "DIN F DIN M 2G BIAS T",
                        "value": "DIN F DIN M 2G BIAS T",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Bias_T/DIN_F_DIN_M_2G_BIAS_T.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_combiner": {

                "question": "Which Combiner product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "3-1 COMBINER 800-2500MHz",
                        "value": "3-1 COMBINER 800-2500MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/combiner/3-1_COMBINER_800-2500MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Triple Band Combiner",
                        "value": "Triple Band Combiner",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/combiner/Triple_Band_Combiner.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2-1 Combiner 800-2500MHz",
                        "value": "2-1 Combiner 800-2500MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/combiner/2-1_Combiner_800-2500MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Hybrid Combiner",
                        "value": "Hybrid Combiner",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/combiner/Hybrid_Combiner.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_directional_coupler": {

                "question": "Which Directional Coupler product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "10dB Cavity Coupler",
                        "value": "10dB Cavity Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/10dB_Cavity_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "20dB Cavity Coupler",
                        "value": "20dB Cavity Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/20dB_Cavity_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "6db cavity directional coupler",
                        "value": "6db cavity directional coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/6db_cavity_directional_coupler.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "3db cavity directional coupler",
                        "value": "3db cavity directional coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/3db_cavity_directional_coupler.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "30dB Cavity",
                        "value": "30dB Cavity",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/30dB_Cavity.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5dB Cavity Coupler",
                        "value": "5dB Cavity Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/5dB_Cavity_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "15dB Cavity Coupler",
                        "value": "15dB Cavity Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/15dB_Cavity_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7dB Cavity Coupler",
                        "value": "7dB Cavity Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/7dB_Cavity_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5G Coupler",
                        "value": "5G Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/5G_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "40dB Cavity Coupler",
                        "value": "40dB Cavity Coupler",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/updated_coupler/40dB_Cavity_Coupler.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3Db to 20Db Directional Couplers",
                        "value": "3Db to 20Db Directional Couplers",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Directional_Coupler/3Db_to_20Db_Directional_Couplers.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_dpdt": {

                "question": "Which DPDT product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "DPDT L2 N F 12.4G LATCHING",
                        "value": "DPDT L2 N F 12.4G LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/DPDT/DPDT_L2_N_F_12.4G_LATCHING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DPDT TRANSFER L1 SMA F 26.5G LATCHING",
                        "value": "DPDT TRANSFER L1 SMA F 26.5G LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/DPDT/DPDT_TRANSFER_L1_SMA_F_26.5G_LATCHING.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_dummy_load": {

                "question": "Which Dummy Load product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N Male 30W 3GHz Dummy Load",
                        "value": "N Male 30W 3GHz Dummy Load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/N_Male_30W_3GHz_Dummy_Load.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "18 GHZ 5W",
                        "value": "18 GHZ 5W",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/18_GHZ_5W.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "5W DL 18G",
                        "value": "5W DL 18G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/5W_DL_18G.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male 10W Dummy Load",
                        "value": "N Male 10W Dummy Load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/N_Male_10W_Dummy_Load.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male 2W Dummy Load",
                        "value": "N Male 2W Dummy Load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/N_Male_2W_Dummy_Load.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N Male 50W Dummy Load",
                        "value": "N Male 50W Dummy Load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/N_Male_50W_Dummy_Load.PDF",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_high_freq_adaptor": {

                "question": "Which HIGH FREQ Adaptor product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMA F to N M Adaptor",
                        "value": "SMA F to N M Adaptor",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ADAPTOR/SMA_F_to_N_M_Adaptor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F to N F Adaptor",
                        "value": "N F to N F Adaptor",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ADAPTOR/N_F_to_N_F_Adaptor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F to SMA F ADAPTOR",
                        "value": "SMA F to SMA F ADAPTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ADAPTOR/SMA_F_to_SMA_F_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M to SMA M adaptor",
                        "value": "SMA M to SMA M adaptor",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ADAPTOR/SMA_M_to_SMA_M_adaptor.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_high_freq_attanuator": {

                "question": "Which HIGH FREQ Attanuator product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2 watt 18 ghz attenuator",
                        "value": "2 watt 18 ghz attenuator",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ATTANUATOR/2_watt_18_ghz_attenuator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1to30DB 2W SMA ATTANUATOR",
                        "value": "1to30DB 2W SMA ATTANUATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ATTANUATOR/1to30DB_2W_SMA_ATTANUATOR.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "5W 18GHZ ATT NMF",
                        "value": "5W 18GHZ ATT NMF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ATTANUATOR/New_High_Freq_Att/5W_18GHZ_ATT_NMF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "100W 18GHZ ATT NMF",
                        "value": "100W 18GHZ ATT NMF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ATTANUATOR/New_High_Freq_Att/100W_18GHZ_ATT_NMF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "25W 26.5GHZ ATT SMAF",
                        "value": "25W 26.5GHZ ATT SMAF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_ATTANUATOR/New_High_Freq_Att/25W_26.5GHZ_ATT_SMAF.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_high_freq_connector": {

                "question": "Which HIGH FREQ Connector product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N M SM 250",
                        "value": "N M SM 250",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/N_M_SM_250.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M RA for RG 405 86",
                        "value": "SMA M RA for RG 405 86",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/SMA_M_RA_for_RG_405_86.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1.85MM F CPS RG141",
                        "value": "1.85MM F CPS RG141",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/1.85MM_F_CPS_RG141.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA F 4 hole 15mm teflon",
                        "value": "SMA F 4 hole 15mm teflon",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/SMA_F_4_hole_15mm_teflon.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F 4 hole Solder",
                        "value": "N F 4 hole Solder",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/N_F_4_hole_Solder.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92mm Connectors",
                        "value": "2.92mm Connectors",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/2.92mm_Connectors.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA 4 HOLE CONNECTOR1",
                        "value": "SMA 4 HOLE CONNECTOR1",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/h_f_connnector/SMA_4_HOLE_CONNECTOR1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA 4 HOLE CONNECTOR2",
                        "value": "SMA 4 HOLE CONNECTOR2",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/h_f_connnector/SMA_4_HOLE_CONNECTOR2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA 2 HOLE CONNECTOR",
                        "value": "SMA 2 HOLE CONNECTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/h_f_connnector/SMA_2_HOLE_CONNECTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA 4 HOLE CONNECTOR",
                        "value": "SMA 4 HOLE CONNECTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/HIGH_FREQ/HIGH_FREQ_CONNECTOR/h_f_connnector/SMA_4_HOLE_CONNECTOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_other_items": {

                "question": "Which Other Microwave Components Items product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "3 way cavity splitter 800 2500 Mhz",
                        "value": "3 way cavity splitter 800 2500 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/3_way_cavity_splitter_800_2500_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial 20W 2 way power divider 6 40GHz",
                        "value": "coaxial 20W 2 way power divider 6 40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_20W_2_way_power_divider_6_40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ultra low noise amplifier",
                        "value": "ultra low noise amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/ultra_low_noise_amplifier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4-4 Combiner",
                        "value": "4-4 Combiner",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4-4_Combiner.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "INDOOR OUTDOOR 1800 and 2100MHz DIPLEXER",
                        "value": "INDOOR OUTDOOR 1800 and 2100MHz DIPLEXER",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/INDOOR_OUTDOOR_1800_and_2100MHz_DIPLEXER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GSM 900 TOWER MOUNT AMPLIFIER",
                        "value": "GSM 900 TOWER MOUNT AMPLIFIER",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/GSM_900_TOWER_MOUNT_AMPLIFIER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8Way 6-40GHz",
                        "value": "8Way 6-40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/8Way_6-40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "6Way 18-40GHz",
                        "value": "6Way 18-40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/6Way_18-40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GSM DCS WCDMA WLAN QUADRUPLE BAND COMBINER1",
                        "value": "GSM DCS WCDMA WLAN QUADRUPLE BAND COMBINER1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/GSM_DCS_WCDMA_WLAN_QUADRUPLE_BAND_COMBINER1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 Way Cavity Splitter 380-400MHz",
                        "value": "4 Way Cavity Splitter 380-400MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4_Way_Cavity_Splitter_380-400MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block 2.2GHz 50ohm BNC Type",
                        "value": "DC Block 2.2GHz 50ohm BNC Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/DC_Block_2.2GHz_50ohm_BNC_Type.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "DCS1800MHz WCDMA2100 MHz QUADRUPLEXERS",
                        "value": "DCS1800MHz WCDMA2100 MHz QUADRUPLEXERS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/DCS1800MHz_WCDMA2100_MHz_QUADRUPLEXERS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5W N MALE DUMMYLOAD",
                        "value": "5W N MALE DUMMYLOAD",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/5W_N_MALE_DUMMYLOAD.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "wr series",
                        "value": "wr series",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/wr_series.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RFS FDDW60021C3L",
                        "value": "RFS FDDW60021C3L",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/RFS_FDDW60021C3L.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Flange dia",
                        "value": "Flange dia",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Flange_dia.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5 WATT DIN TYPE DUMMYLOAD",
                        "value": "5 WATT DIN TYPE DUMMYLOAD",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/5_WATT_DIN_TYPE_DUMMYLOAD.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "50 WATT DIN TYPE DUMMYLOAD",
                        "value": "50 WATT DIN TYPE DUMMYLOAD",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/50_WATT_DIN_TYPE_DUMMYLOAD.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 Way Cavity Splitter 180-400MHz",
                        "value": "2 Way Cavity Splitter 180-400MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2_Way_Cavity_Splitter_180-400MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RF Switch 24V",
                        "value": "RF Switch 24V",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/RF_Switch_24V.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "10 W DUMMYLOAD N MALE",
                        "value": "10 W DUMMYLOAD N MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/10_W_DUMMYLOAD_N_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial watt 2 way power divider 2 40 GHz",
                        "value": "coaxial watt 2 way power divider 2 40 GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_watt_2_way_power_divider_2_40_GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "wide band power amplifier 6 12 GHz",
                        "value": "wide band power amplifier 6 12 GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/wide_band_power_amplifier_6_12_GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "50 WATT DUMMYLOAD N MALE",
                        "value": "50 WATT DUMMYLOAD N MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/50_WATT_DUMMYLOAD_N_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial 30 W 2way power divider 6 18 GHz",
                        "value": "coaxial 30 W 2way power divider 6 18 GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_30_W_2way_power_divider_6_18%20GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block 6GHz",
                        "value": "DC Block 6GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/DC_Block_6GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0.5 SMA DUMMYLOAD",
                        "value": "0.5 SMA DUMMYLOAD",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/0.5_SMA_DUMMYLOAD.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 way cavity splitter 700 3500 Mhz",
                        "value": "4 way cavity splitter 700 3500 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4_way_cavity_splitter_700_3500_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "C band high gainlow noise power amplifiers",
                        "value": "C band high gainlow noise power amplifiers",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/C_band_high_gainlow_noise_power_amplifiers.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "cal-short",
                        "value": "cal-short",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/cal-short.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial 20 W 2way power divider 0.5 18 GHz",
                        "value": "coaxial 20 W 2way power divider 0.5 18 GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_20_W_2way_power_divider_0.5_18%20GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Level One VoiceCon VOI 7100 VoIP phone",
                        "value": "Level One VoiceCon VOI 7100 VoIP phone",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/VoIP/Level_One_VoiceCon_VOI_7100_VoIP_phone.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Zero Bias Microwave Detector",
                        "value": "Zero Bias Microwave Detector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Zero_Bias_Microwave_Detector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "6Way 0.8-18GHz",
                        "value": "6Way 0.8-18GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/6Way_0.8-18GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "16Way 6-40GHz",
                        "value": "16Way 6-40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/16Way_6-40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3Way 0.5-18GHz",
                        "value": "3Way 0.5-18GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/3Way_0.5-18GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 way N F microstrip 2500Mhz",
                        "value": "2 way N F microstrip 2500Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2_way_N_F_microstrip_2500Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial 30W 2 way power divider",
                        "value": "coaxial 30W 2 way power divider",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_30W_2_way_power_divider.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "cal-open",
                        "value": "cal-open",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/cal-open.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ultra wide band AC power amplifier",
                        "value": "ultra wide band AC power amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/ultra_wide_band_AC_power_amplifier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "16Way 6-26.5GHz",
                        "value": "16Way 6-26.5GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/16Way_6-26.5GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2W DIN TYPE Dummy Load",
                        "value": "2W DIN TYPE Dummy Load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/2W_DIN_TYPE_Dummy_Load.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "cal-load",
                        "value": "cal-load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/HIGH_FREQ/cal-load.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "medium power wide band driver amplifier",
                        "value": "medium power wide band driver amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/medium_power_wide_band_driver_amplifier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block 8GHz 50ohm SMA Type",
                        "value": "DC Block 8GHz 50ohm SMA Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/DC_Block_8GHz_50ohm_SMA_Type.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "Gas Discharge Tube type Surge Protector N Male to N Female Bulkhead Port 1.2GHz-2.6GHz)",
                        "value": "Gas Discharge Tube type Surge Protector N Male to N Female Bulkhead Port 1.2GHz-2.6GHz)",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Gas_Discharge_Tube_type_Surge_Protector_N_Male_to_N_Female_Bulkhead_Port_1.2GHz-2.6GHz).pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2W SMA M DUMMYLOAD 18GHZ",
                        "value": "2W SMA M DUMMYLOAD 18GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/2W_SMA_M_DUMMYLOAD_18GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2Way 1-40GHz",
                        "value": "2Way 1-40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2Way_1-40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block 18GHz SMA Type",
                        "value": "DC Block 18GHz SMA Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/DC_Block_18GHz_SMA_Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "High Frequency Product.compressed",
                        "value": "High Frequency Product.compressed",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Product/High_Frequency_Product.compressed.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8 way N F microstrip 2500Mhz",
                        "value": "8 way N F microstrip 2500Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/8_way_N_F_microstrip_2500Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "200W Dummy Load N Male",
                        "value": "200W Dummy Load N Male",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/200W_Dummy_Load_N_Male.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1W DUMMLOAD BNC",
                        "value": "1W DUMMLOAD BNC",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/1W_DUMMLOAD_BNC.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8 way SMA F microstrip 3000Mhz",
                        "value": "8 way SMA F microstrip 3000Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/8_way_SMA_F_microstrip_3000Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 way cavity splitter 700 2700 Mhz",
                        "value": "2 way cavity splitter 700 2700 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2_way_cavity_splitter_700_2700_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 way N F microstrip 2500Mhz",
                        "value": "4 way N F microstrip 2500Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4_way_N_F_microstrip_2500Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "100W Dummy Load N Males",
                        "value": "100W Dummy Load N Males",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/100W_Dummy_Load_N_Males.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ultra wide band low noise amplifier",
                        "value": "ultra wide band low noise amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/ultra_wide_band_low_noise_amplifier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial 50 watt 2 way power divider",
                        "value": "coaxial 50 watt 2 way power divider",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_50_watt_2_way_power_divider.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 watt n male Dummy load",
                        "value": "2 watt n male Dummy load",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/2_watt_n_male_Dummy_load.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8Way 0.5-40GHz",
                        "value": "8Way 0.5-40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/8Way_0.5-40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block F-Type",
                        "value": "DC Block F-Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/DC_Block_F-Type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Diplexer",
                        "value": "Diplexer",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Diplexer.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC Block 2.2GHz 75ohm BNC Type",
                        "value": "DC Block 2.2GHz 75ohm BNC Type",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/DC_Block_2.2GHz_75ohm_BNC_Type.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "PCS DUAL TOWER MOUNT AMPLIFIER",
                        "value": "PCS DUAL TOWER MOUNT AMPLIFIER",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/PCS_DUAL_TOWER_MOUNT_AMPLIFIER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 way cavity splitter 800 2500 Mhz",
                        "value": "4 way cavity splitter 800 2500 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4_way_cavity_splitter_800_2500_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4Way 1-40GHz",
                        "value": "4Way 1-40GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4Way_1-40GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1W 50Ohm 18Ghz Dummy Load SMAM",
                        "value": "1W 50Ohm 18Ghz Dummy Load SMAM",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/1W_50Ohm_18Ghz_Dummy_Load_SMAM.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4Way 0.3-18GHz",
                        "value": "4Way 0.3-18GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4Way_0.3-18GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 watt F M dummyload",
                        "value": "2 watt F M dummyload",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/2_watt_F_M_dummyload.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 way SMA F microstrip 3000Mhz",
                        "value": "2 way SMA F microstrip 3000Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2_way_SMA_F_microstrip_3000Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1W DUMMYLOAD N MALE",
                        "value": "1W DUMMYLOAD N MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/1W_DUMMYLOAD_N_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2Way 0.3-18GHZ",
                        "value": "2Way 0.3-18GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2Way_0.3-18GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3 way N F microstrip 2500Mhz",
                        "value": "3 way N F microstrip 2500Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/3_way_N_F_microstrip_2500Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "25 WATT DUMMYLOAD N MALE",
                        "value": "25 WATT DUMMYLOAD N MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Dummy_Load/25_WATT_DUMMYLOAD_N_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coaxial 10watt 3way power divider 1 500 MHz",
                        "value": "coaxial 10watt 3way power divider 1 500 MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/coaxial_10watt_3way_power_divider_1_500%20MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RP SMA DC block",
                        "value": "RP SMA DC block",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DC_Block/RP_SMA_DC_block.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "TRIPLE BAND COMBINER INDOOR OUTDOOR",
                        "value": "TRIPLE BAND COMBINER INDOOR OUTDOOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/TRIPLE_BAND_COMBINER_INDOOR_OUTDOOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "10W ultra wide band amplifier",
                        "value": "10W ultra wide band amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/10W_ultra_wide_band_amplifier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3Way 18-26.5GHz",
                        "value": "3Way 18-26.5GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/3Way_18-26.5GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3 way cavity splitter 700 2700 Mhz",
                        "value": "3 way cavity splitter 700 2700 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/3_way_cavity_splitter_700_2700_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 way cavity splitter 800 2500 Mhz",
                        "value": "2 way cavity splitter 800 2500 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/2_way_cavity_splitter_800_2500_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 way SMA F microstrip 2500Mhz",
                        "value": "4 way SMA F microstrip 2500Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4_way_SMA_F_microstrip_2500Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "30w solid state high power amplifier",
                        "value": "30w solid state high power amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/30w_solid_state_high_power_amplifier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 way cavity splitter 700 2700 Mhz",
                        "value": "4 way cavity splitter 700 2700 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/4_way_cavity_splitter_700_2700_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "INDOOR OUTDOOR 900 1800 AND 2100 DIPLEXER",
                        "value": "INDOOR OUTDOOR 900 1800 AND 2100 DIPLEXER",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/DIPLEXER/INDOOR_OUTDOOR_900_1800_AND_2100_DIPLEXER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "adapter",
                        "value": "adapter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/high_freq_catalouge/adapter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RF Switch 12V",
                        "value": "RF Switch 12V",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/RF_Switch_12V.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "narrow wide band low noise amplifier",
                        "value": "narrow wide band low noise amplifier",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/amplifier_combiner/narrow_wide_band_low_noise_amplifier.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp10t": {

                "question": "Which SP10T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP10T SMA F 15G F L M",
                        "value": "SP10T SMA F 15G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP10T/SP10T_SMA_F_15G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp10t_terminated": {

                "question": "Which SP10T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP10T OPEN PORTS TERMINATED 15G",
                        "value": "SP10T OPEN PORTS TERMINATED 15G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP10T_TERMINATED/SP10T_OPEN_PORTS_TERMINATED_15G.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp3t": {

                "question": "Which SP3T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP3T G3 SMA F 26.5G MOUNTING BRACKET",
                        "value": "SP3T G3 SMA F 26.5G MOUNTING BRACKET",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T/SP3T_G3_SMA_F_26.5G_MOUNTING_BRACKET.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP3T W3 SC F 6G MOMENTARY LATCHING",
                        "value": "SP3T W3 SC F 6G MOMENTARY LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T/SP3T_W3_SC_F_6G_MOMENTARY_LATCHING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP3T U3 N F 12.4G MOMENTARY LATCHING",
                        "value": "SP3T U3 N F 12.4G MOMENTARY LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T/SP3T_U3_N_F_12.4G_MOMENTARY_LATCHING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP3T H3 SMA F 26.5G MOMENTARY LATCHING",
                        "value": "SP3T H3 SMA F 26.5G MOMENTARY LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T/SP3T_H3_SMA_F_26.5G_MOMENTARY_LATCHING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP3T F3 SMA F 26.5G MOMENTARY",
                        "value": "SP3T F3 SMA F 26.5G MOMENTARY",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T/SP3T_F3_SMA_F_26.5G_MOMENTARY.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp3t_terminated": {

                "question": "Which SP3T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP3T P3 SMA F 26.5G MOMENTARY LATCHING",
                        "value": "SP3T P3 SMA F 26.5G MOMENTARY LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T_TERMINATED/SP3T_P3_SMA_F_26.5G_MOMENTARY_LATCHING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP3T Q3 MOUNTING 26.5G MOMENTARY LATCHING",
                        "value": "SP3T Q3 MOUNTING 26.5G MOMENTARY LATCHING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP3T_TERMINATED/SP3T_Q3_MOUNTING_26.5G_MOMENTARY_LATCHING.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp4t": {

                "question": "Which SP4T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP4T W4 SC F DC 6 FAILSAFE LATCHING MOMENTARY",
                        "value": "SP4T W4 SC F DC 6 FAILSAFE LATCHING MOMENTARY",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP4T/SP4T_W4_SC_F_DC_6_FAILSAFE_LATCHING_MOMENTARY.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP4T U4 N F DC 12.4 FAILSAFE LATCHING MOMENTARY",
                        "value": "SP4T U4 N F DC 12.4 FAILSAFE LATCHING MOMENTARY",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP4T/SP4T_U4_N_F_DC_12.4_FAILSAFE_LATCHING_MOMENTARY.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP4T G4 SMA F DC 26.5 FAILSAFE LATCHING MOMENTARY",
                        "value": "SP4T G4 SMA F DC 26.5 FAILSAFE LATCHING MOMENTARY",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP4T/SP4T_G4_SMA_F_DC_26.5_FAILSAFE_LATCHING_MOMENTARY.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP4T H4 SMA F DC 26.5 FAILSAFE LATCHING MOMENTARY",
                        "value": "SP4T H4 SMA F DC 26.5 FAILSAFE LATCHING MOMENTARY",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP4T/SP4T_H4_SMA_F_DC_26.5_FAILSAFE_LATCHING_MOMENTARY.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp4t_terminated": {

                "question": "Which SP4T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP4T TERMINATED Q4 MOUNTING 26.5G F L M",
                        "value": "SP4T TERMINATED Q4 MOUNTING 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP4T_TERMINATED/SP4T_TERMINATED_Q4_MOUNTING_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP4T TERMINATED P4 SMA F 26.5G",
                        "value": "SP4T TERMINATED P4 SMA F 26.5G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP4T_TERMINATED/SP4T_TERMINATED_P4_SMA_F_26.5G.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp5t": {

                "question": "Which SP5T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP5T G5 SMA F 26.5G M L F",
                        "value": "SP5T G5 SMA F 26.5G M L F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T/SP5T_G5_SMA_F_26.5G_M_L_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP5T F5 SMA F 26.5G MOMENTARY ONLY",
                        "value": "SP5T F5 SMA F 26.5G MOMENTARY ONLY",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T/SP5T_F5_SMA_F_26.5G_MOMENTARY_ONLY.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP5T H5 SMA F 26.5G M L F",
                        "value": "SP5T H5 SMA F 26.5G M L F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T/SP5T_H5_SMA_F_26.5G_M_L_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP5T U5 N F 12.4G M L F",
                        "value": "SP5T U5 N F 12.4G M L F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T/SP5T_U5_N_F_12.4G_M_L_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP5T W5 VHP SC F 6G M L F",
                        "value": "SP5T W5 VHP SC F 6G M L F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T/SP5T_W5_VHP_SC_F_6G_M_L_F.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp5t_terminated": {

                "question": "Which SP5T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP5T TERMINATED Q5 MOUNTING BRACKET 26.5G F L M",
                        "value": "SP5T TERMINATED Q5 MOUNTING BRACKET 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T_TERMINATED/SP5T_TERMINATED_Q5_MOUNTING_BRACKET_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP5T TERMINATED P5 SMA F 26.5G F L M",
                        "value": "SP5T TERMINATED P5 SMA F 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP5T_TERMINATED/SP5T_TERMINATED_P5_SMA_F_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp6t": {

                "question": "Which SP6T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP6T H6 SMA F 26.5G F L M",
                        "value": "SP6T H6 SMA F 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T/SP6T_H6_SMA_F_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP6T U6 N F 12.4G F L M",
                        "value": "SP6T U6 N F 12.4G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T/SP6T_U6_N_F_12.4G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP6T F6 SMA F 26.5G NORMALY OPEN",
                        "value": "SP6T F6 SMA F 26.5G NORMALY OPEN",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T/SP6T_F6_SMA_F_26.5G_NORMALY_OPEN.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP6T W6 VHF SC F 6G F L M",
                        "value": "SP6T W6 VHF SC F 6G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T/SP6T_W6_VHF_SC_F_6G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP6T G6 MOUNTING BRACKET SMA F 26.5G F L M",
                        "value": "SP6T G6 MOUNTING BRACKET SMA F 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T/SP6T_G6_MOUNTING_BRACKET_SMA_F_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp6t_terminated": {

                "question": "Which SP6T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP6T TERMINATED P6 SMA F 26.5G F L M",
                        "value": "SP6T TERMINATED P6 SMA F 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T_TERMINATED/SP6T_TERMINATED_P6_SMA_F_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP6T TERMINATED Q6 MOUNTING BRACKET 26.5G F L M",
                        "value": "SP6T TERMINATED Q6 MOUNTING BRACKET 26.5G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP6T_TERMINATED/SP6T_TERMINATED_Q6_MOUNTING_BRACKET_26.5G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp8t": {

                "question": "Which SP8T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP8T J8 MOMENTARY 20G",
                        "value": "SP8T J8 MOMENTARY 20G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP8T/SP8T_J8_MOMENTARY_20G.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP8T K8 SMA F 18G F L M",
                        "value": "SP8T K8 SMA F 18G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP8T/SP8T_K8_SMA_F_18G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP8T N8 MOUNTING BRACKET SMA F 18G F L M",
                        "value": "SP8T N8 MOUNTING BRACKET SMA F 18G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP8T/SP8T_N8_MOUNTING_BRACKET_SMA_F_18G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp8t_terminated": {

                "question": "Which SP8T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP8T TERMINATED O8 OPEN PORT 18G F L M",
                        "value": "SP8T TERMINATED O8 OPEN PORT 18G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP8T_TERMINATED/SP8T_TERMINATED_O8_OPEN_PORT_18G_F_L_M.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SP8T TERMINATED M8 SMA F 18G F L M",
                        "value": "SP8T TERMINATED M8 SMA F 18G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP8T_TERMINATED/SP8T_TERMINATED_M8_SMA_F_18G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp9t": {

                "question": "Which SP9T product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP9T SMA F 15G F L M",
                        "value": "SP9T SMA F 15G F L M",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP9T/SP9T_SMA_F_15G_F_L_M.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_sp9t_terminated": {

                "question": "Which SP9T Terminated product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SP9T OPEN PORT TERMINATED SMA F 15 G",
                        "value": "SP9T OPEN PORT TERMINATED SMA F 15 G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SP9T_TERMINATED/SP9T_OPEN_PORT_TERMINATED_SMA_F_15_G.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_spdt": {

                "question": "Which SPDT product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SPDT B1 SMA F 26.5G Failsafe",
                        "value": "SPDT B1 SMA F 26.5G Failsafe",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SPDT/SPDT_B1_SMA_F_26.5G_Failsafe.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SPDT B10 SMA F 26.5G 4mounting holes",
                        "value": "SPDT B10 SMA F 26.5G 4mounting holes",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SPDT/SPDT_B10_SMA_F_26.5G_4mounting_holes.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_spdt_termineted": {

                "question": "Which SPDT Termineted product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SPDT B6 TERMINATED N F 12.4G",
                        "value": "SPDT B6 TERMINATED N F 12.4G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/RF_Switch/SPDT_TERMINETED/SPDT_B6_TERMINATED_N_F_12.4G.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_splitters": {

                "question": "Which Splitters product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2 way SMA F microstrip 2500Mhz",
                        "value": "2 way SMA F microstrip 2500Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Splitters/Microstrip_splitter/2_way_SMA_F_microstrip_2500Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5G Splitter",
                        "value": "5G Splitter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Splitters/cavity/5G_Splitter.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "microwave_components_surg_arrester": {

                "question": "Which SURG Arrester product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N (M) to N (F) B H 2.5 Ghz Surge Arrestor",
                        "value": "N (M) to N (F) B H 2.5 Ghz Surge Arrestor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/Gas_Tube/N_(M)_to_N_(F)_B_H_2.5_Ghz_Surge_Arrestor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN (M) to DIN (F) T 2.5 Mhz Surge Arrestor",
                        "value": "DIN (M) to DIN (F) T 2.5 Mhz Surge Arrestor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/T_Type/DIN_(M)_to_DIN_(F)_T_2.5_Mhz_Surge_Arrestor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "f F f f surge arrster",
                        "value": "f F f f surge arrster",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/Gas_Tube/f_F_f_f_surge_arrster.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N (f) to N (f) B H 6 Ghz Surge Arrestor",
                        "value": "N (f) to N (f) B H 6 Ghz Surge Arrestor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/Gas_Tube/N_(f)_to_N_(f)_B_H_6_Ghz_Surge_Arrestor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC (M) to TNC (F) B H 2.5 Ghz Surge Arrestor",
                        "value": "TNC (M) to TNC (F) B H 2.5 Ghz Surge Arrestor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/Gas_Tube/TNC_(M)_to_TNC_(F)_B_H_2.5_Ghz_Surge_Arrestor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DC1 Surge suppressor for CMM5",
                        "value": "DC1 Surge suppressor for CMM5",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/DC1_Surge_suppressor_for_CMM5.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "f m f f surge arrster",
                        "value": "f m f f surge arrster",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/Gas_Tube/f_m_f_f_surge_arrster.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RJ45 DATA SURGE ARR Specifications",
                        "value": "RJ45 DATA SURGE ARR Specifications",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/RJ45_DATA_SURGE_ARR_Specifications.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N (M) to N (F) B H 3 Ghz Surge Arrestor",
                        "value": "N (M) to N (F) B H 3 Ghz Surge Arrestor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/Gas_Tube/N_(M)_to_N_(F)_B_H_3_Ghz_Surge_Arrestor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Surge Protector MHT-N5-2",
                        "value": "Surge Protector MHT-N5-2",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/SURG_ARRESTER/T_Type/Surge_Protector_MHT-N5-2.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Which Antenna?
            # -------------------------------------------------

            "antennas": {

                "question": "Which Antenna?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "5G Horn Antenna",
                        "value": "5G Horn Antenna",
                        "next": "antennas_5g_horn_antenna"
                    },

                    {
                        "text": "Antenna Cable",
                        "value": "Antenna Cable",
                        "next": "antennas_antenna_cable"
                    },

                    {
                        "text": "Coaxial Connector",
                        "value": "Coaxial Connector",
                        "next": "antennas_coaxial_connector"
                    },

                    {
                        "text": "Final Antenna",
                        "value": "Final Antenna",
                        "next": "antennas_final_antenna"
                    },

                    {
                        "text": "GPS Antenna",
                        "value": "GPS Antenna",
                        "next": "antennas_gps_antenna"
                    },

                    {
                        "text": "Hand Tools",
                        "value": "Hand Tools",
                        "next": "antennas_hand_tools"
                    },

                    {
                        "text": "HF UHF VHF Antennas",
                        "value": "HF UHF VHF Antennas",
                        "next": "antennas_hf_uhf_vhf_antennas"
                    },

                    {
                        "text": "Hornantenna",
                        "value": "Hornantenna",
                        "next": "antennas_hornantenna"
                    },

                    {
                        "text": "Newantenna",
                        "value": "Newantenna",
                        "next": "antennas_newantenna"
                    },

                    {
                        "text": "Open Ended Waveguide Probes",
                        "value": "Open Ended Waveguide Probes",
                        "next": "antennas_open_ended_waveguide_probes"
                    },

                    {
                        "text": "Other Antennas Items",
                        "value": "Other Antennas Items",
                        "next": "antennas_other_items"
                    },

                    {
                        "text": "PANEL Antenna",
                        "value": "PANEL Antenna",
                        "next": "antennas_panel_antenna"
                    },

                    {
                        "text": "Wave Guides",
                        "value": "Wave Guides",
                        "next": "antennas_wave_guides"
                    }

                ]

            },

            "antennas_5g_horn_antenna": {

                "question": "Which 5G Horn Antenna product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Broadband Horn Antenna 18 50G 20dBi",
                        "value": "Broadband Horn Antenna 18 50G 20dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_18_50G_20dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 6 67G 13dBi",
                        "value": "Broadband Horn Antenna 6 67G 13dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_6_67G_13dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 50 65G 20dBi 1.85F",
                        "value": "Standerd Gain Horn Antenna 50 65G 20dBi 1.85F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_50_65G_20dBi_1.85F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 0.7 18G 12dBi",
                        "value": "Broadband Horn Antenna 0.7 18G 12dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_0.7_18G_12dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 18 40G 15dBi",
                        "value": "Broadband Horn Antenna 18 40G 15dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_18_40G_15dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 22 33G 20dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 22 33G 20dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_22_33G_20dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Multi Octave Horn Antenna 18 40G 15dBi 2.92F",
                        "value": "Multi Octave Horn Antenna 18 40G 15dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Multi_Octave_Horn_Antenna/Multi_Octave_Horn_Antenna_18_40G_15dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Pol Horn Antenna 18 40G 15dBi 2.92F",
                        "value": "Dual Pol Horn Antenna 18 40G 15dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Dual_Pol_Horn_Antenna/Dual_Pol_Horn_Antenna_18_40G_15dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 26 40G 20dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 26 40G 20dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_26_40G_20dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Pol Horn Antenna 5 50G 15dBi 2.4F",
                        "value": "Dual Pol Horn Antenna 5 50G 15dBi 2.4F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Dual_Pol_Horn_Antenna/Dual_Pol_Horn_Antenna_5_50G_15dBi_2.4F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 22 33G 15dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 22 33G 15dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_22_33G_15dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 26 40G 15dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 26 40G 15dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_26_40G_15dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 26 40G 10dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 26 40G 10dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_26_40G_10dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 0.8 8G 10dBi",
                        "value": "Broadband Horn Antenna 0.8 8G 10dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_0.8_8G_10dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Conical Horn Antenna SB 28 20 26.5 40G 2.92F",
                        "value": "Conical Horn Antenna SB 28 20 26.5 40G 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Conical_Horn_Antenna/Conical_Horn_Antenna_SB_28_20_26.5_40G_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 22 33G 25dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 22 33G 25dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_22_33G_25dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2in1 Hybrid Coupler 0740Mhz 150",
                        "value": "2in1 Hybrid Coupler 0740Mhz 150",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/2in1_Hybrid_Coupler_0740Mhz_150.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 4.5 45G 13dBi",
                        "value": "Broadband Horn Antenna 4.5 45G 13dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_4.5_45G_13dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Pol Horn Antenna 0.4 6G 4 14dBi SF",
                        "value": "Dual Pol Horn Antenna 0.4 6G 4 14dBi SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Dual_Pol_Horn_Antenna/Dual_Pol_Horn_Antenna_0.4_6G_4_14dBi_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Pol Horn Antenna 18 43.5G 15dBi 2.4F",
                        "value": "Dual Pol Horn Antenna 18 43.5G 15dBi 2.4F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Dual_Pol_Horn_Antenna/Dual_Pol_Horn_Antenna_18_43.5G_15dBi_2.4F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Multi Octave Horn Antenna 18 40G 25dBi 2.92F",
                        "value": "Multi Octave Horn Antenna 18 40G 25dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Multi_Octave_Horn_Antenna/Multi_Octave_Horn_Antenna_18_40G_25dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Bi Conical Horn Antenna 4 40G 3dBi P",
                        "value": "Bi Conical Horn Antenna 4 40G 3dBi P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Bi_Conical_Horn_Antenna/Bi_Conical_Horn_Antenna_4_40G_3dBi_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2in1 Hybrid Coupler 0738Mhz",
                        "value": "2in1 Hybrid Coupler 0738Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/2in1_Hybrid_Coupler_0738Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Multi Octave Horn Antenna 18 40G 10dBi 2.92F",
                        "value": "Multi Octave Horn Antenna 18 40G 10dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Multi_Octave_Horn_Antenna/Multi_Octave_Horn_Antenna_18_40G_10dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 50 65G 25dBi 1.85F",
                        "value": "Standerd Gain Horn Antenna 50 65G 25dBi 1.85F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_50_65G_25dBi_1.85F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Pol Horn Antenna 0.7 7G 11dBi SF",
                        "value": "Dual Pol Horn Antenna 0.7 7G 11dBi SF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Dual_Pol_Horn_Antenna/Dual_Pol_Horn_Antenna_0.7_7G_11dBi_SF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Diagonal Horn Antenna 28 20 26.5 40G 2.92F",
                        "value": "Diagonal Horn Antenna 28 20 26.5 40G 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Diagonal_Horn_Antenna/Diagonal_Horn_Antenna_28_20_26.5_40G_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 22 33G 10dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 22 33G 10dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_22_33G_10dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 4 40G 13dBi",
                        "value": "Broadband Horn Antenna 4 40G 13dBi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Broadband_Horn_Antenna/Broadband_Horn_Antenna_4_40G_13dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Multi Octave Horn Antenna 18 40G 20dBi 2.92F",
                        "value": "Multi Octave Horn Antenna 18 40G 20dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Multi_Octave_Horn_Antenna/Multi_Octave_Horn_Antenna_18_40G_20dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 26 40G 25dBi 2.92F",
                        "value": "Standerd Gain Horn Antenna 26 40G 25dBi 2.92F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_26_40G_25dBi_2.92F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 1.7 2.6G 10dBi NF",
                        "value": "Standerd Gain Horn Antenna 1.7 2.6G 10dBi NF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_1.7_2.6G_10dBi_NF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 50 65G 15dBi 1.85F",
                        "value": "Standerd Gain Horn Antenna 50 65G 15dBi 1.85F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_50_65G_15dBi_1.85F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standerd Gain Horn Antenna 50 65G 10dBi 1.85F",
                        "value": "Standerd Gain Horn Antenna 50 65G 10dBi 1.85F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Standerd_Gain_Horn_Antenna/Standerd_Gain_Horn_Antenna_50_65G_10dBi_1.85F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Conical Horn Antenna SB 28 20 24 50G 2.4F",
                        "value": "Conical Horn Antenna SB 28 20 24 50G 2.4F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/5G_Horn_Antenna/Conical_Horn_Antenna/Conical_Horn_Antenna_SB_28_20_24_50G_2.4F.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_antenna_cable": {

                "question": "Which Antenna Cable product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "ufl ufl connector",
                        "value": "ufl ufl connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/antenna_cable/ufl_ufl_connector.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_coaxial_connector": {

                "question": "Which Coaxial Connector product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "ALL CONNECTOR",
                        "value": "ALL CONNECTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/ALL_CONNECTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE FLANGE MOUNT CONNECTOR FOR RG402 141 CABLE",
                        "value": "N FEMALE FLANGE MOUNT CONNECTOR FOR RG402 141 CABLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/Coaxial_Connector/N/N_FEMALE_FLANGE_MOUNT_CONNECTOR_FOR_RG402_141_CABLE.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_final_antenna": {

                "question": "Which Final Antenna product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Sector Antenna 17dbi 5700 5900Mhz Kenstal",
                        "value": "Sector Antenna 17dbi 5700 5900Mhz Kenstal",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/Sector_Antenna_17dbi_5700_5900Mhz_Kenstal.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "UHF Duplexer Filer",
                        "value": "UHF Duplexer Filer",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/UHF_Duplexer_Filer.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7 dBi Vehicle Antenna",
                        "value": "7 dBi Vehicle Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/7_dBi_Vehicle_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4.9 5.9GHz 18dbi MIMO Sector antennas 60 90 120",
                        "value": "4.9 5.9GHz 18dbi MIMO Sector antennas 60 90 120",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/4.9_5.9GHz_18dbi_MIMO_Sector_antennas_60_90_120.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5 dBi Vehicle Antenna",
                        "value": "5 dBi Vehicle Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/5_dBi_Vehicle_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "9dbi Magnetic Base Antenna with 3Mtr 698 2700Mhz",
                        "value": "9dbi Magnetic Base Antenna with 3Mtr 698 2700Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/9dbi_Magnetic_Base_Antenna_with_3Mtr_698_2700Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4.9 5.8GHz MIMO Dish Antenna",
                        "value": "4.9 5.8GHz MIMO Dish Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/4.9_5.8GHz_MIMO_Dish_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "unipole folded antenna",
                        "value": "unipole folded antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/unipole_folded_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3.3 3.8 GHZ SECTOR ANTENNA",
                        "value": "3.3 3.8 GHZ SECTOR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/3.3_3.8_GHZ_SECTOR_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GSM Ceiling Antenna",
                        "value": "GSM Ceiling Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/GSM_Ceiling_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8-10dbi 5150-5250Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "8-10dbi 5150-5250Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/8-10dbi%205150-5250Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8 9 dbi panel antenna",
                        "value": "8 9 dbi panel antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/8_9_dbi_panel_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5GHZ MIMO OMNI ANTENNAS 12dBi",
                        "value": "5GHZ MIMO OMNI ANTENNAS 12dBi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/5GHZ_MIMO_OMNI_ANTENNAS_12dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5-6dbi 430-435Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "5-6dbi 430-435Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/5-6dbi%20430-435Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GPS INDOOR ANTENNA 28DBI 3MTR RG174 SMAM1",
                        "value": "GPS INDOOR ANTENNA 28DBI 3MTR RG174 SMAM1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/GPS_INDOOR_ANTENNA_28DBI_3MTR_RG174_SMAM1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3 dBi Vehicle Antenna",
                        "value": "3 dBi Vehicle Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/3_dBi_Vehicle_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "9DBI GSM MAGNETIC ANTENNA",
                        "value": "9DBI GSM MAGNETIC ANTENNA",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/9DBI_GSM_MAGNETIC_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5-6dbi 2400-2485Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "5-6dbi 2400-2485Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/5-6dbi%202400-2485Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8-10dbi 5750-5875Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "8-10dbi 5750-5875Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/8-10dbi%205750-5875Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "24GHZ MIMO OMNI ANTENNAS 12dBi",
                        "value": "24GHZ MIMO OMNI ANTENNAS 12dBi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/24GHZ_MIMO_OMNI_ANTENNAS_12dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 2400 2500 Mhz",
                        "value": "helical antenna 2400 2500 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_2400_2500_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.3 2.7GHz MIMO Sector Antenna",
                        "value": "2.3 2.7GHz MIMO Sector Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/2.3_2.7GHz_MIMO_Sector_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.4 2.5GHz Dual Polarized MIMO Patch Antennas 12 14&18 dBi",
                        "value": "2.4 2.5GHz Dual Polarized MIMO Patch Antennas 12 14&18 dBi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/2.4_2.5GHz_Dual_Polarized_MIMO_Patch_Antennas_12_14&18_dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4g panel antenna",
                        "value": "4g panel antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/4g_panel_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5-6dbi 902-928Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "5-6dbi 902-928Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/5-6dbi%20902-928Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5-6dbi 1160-1280Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "5-6dbi 1160-1280Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/5-6dbi%201160-1280Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 430 435 Mhz",
                        "value": "helical antenna 430 435 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_430_435_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "9dBi Collinear Omni Directional Antenna",
                        "value": "9dBi Collinear Omni Directional Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/9dBi_Collinear_Omni_Directional_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GPS GLONASS ANTENNA",
                        "value": "GPS GLONASS ANTENNA",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/GPS_GLONASS_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 5720 5875 Mhz",
                        "value": "helical antenna 5720 5875 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_5720_5875_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "omni directional antenna 1710 1880mhz",
                        "value": "omni directional antenna 1710 1880mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/omni_directional_antenna_1710_1880mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "VHF Duplexer Filer",
                        "value": "VHF Duplexer Filer",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/VHF_Duplexer_Filer.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "LPDA ANTENNA 14DBI 698 2700Mhz 1FEET RG58 NF",
                        "value": "LPDA ANTENNA 14DBI 698 2700Mhz 1FEET RG58 NF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/LPDA_ANTENNA_14DBI_698_2700Mhz_1FEET_RG58_NF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 30 mhz hf antenna",
                        "value": "2 30 mhz hf antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/2_30_mhz_hf_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 1160 1280 Mhz",
                        "value": "helical antenna 1160 1280 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_1160_1280_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5-6dbi 1560-1580Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "value": "5-6dbi 1560-1580Mhz FIBERGLASS OMNI DIRECTIONAL COLLINEAR ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/5-6dbi%201560-1580Mhz%20FIBERGLASS%20OMNI%20DIRECTIONAL%20COLLINEAR%20ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "LPDA100-1000MHZ 10DB I",
                        "value": "LPDA100-1000MHZ 10DB I",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/LPDA100-1000MHZ_10DB_I.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 902 928 Mhz",
                        "value": "helical antenna 902 928 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_902_928_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "gps 2g 3g 4g combo antenna",
                        "value": "gps 2g 3g 4g combo antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/gps_2g_3g_4g_combo_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5GHz Panel Antennas 22dBi",
                        "value": "5GHz Panel Antennas 22dBi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/final_antenna/5GHz_Panel_Antennas_22dBi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 5150 5250 Mhz",
                        "value": "helical antenna 5150 5250 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_5150_5250_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Mimo Sector Antenna 18dbi 5400 6000Mhz",
                        "value": "Mimo Sector Antenna 18dbi 5400 6000Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/Mimo_Sector_Antenna_18dbi_5400_6000Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "helical antenna 1560 1580 Mhz",
                        "value": "helical antenna 1560 1580 Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/helical_antenna_1560_1580_Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8-10dbi 440-452Mhz Fiber Glass Omni Antenna",
                        "value": "8-10dbi 440-452Mhz Fiber Glass Omni Antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/final_antenna/8-10dbi%20440-452Mhz%20Fiber%20Glass%20Omni%20Antenna.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_gps_antenna": {

                "question": "Which GPS Antenna product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "28 DBI GPS MAGNETIC INDOOR ANTENNA MMCX RA",
                        "value": "28 DBI GPS MAGNETIC INDOOR ANTENNA MMCX RA",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/GPS_Antenna/28_DBI_GPS_MAGNETIC_INDOOR_ANTENNA_MMCX_RA.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_hand_tools": {

                "question": "Which Hand Tools product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "leica icon gps smart antenna",
                        "value": "leica icon gps smart antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/leica_icon_gps_smart_antenna.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_hf_uhf_vhf_antennas": {

                "question": "Which HF UHF VHF Antennas product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "GROUND PLANE UNITY GAIN BASE ANTENNA",
                        "value": "GROUND PLANE UNITY GAIN BASE ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/GROUND_PLANE_UNITY_GAIN_BASE_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "J POLE ANTENNA 2.5dbi",
                        "value": "J POLE ANTENNA 2.5dbi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/J_POLE_ANTENNA_2.5dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0dB WHIP SPRING TYPE ANTENNA",
                        "value": "0dB WHIP SPRING TYPE ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Vehicle_Mobile_Antennas/0dB_WHIP_SPRING_TYPE_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GROUND PLANE UNITY GAIN BASE MILITARY STANDARD ANTENNA GP03ANT",
                        "value": "GROUND PLANE UNITY GAIN BASE MILITARY STANDARD ANTENNA GP03ANT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/GROUND_PLANE_UNITY_GAIN_BASE_MILITARY_STANDARD_ANTENNA_GP03ANT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0dB WHIP MAGNETIC MOUNT ANTENNA",
                        "value": "0dB WHIP MAGNETIC MOUNT ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Vehicle_Mobile_Antennas/0dB_WHIP_MAGNETIC_MOUNT_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YAGI ANTENNA 8dbi 400 450Mhz",
                        "value": "YAGI ANTENNA 8dbi 400 450Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/YAGI_ANTENNA_8dbi_400_450Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5 8 3dB BASE VHF MILITARY STANDARD ANTENNA",
                        "value": "5 8 3dB BASE VHF MILITARY STANDARD ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/5_8_3dB_BASE_VHF_MILITARY_STANDARD_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "136 174 MHz Outdoor Antenna",
                        "value": "136 174 MHz Outdoor Antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/136_174_MHz_Outdoor_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3dB 5 8 lambda Omni directional base antenna",
                        "value": "3dB 5 8 lambda Omni directional base antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/3dB_5_8_lambda_Omni_directional_base_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "OMNI DIRECTIONAL COLLINEAR ANTENNA 3dB GAIN",
                        "value": "OMNI DIRECTIONAL COLLINEAR ANTENNA 3dB GAIN",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/OMNI_DIRECTIONAL_COLLINEAR_ANTENNA_3dB_GAIN.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GROUND PLANE UNITY GAIN BASE MILITARY STANDARD ANTENNA",
                        "value": "GROUND PLANE UNITY GAIN BASE MILITARY STANDARD ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/GROUND_PLANE_UNITY_GAIN_BASE_MILITARY_STANDARD_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "FOLDED STACK DIPOLE ANTENNA OMNI DIRECTIONAL",
                        "value": "FOLDED STACK DIPOLE ANTENNA OMNI DIRECTIONAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/FOLDED_STACK_DIPOLE_ANTENNA_OMNI_DIRECTIONAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "6dB HIGH GAIN BASE ANTENNA",
                        "value": "6dB HIGH GAIN BASE ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/6dB_HIGH_GAIN_BASE_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5 8 3dB BASE ANTENNA VHF",
                        "value": "5 8 3dB BASE ANTENNA VHF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/5_8_3dB_BASE_ANTENNA_VHF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "0dB WHIP CLAMP MOUNT ANTENNA",
                        "value": "0dB WHIP CLAMP MOUNT ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Vehicle_Mobile_Antennas/0dB_WHIP_CLAMP_MOUNT_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YAGI ANTENNA 8dbi",
                        "value": "YAGI ANTENNA 8dbi",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/YAGI_ANTENNA_8dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5 8 3dB WHIP ANTENNA",
                        "value": "5 8 3dB WHIP ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Vehicle_Mobile_Antennas/5_8_3dB_WHIP_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "868 MHz Antenna Outdoor Antenna",
                        "value": "868 MHz Antenna Outdoor Antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/868_MHz_Antenna_Outdoor_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TELESCOPIC TYPE 3dB WHIP ANTENNA",
                        "value": "TELESCOPIC TYPE 3dB WHIP ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Vehicle_Mobile_Antennas/TELESCOPIC_TYPE_3dB_WHIP_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "433MHz Outdoor Antenna",
                        "value": "433MHz Outdoor Antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/433MHz_Outdoor_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "6 dB GROUND PLANE ANTENNA VHF",
                        "value": "6 dB GROUND PLANE ANTENNA VHF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Base_Station_Antennas_VHF_UHF/6_dB_GROUND_PLANE_ANTENNA_VHF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3dB WHIP MAGNETIC MOUNT ANTENNA",
                        "value": "3dB WHIP MAGNETIC MOUNT ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/HF_UHF_VHF_Antennas/Vehicle_Mobile_Antennas/3dB_WHIP_MAGNETIC_MOUNT_ANTENNA.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_hornantenna": {

                "question": "Which Hornantenna product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Broadband Horn Antenna 0.2 2.5GHz",
                        "value": "Broadband Horn Antenna 0.2 2.5GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Broadband_Horn_Antenna_0.2_2.5GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Corrugated Feed Horn Antenna 22 33.0GHz",
                        "value": "Corrugated Feed Horn Antenna 22 33.0GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Corrugated_Feed_Horn_Antenna_22_33.0GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 0.5 6.0GHz",
                        "value": "Broadband Horn Antenna 0.5 6.0GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Broadband_Horn_Antenna_0.5_6.0GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Corrugated Conical Horn Antenna 8.2 12.4GHz",
                        "value": "Corrugated Conical Horn Antenna 8.2 12.4GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Corrugated_Conical_Horn_Antenna_8.2_12.4GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Log Periodic Antenna 100 4000MHz",
                        "value": "Log Periodic Antenna 100 4000MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Log_Periodic_Antenna_100_4000MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Conical Horn Antenna 8.2 12.4GHz",
                        "value": "Conical Horn Antenna 8.2 12.4GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Conical_Horn_Antenna_8.2_12.4GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Open Boundary Quad Ridged Horn Antenna 0.4 6.0GHz",
                        "value": "Open Boundary Quad Ridged Horn Antenna 0.4 6.0GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Open_Boundary_Quad_Ridged_Horn_Antenna_0.4_6.0GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Octave Horn Antenna 4.0 8.0GHz",
                        "value": "Octave Horn Antenna 4.0 8.0GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Octave_Horn_Antenna_4.0_8.0GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "wideband dual rigged Horn antenna",
                        "value": "wideband dual rigged Horn antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/wideband_dual_rigged_Horn_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadband Horn Antenna 0.4 6GHz",
                        "value": "Broadband Horn Antenna 0.4 6GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Broadband_Horn_Antenna_0.4_6GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Standard Horn Antenna 8.2 12.4GHZ",
                        "value": "Standard Horn Antenna 8.2 12.4GHZ",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Standard_Horn_Antenna_8.2_12.4GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Diognal Horn Antenna 8.2 12.4Ghz",
                        "value": "Diognal Horn Antenna 8.2 12.4Ghz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Diognal_Horn_Antenna_8.2_12.4Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Log Periodic Antenna 30 3000MHz",
                        "value": "Log Periodic Antenna 30 3000MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Log_Periodic_Antenna_30_3000MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DISCON ANTENNA 40 5000Mhz",
                        "value": "DISCON ANTENNA 40 5000Mhz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/DISCON_ANTENNA_40_5000Mhz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Log Periodic Antenna 100 400MHz",
                        "value": "Log Periodic Antenna 100 400MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Log_Periodic_Antenna_100_400MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Polarization Horn Antenna 1.0 10.0GHz",
                        "value": "Dual Polarization Horn Antenna 1.0 10.0GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/hornantenna/Dual_Polarization_Horn_Antenna_1.0_10.0GHz.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_newantenna": {

                "question": "Which Newantenna product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "ATT 3DB 2W SMA MF 6GHZ",
                        "value": "ATT 3DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_3DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 6DB 2W SMA MF 6GHZ",
                        "value": "ATT 6DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_6DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 5DB 2W SMA MF 6GHZ",
                        "value": "ATT 5DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_5DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 6DB 1W SMA MF 6GHZ",
                        "value": "ATT 6DB 1W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_6DB_1W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "magnetic base antenna 8 dbi",
                        "value": "magnetic base antenna 8 dbi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/magnetic_base_antenna_8_dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10W 10dB 6Ghz",
                        "value": "ATT 10W 10dB 6Ghz",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_10W_10dB_6Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "whip antenna rp mov 5dbi",
                        "value": "whip antenna rp mov 5dbi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/whip_antenna_rp_mov_5dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Yagi antenna 18 dbi",
                        "value": "Yagi antenna 18 dbi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/Yagi_antenna_18_dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 10dB 6Ghz",
                        "value": "ATT 1W 10dB 6Ghz",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_1W_10dB_6Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "whip antenna ra mov 3 dbi",
                        "value": "whip antenna ra mov 3 dbi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/whip_antenna_ra_mov_3_dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "28 dbi gps internal antenna",
                        "value": "28 dbi gps internal antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/newantenna/28_dbi_gps_internal_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 10DB 2W SMA MF 6GHZ",
                        "value": "ATT 10DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_10DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "whip antenna rp mov 3dbi",
                        "value": "whip antenna rp mov 3dbi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/whip_antenna_rp_mov_3dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1W 1dB 6Ghz",
                        "value": "ATT 1W 1dB 6Ghz",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/new_attenuator/ATT_1W_1dB_6Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 20DB 2W SMA MF 6GHZ",
                        "value": "ATT 20DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_20DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 3DB 1WSMA MF 6GHZ",
                        "value": "ATT 3DB 1WSMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_3DB_1WSMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 2DB 2W SMA MF 6GHZ",
                        "value": "ATT 2DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_2DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GSM STICKER ANTENNA 3DBI",
                        "value": "GSM STICKER ANTENNA 3DBI",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/GSM_STICKER_ANTENNA_3DBI.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 15DB 2W SMA MF 6GHZ",
                        "value": "ATT 15DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_15DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Omni Antenna 4dbi",
                        "value": "Omni Antenna 4dbi",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/Omni_Antenna_4dbi.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 30DB 2W SMA MF 6GHZ",
                        "value": "ATT 30DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_30DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 20W 10dB 3Ghz",
                        "value": "ATT 20W 10dB 3Ghz",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_20W_10dB_3Ghz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ATT 1DB 2W SMA MF 6GHZ",
                        "value": "ATT 1DB 2W SMA MF 6GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/newantenna/New_antenna/ATT_1DB_2W_SMA_MF_6GHZ.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_open_ended_waveguide_probes": {

                "question": "Which Open Ended Waveguide Probes product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Open Ended Waveguide Probes 26.5 40G",
                        "value": "Open Ended Waveguide Probes 26.5 40G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/Open_Ended_Waveguide_Probes/Open_Ended_Waveguide_Probes_26.5_40G.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Open Ended Waveguide Probes 50 65G 1.85",
                        "value": "Open Ended Waveguide Probes 50 65G 1.85",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/Open_Ended_Waveguide_Probes/Open_Ended_Waveguide_Probes_50_65G_1.85.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Open Ended Waveguide Probes 33 50G 2.4",
                        "value": "Open Ended Waveguide Probes 33 50G 2.4",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/Open_Ended_Waveguide_Probes/Open_Ended_Waveguide_Probes_33_50G_2.4.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Open Ended Waveguide Probes 18 26.5G",
                        "value": "Open Ended Waveguide Probes 18 26.5G",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/SYNERGY_5G_PRODUCT/Open_Ended_Waveguide_Probes/Open_Ended_Waveguide_Probes_18_26.5G.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_other_items": {

                "question": "Which Other Antennas Items product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "WHIP ANTENNA RA MOV 3DBI 2400Mhz WITH UFL",
                        "value": "WHIP ANTENNA RA MOV 3DBI 2400Mhz WITH UFL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/IBS/WHIP_ANTENNA_RA_MOV_3DBI_2400Mhz_WITH_UFL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "High rim rf component",
                        "value": "High rim rf component",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Connector_Adaptor/High_rim_rf_component.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Antenna",
                        "value": "Antenna",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Multiband Bi Directional LPDA Antenna",
                        "value": "Multiband Bi Directional LPDA Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/Multiband_Bi_Directional_LPDA_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1560 1620Mhz 8dbi OMNI ANTENNA",
                        "value": "1560 1620Mhz 8dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/1560_1620Mhz_8dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "410 485Mhz 3dbi OMNI ANTENNA",
                        "value": "410 485Mhz 3dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/410_485Mhz_3dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8DBI PANEL ANTENNA 700 3500MHz",
                        "value": "8DBI PANEL ANTENNA 700 3500MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/IBS/8DBI_PANEL_ANTENNA_700_3500MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1400 1499Mhz 6dbi OMNI ANTENNA",
                        "value": "1400 1499Mhz 6dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/1400_1499Mhz_6dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Hand-Formable Semi-Flexible Coaxial Cable BRV MHDCable",
                        "value": "Hand-Formable Semi-Flexible Coaxial Cable BRV MHDCable",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Group_Data_Sheet/Hand-Formable_Semi-Flexible_Coaxial_Cable_BRV_MHDCable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1160 1280Mhz 6dbi OMNI ANTENNA",
                        "value": "1160 1280Mhz 6dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/1160_1280Mhz_6dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "860 930Mhz 5dbi OMNI ANTENNA",
                        "value": "860 930Mhz 5dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/860_930Mhz_5dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2400 2500Mhz 8dbi OMNI ANTENNA",
                        "value": "2400 2500Mhz 8dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/2400_2500Mhz_8dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "fishing pole antenna",
                        "value": "fishing pole antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/fishing_pole_antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5700 5900Mhz 8dbi OMNI ANTENNA",
                        "value": "5700 5900Mhz 8dbi OMNI ANTENNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/omni_high_power/5700_5900Mhz_8dbi_OMNI_ANTENNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Omni Antenna 700-3500MHz",
                        "value": "Omni Antenna 700-3500MHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/IBS/Omni_Antenna_700-3500MHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "12 dBi LPDA Antenna",
                        "value": "12 dBi LPDA Antenna",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/12_dBi_LPDA_Antenna.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "IMG 20160518 WA0035 (1)",
                        "value": "IMG 20160518 WA0035 (1)",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Antenna/IMG_20160518_WA0035_(1).pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_panel_antenna": {

                "question": "Which PANEL Antenna product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "9DBI PANEL ANTENNA 700 2700MHZ",
                        "value": "9DBI PANEL ANTENNA 700 2700MHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Antenna/PANEL_ANTENNA/9DBI_PANEL_ANTENNA_700_2700MHZ.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "antennas_wave_guides": {

                "question": "Which Wave Guides product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "ST-2013 Microwave Labkit",
                        "value": "ST-2013 Microwave Labkit",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/ST-2013_Microwave_Labkit.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST-2003 Microwave Labkit",
                        "value": "ST-2003 Microwave Labkit",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/ST-2003_Microwave_Labkit.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST-2003m Microwave Kit",
                        "value": "ST-2003m Microwave Kit",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/ST-2003m_Microwave_Kit.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Which Waveguide product?
            # -------------------------------------------------

            "waveguides": {

                "question": "Which Waveguide product?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Dummy Load",
                        "value": "Dummy Load",
                        "next": "waveguides_dummy_load"
                    },

                    {
                        "text": "Wave Guides",
                        "value": "Wave Guides",
                        "next": "waveguides_wave_guides"
                    },

                    {
                        "text": "Waveguide",
                        "value": "Waveguide",
                        "next": "waveguides_waveguide"
                    }

                ]

            },

            "waveguides_dummy_load": {

                "question": "Which Dummy Load product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "waveguide dummy loads",
                        "value": "waveguide dummy loads",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Dummy_Load/waveguide_dummy_loads.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "waveguides_wave_guides": {

                "question": "Which Wave Guides product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Tapered Waveguide",
                        "value": "Tapered Waveguide",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Tapered_Waveguide.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide-tunable",
                        "value": "waveguide-tunable",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide-tunable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide-precision-rotary-vane-type",
                        "value": "waveguide-precision-rotary-vane-type",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide-precision-rotary-vane-type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Rotary Joints",
                        "value": "Waveguide Rotary Joints",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Waveguide_Rotary_Joints.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide-fixed",
                        "value": "waveguide-fixed",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide-fixed.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Phase Shifter",
                        "value": "Waveguide Phase Shifter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Waveguide_Phase_Shifter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Rotary SPDT",
                        "value": "Waveguide Rotary SPDT",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Waveguide_Rotary_SPDT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide-adjustable",
                        "value": "waveguide-adjustable",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide-adjustable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Turn table",
                        "value": "Waveguide Turn table",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Waveguide_Turn_table.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Frequency Meters waveguide Direct Reading type",
                        "value": "Frequency Meters waveguide Direct Reading type",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Frequency_Meters_waveguide_Direct_Reading_type.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "COAXIAL TO RECTANGULAR WAVEGUIDE",
                        "value": "COAXIAL TO RECTANGULAR WAVEGUIDE",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/COAXIAL_TO_RECTANGULAR_WAVEGUIDE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide E H Plane TEE",
                        "value": "Waveguide E H Plane TEE",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Waveguide_E_H_Plane_TEE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Tripod",
                        "value": "Waveguide Tripod",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/Waveguide_Tripod.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide Slotted Section With Probe Carrier",
                        "value": "waveguide Slotted Section With Probe Carrier",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide_Slotted_Section_With_Probe_Carrier.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide-variable",
                        "value": "waveguide-variable",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide-variable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "waveguide-matched detector Mount-fixed",
                        "value": "waveguide-matched detector Mount-fixed",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/UpCommingProducts/Wave_Guides/waveguide-matched_detector_Mount-fixed.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "waveguides_waveguide": {

                "question": "Which Waveguide product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "WR1800",
                        "value": "WR1800",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR1800.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR42",
                        "value": "WR42",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR42.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 430 TO N FEMALE ADAPTOR",
                        "value": "WR 430 TO N FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR_430_TO_N_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 62 TO TNC FEMALE ENDLAUNCH",
                        "value": "WR 62 TO TNC FEMALE ENDLAUNCH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/NEWWAVEGUIDE/WR_62_TO_TNC_FEMALE_ENDLAUNCH.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR34",
                        "value": "WR34",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR34.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR340",
                        "value": "WR340",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_bend/WR340.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR284 TO SMA FEMALE ADAPTOR",
                        "value": "WR284 TO SMA FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR284_TO_SMA_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Qoutation For Waveguide",
                        "value": "Qoutation For Waveguide",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Qoutation_For_Waveguide.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR112 to WR90",
                        "value": "WR112 to WR90",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR112_to_WR90.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "11",
                        "value": "11",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/11.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR90",
                        "value": "WR90",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR90.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR284",
                        "value": "WR284",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_bend/WR284.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR19 to WR15",
                        "value": "WR19 to WR15",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR19_to_WR15.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Plus Branch Connector",
                        "value": "Plus Branch Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Plus_Branch_Connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR229",
                        "value": "WR229",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_bend/WR229.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR62",
                        "value": "WR62",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR62.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR975",
                        "value": "WR975",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR975.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "T Branch Connector",
                        "value": "T Branch Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/T_Branch_Connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR112",
                        "value": "WR112",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_bend/WR112.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR650",
                        "value": "WR650",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR650.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR112 TO N FEMALE ADAPTOR",
                        "value": "WR112 TO N FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR112_TO_N_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "1",
                        "value": "1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 62 TO TNC MALE END LAUNCH",
                        "value": "WR 62 TO TNC MALE END LAUNCH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/NEWWAVEGUIDE/WR_62_TO_TNC_MALE_END_LAUNCH.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR2300",
                        "value": "WR2300",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR2300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "16",
                        "value": "16",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/16.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ESC 4 M ESC 4 F",
                        "value": "ESC 4 M ESC 4 F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/ESC_4_M_ESC_4_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR62 TO TNC FEMALE",
                        "value": "WR62 TO TNC FEMALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/NEWWAVEGUIDE/WR62_TO_TNC_FEMALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR229 to WR187",
                        "value": "WR229 to WR187",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR229_to_WR187.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Ku band Waveguide Single Channel Rotary Joint",
                        "value": "Ku band Waveguide Single Channel Rotary Joint",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Ku_band_Waveguide_Single_Channel_Rotary_Joint.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 28 WAVE GUIDE BAND H BAND",
                        "value": "WR 28 WAVE GUIDE BAND H BAND",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR_28_WAVE_GUIDE_BAND_H_BAND.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR284 to WR187",
                        "value": "WR284 to WR187",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR284_to_WR187.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR2100",
                        "value": "WR2100",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR2100.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3 way Branch Connector",
                        "value": "3 way Branch Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/3_way_Branch_Connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR187",
                        "value": "WR187",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_twist/WR187.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR34 to WR28",
                        "value": "WR34 to WR28",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR34_to_WR28.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR19",
                        "value": "WR19",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR19.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "7",
                        "value": "7",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/7.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR1150",
                        "value": "WR1150",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR1150.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ESC 4 UW M ESC 4 F",
                        "value": "ESC 4 UW M ESC 4 F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/ESC_4_UW_M_ESC_4_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR159",
                        "value": "WR159",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR159.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR15",
                        "value": "WR15",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_bend/WR15.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 28 WAVE GUIDE BAND E BAND",
                        "value": "WR 28 WAVE GUIDE BAND E BAND",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR_28_WAVE_GUIDE_BAND_E_BAND.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR510 to WR430",
                        "value": "WR510 to WR430",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR510_to_WR430.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR137 TO N FEMALE ADAPTOR",
                        "value": "WR137 TO N FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR137_TO_N_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR75 to WR90",
                        "value": "WR75 to WR90",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR75_to_WR90.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR28",
                        "value": "WR28",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR28.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 way Branch Connector",
                        "value": "2 way Branch Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/2_way_Branch_Connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR430",
                        "value": "WR430",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR430.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "5",
                        "value": "5",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/5.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR1500",
                        "value": "WR1500",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR1500.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST260WRSCFBP260",
                        "value": "ST260WRSCFBP260",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Waveguide_Rotatory_Joint/ST260WRSCFBP260.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "12",
                        "value": "12",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/12.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Flex Twist IEC EIA",
                        "value": "Flex Twist IEC EIA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Flex_Twist_IEC_EIA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR187 TO SMA FEMALE ADAPTOR",
                        "value": "WR187 TO SMA FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR187_TO_SMA_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 62 TO TNC MALE",
                        "value": "WR 62 TO TNC MALE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/NEWWAVEGUIDE/WR_62_TO_TNC_MALE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR22",
                        "value": "WR22",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR22.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST70WRSCFDP70",
                        "value": "ST70WRSCFDP70",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Waveguide_Rotatory_Joint/ST70WRSCFDP70.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "8",
                        "value": "8",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/8.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Directional Coupler WR284",
                        "value": "Directional Coupler WR284",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Directional_Coupler_WR284.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "ST220WRSCFBP220",
                        "value": "ST220WRSCFBP220",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Waveguide_Rotatory_Joint/ST220WRSCFBP220.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Broadwall Directional Coupler WR90",
                        "value": "Broadwall Directional Coupler WR90",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Broadwall_Directional_Coupler_WR90.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "WR430 to WR340",
                        "value": "WR430 to WR340",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR430_to_WR340.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR112 TO SMA FEMALE ADAPTOR",
                        "value": "WR112 TO SMA FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR112_TO_SMA_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST140WRSCFBP140",
                        "value": "ST140WRSCFBP140",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Waveguide_Rotatory_Joint/ST140WRSCFBP140.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "15",
                        "value": "15",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/15.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR187 TO N FEMALE ADAPTOR",
                        "value": "WR187 TO N FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR187_TO_N_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR770",
                        "value": "WR770",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR770.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR12 to WR10",
                        "value": "WR12 to WR10",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR12_to_WR10.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR159 to WR187",
                        "value": "WR159 to WR187",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR159_to_WR187.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR51",
                        "value": "WR51",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR51.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4",
                        "value": "4",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/4.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2",
                        "value": "2",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR 430 TO SMA FEMALE ADAPTOR",
                        "value": "WR 430 TO SMA FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR%20430_TO_SMA_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide High Power termination WR284",
                        "value": "Waveguide High Power termination WR284",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Waveguide_High_Power_termination_WR284.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "6",
                        "value": "6",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/6.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "9",
                        "value": "9",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/9.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR10",
                        "value": "WR10",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR10.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Beryllium Copper Finger Stock",
                        "value": "Beryllium Copper Finger Stock",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Beryllium_Copper_Finger_Stock.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR284 TO N FEMALE ADAPTOR",
                        "value": "WR284 TO N FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR284_TO_N_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST100WRHPFBP100",
                        "value": "ST100WRHPFBP100",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Waveguide_Rotatory_Joint/ST100WRHPFBP100.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR75 to WR62",
                        "value": "WR75 to WR62",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR75_to_WR62.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Flexible Twistable Waveguide For WR137",
                        "value": "Flexible Twistable Waveguide For WR137",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Flexible_Twistable_Waveguide_For_WR137.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR137",
                        "value": "WR137",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR137.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR340 to WR284",
                        "value": "WR340 to WR284",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR340_to_WR284.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Adaptor",
                        "value": "Waveguide Adaptor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Waveguide_Adaptor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR15 to WR12",
                        "value": "WR15 to WR12",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR15_to_WR12.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide twisted Adator WR112",
                        "value": "Waveguide twisted Adator WR112",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Waveguide_twisted_Adator_WR112.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "WR137 to WR112",
                        "value": "WR137 to WR112",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR137_to_WR112.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR159 to WR137",
                        "value": "WR159 to WR137",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR159_to_WR137.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR75",
                        "value": "WR75",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_twist/WR75.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3",
                        "value": "3",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/3.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Adator WR284",
                        "value": "Waveguide Adator WR284",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Waveguide_Adator_WR284.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "4 rail module junction box",
                        "value": "4 rail module junction box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/4_rail_module_junction_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "10",
                        "value": "10",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/10.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ESC 4 PM M ESC 4 PM F",
                        "value": "ESC 4 PM M ESC 4 PM F",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/ESC_4_PM_M_ESC_4_PM_F.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "13",
                        "value": "13",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/13.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "17",
                        "value": "17",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/17.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MW",
                        "value": "MW",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/MW.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Wavequide",
                        "value": "Wavequide",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wavequide.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR12",
                        "value": "WR12",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/WR12.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ST100WRDCFBP100",
                        "value": "ST100WRDCFBP100",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Waveguide_Rotatory_Joint/ST100WRDCFBP100.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR137 TO SMA FEMALE ADAPTOR",
                        "value": "WR137 TO SMA FEMALE ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR137_TO_SMA_FEMALE_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR770 to WR650",
                        "value": "WR770 to WR650",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR770_to_WR650.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Waveguide Adator WR112",
                        "value": "Waveguide Adator WR112",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/Waveguide_Adator_WR112.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "WR19 to WR22",
                        "value": "WR19 to WR22",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/waveguide_transition/WR19_to_WR22.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "WR510",
                        "value": "WR510",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Wave_Guide_Coaxial_Adaptor/WR510.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "flange dg",
                        "value": "flange dg",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/flange_dg.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "14",
                        "value": "14",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/14.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3 rail module junction box",
                        "value": "3 rail module junction box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/3_rail_module_junction_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 rail module junction box",
                        "value": "2 rail module junction box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/2_rail_module_junction_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Flex Twist for WR120 18GHz",
                        "value": "Flex Twist for WR120 18GHz",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Flex_Twist_for_WR120_18GHz.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Y Branch Connector",
                        "value": "Y Branch Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Waveguide/Y_Branch_Connector.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Which RF Adaptor?
            # -------------------------------------------------

            "rf_adaptors": {

                "question": "Which RF Adaptor?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "1.0 To 1.85",
                        "value": "1.0 To 1.85",
                        "next": "rf_adaptors_1_0_to_1_85"
                    },

                    {
                        "text": "1.0 To 2.4",
                        "value": "1.0 To 2.4",
                        "next": "rf_adaptors_1_0_to_2_4"
                    },

                    {
                        "text": "1.85 To 1.85",
                        "value": "1.85 To 1.85",
                        "next": "rf_adaptors_1_85_to_1_85"
                    },

                    {
                        "text": "1.85 To 2.4",
                        "value": "1.85 To 2.4",
                        "next": "rf_adaptors_1_85_to_2_4"
                    },

                    {
                        "text": "1.85 To 2.92",
                        "value": "1.85 To 2.92",
                        "next": "rf_adaptors_1_85_to_2_92"
                    },

                    {
                        "text": "1.85 To 3.5",
                        "value": "1.85 To 3.5",
                        "next": "rf_adaptors_1_85_to_3_5"
                    },

                    {
                        "text": "2.4 To 2.4",
                        "value": "2.4 To 2.4",
                        "next": "rf_adaptors_2_4_to_2_4"
                    },

                    {
                        "text": "2.4 To 2.92",
                        "value": "2.4 To 2.92",
                        "next": "rf_adaptors_2_4_to_2_92"
                    },

                    {
                        "text": "2.4 To 3.5",
                        "value": "2.4 To 3.5",
                        "next": "rf_adaptors_2_4_to_3_5"
                    },

                    {
                        "text": "2.92 To 2.92",
                        "value": "2.92 To 2.92",
                        "next": "rf_adaptors_2_92_to_2_92"
                    },

                    {
                        "text": "2.92 To SSMP",
                        "value": "2.92 To SSMP",
                        "next": "rf_adaptors_2_92_to_ssmp"
                    },

                    {
                        "text": "3.5 To 3.5",
                        "value": "3.5 To 3.5",
                        "next": "rf_adaptors_3_5_to_3_5"
                    },

                    {
                        "text": "N To 1.85",
                        "value": "N To 1.85",
                        "next": "rf_adaptors_n_to_1_85"
                    },

                    {
                        "text": "N To 2.4",
                        "value": "N To 2.4",
                        "next": "rf_adaptors_n_to_2_4"
                    },

                    {
                        "text": "N To 2.92",
                        "value": "N To 2.92",
                        "next": "rf_adaptors_n_to_2_92"
                    },

                    {
                        "text": "N To 3.5",
                        "value": "N To 3.5",
                        "next": "rf_adaptors_n_to_3_5"
                    },

                    {
                        "text": "N To N",
                        "value": "N To N",
                        "next": "rf_adaptors_n_to_n"
                    },

                    {
                        "text": "N To SMA",
                        "value": "N To SMA",
                        "next": "rf_adaptors_n_to_sma"
                    },

                    {
                        "text": "N To TNC",
                        "value": "N To TNC",
                        "next": "rf_adaptors_n_to_tnc"
                    },

                    {
                        "text": "Ntoc Adapter",
                        "value": "Ntoc Adapter",
                        "next": "rf_adaptors_ntoc_adapter"
                    },

                    {
                        "text": "Other Rf Adaptors Items",
                        "value": "Other Rf Adaptors Items",
                        "next": "rf_adaptors_other_items"
                    },

                    {
                        "text": "SMA To SMA",
                        "value": "SMA To SMA",
                        "next": "rf_adaptors_sma_to_sma"
                    }

                ]

            },

            "rf_adaptors_1_0_to_1_85": {

                "question": "Which 1.0 To 1.85 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.0 MALE TO 1.85 FEMALE ADPATOR",
                        "value": "1.0 MALE TO 1.85 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/1.0_To_1.85/1.0_MALE_TO_1.85_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_1_0_to_2_4": {

                "question": "Which 1.0 To 2.4 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.0 MALE TO 2.4 MALE ADPATOR",
                        "value": "1.0 MALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/1.0_To_2.4/1.0_MALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_1_85_to_1_85": {

                "question": "Which 1.85 To 1.85 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.85 MALE TO 1.85 FEMALE ADPATOR",
                        "value": "1.85 MALE TO 1.85 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/1.85_To_1.85/1.85_MALE_TO_1.85_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_1_85_to_2_4": {

                "question": "Which 1.85 To 2.4 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.85 MALE TO 2.4 MALE ADPATOR",
                        "value": "1.85 MALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/1.85_To_2.4/1.85_MALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_1_85_to_2_92": {

                "question": "Which 1.85 To 2.92 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.85 MALE TO 2.92 MALE ADPATOR",
                        "value": "1.85 MALE TO 2.92 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/1.85_To_2.92/1.85_MALE_TO_2.92_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_1_85_to_3_5": {

                "question": "Which 1.85 To 3.5 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "1.85 MALE TO 3.5 MALE ADPATOR",
                        "value": "1.85 MALE TO 3.5 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/1.85_To_3.5/1.85_MALE_TO_3.5_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_2_4_to_2_4": {

                "question": "Which 2.4 To 2.4 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2.4 MALE TO 2.4 FEMALE ADPATOR",
                        "value": "2.4 MALE TO 2.4 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_2.4/2.4_MALE_TO_2.4_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.4 MALE TO 2.4 MALE ADPATOR",
                        "value": "2.4 MALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_2.4/2.4_MALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.4 FEMALE TO 2.4 FEMALE ADPATOR",
                        "value": "2.4 FEMALE TO 2.4 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_2.4/2.4_FEMALE_TO_2.4_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_2_4_to_2_92": {

                "question": "Which 2.4 To 2.92 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2.92 FEMALE TO 2.4 MALE ADPATOR",
                        "value": "2.92 FEMALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_2.92/2.92_FEMALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO 2.4 MALE ADPATOR",
                        "value": "2.92 MALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_2.92/2.92_MALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO 2.4 FEMALE ADPATOR",
                        "value": "2.92 MALE TO 2.4 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_2.92/2.92_MALE_TO_2.4_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_2_4_to_3_5": {

                "question": "Which 2.4 To 3.5 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2.4 FEMALE TO 3.5 FEMALE ADPATOR",
                        "value": "2.4 FEMALE TO 3.5 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_3.5/2.4_FEMALE_TO_3.5_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.4 FEMALE TO 3.5 MALE ADPATOR",
                        "value": "2.4 FEMALE TO 3.5 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_3.5/2.4_FEMALE_TO_3.5_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.4 MALE TO 3.5 MALE ADPATOR",
                        "value": "2.4 MALE TO 3.5 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_3.5/2.4_MALE_TO_3.5_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.4 MALE TO 3.5 FEMALE ADPATOR",
                        "value": "2.4 MALE TO 3.5 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.4_To_3.5/2.4_MALE_TO_3.5_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_2_92_to_2_92": {

                "question": "Which 2.92 To 2.92 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2.92 FEMALE TO 2.92 FEMALE ADPATOR 4H",
                        "value": "2.92 FEMALE TO 2.92 FEMALE ADPATOR 4H",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_FEMALE_TO_2.92_FEMALE_ADPATOR_4H.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 FEMALE TO 2.92 FEMALE ADPATOR RA",
                        "value": "2.92 FEMALE TO 2.92 FEMALE ADPATOR RA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_FEMALE_TO_2.92_FEMALE_ADPATOR_RA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO 2.92 MALE ADPATOR RA",
                        "value": "2.92 MALE TO 2.92 MALE ADPATOR RA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_MALE_TO_2.92_MALE_ADPATOR_RA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 FEMALE TO 2.92 FEMALE ADPATOR",
                        "value": "2.92 FEMALE TO 2.92 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_FEMALE_TO_2.92_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO 2.92 FEMALE ADPATOR",
                        "value": "2.92 MALE TO 2.92 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_MALE_TO_2.92_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO 2.92 MALE ADPATOR",
                        "value": "2.92 MALE TO 2.92 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_MALE_TO_2.92_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO 2.92 FEMALE ADPATOR RA",
                        "value": "2.92 MALE TO 2.92 FEMALE ADPATOR RA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_MALE_TO_2.92_FEMALE_ADPATOR_RA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 FEMALE TO 2.92 FEMALE ADPATOR BH",
                        "value": "2.92 FEMALE TO 2.92 FEMALE ADPATOR BH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_2.92/2.92_FEMALE_TO_2.92_FEMALE_ADPATOR_BH.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_2_92_to_ssmp": {

                "question": "Which 2.92 To SSMP product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "2.92 FEMALE TO SSMP MALE ADPATOR",
                        "value": "2.92 FEMALE TO SSMP MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_SSMP/2.92_FEMALE_TO_SSMP_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 FEMALE TO SSMP FEMALE ADPATOR",
                        "value": "2.92 FEMALE TO SSMP FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_SSMP/2.92_FEMALE_TO_SSMP_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2.92 MALE TO SSMP FEMALE ADPATOR",
                        "value": "2.92 MALE TO SSMP FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/2.92_To_SSMP/2.92_MALE_TO_SSMP_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_3_5_to_3_5": {

                "question": "Which 3.5 To 3.5 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "3.5 MALE TO 3.5 FEMALE ADPATOR",
                        "value": "3.5 MALE TO 3.5 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/3.5_To_3.5/3.5_MALE_TO_3.5_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3.5 MALE TO 3.5 FEMALE ADPATOR BH",
                        "value": "3.5 MALE TO 3.5 FEMALE ADPATOR BH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/3.5_To_3.5/3.5_MALE_TO_3.5_FEMALE_ADPATOR_BH.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3.5 MALE TO 3.5 MALE ADPATOR",
                        "value": "3.5 MALE TO 3.5 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/3.5_To_3.5/3.5_MALE_TO_3.5_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3.5 FEMALE TO 3.5 FEMALE ADPATOR",
                        "value": "3.5 FEMALE TO 3.5 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/3.5_To_3.5/3.5_FEMALE_TO_3.5_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3.5 FEMALE TO 3.5 FEMALE ADPATOR BH",
                        "value": "3.5 FEMALE TO 3.5 FEMALE ADPATOR BH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/3.5_To_3.5/3.5_FEMALE_TO_3.5_FEMALE_ADPATOR_BH.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_1_85": {

                "question": "Which N To 1.85 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N MALE TO 1.85 FEMALE ADPATOR",
                        "value": "N MALE TO 1.85 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_1.85/N_MALE_TO_1.85_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_2_4": {

                "question": "Which N To 2.4 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N FEMALE TO 2.4 FEMALE ADPATOR",
                        "value": "N FEMALE TO 2.4 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.4/N_FEMALE_TO_2.4_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO 2.4 FEMALE ADPATOR",
                        "value": "N MALE TO 2.4 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.4/N_MALE_TO_2.4_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO 2.4 MALE ADPATOR",
                        "value": "N MALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.4/N_MALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO 2.4 MALE ADPATOR",
                        "value": "N FEMALE TO 2.4 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.4/N_FEMALE_TO_2.4_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_2_92": {

                "question": "Which N To 2.92 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N MALE TO 2.92 FEMALE ADPATOR",
                        "value": "N MALE TO 2.92 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.92/N_MALE_TO_2.92_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO 2.92 MALE ADPATOR",
                        "value": "N MALE TO 2.92 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.92/N_MALE_TO_2.92_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO 2.92 MALE ADPATOR",
                        "value": "N FEMALE TO 2.92 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.92/N_FEMALE_TO_2.92_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO 2.92 FEMALE ADPATOR",
                        "value": "N FEMALE TO 2.92 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_2.92/N_FEMALE_TO_2.92_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_3_5": {

                "question": "Which N To 3.5 product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N MALE TO 3.5 MALE ADPATOR",
                        "value": "N MALE TO 3.5 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_3.5/N_MALE_TO_3.5_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO 3.5 MALE ADPATOR",
                        "value": "N FEMALE TO 3.5 MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_3.5/N_FEMALE_TO_3.5_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO 3.5 FEMALE ADPATOR",
                        "value": "N MALE TO 3.5 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_3.5/N_MALE_TO_3.5_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO 3.5 FEMALE ADPATOR",
                        "value": "N FEMALE TO 3.5 FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_3.5/N_FEMALE_TO_3.5_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_n": {

                "question": "Which N To N product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N MALE TO N FEMALE ADPATOR",
                        "value": "N MALE TO N FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_N/N_MALE_TO_N_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO N FEMALE ADPATOR 4H",
                        "value": "N FEMALE TO N FEMALE ADPATOR 4H",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_N/N_FEMALE_TO_N_FEMALE_ADPATOR_4H.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO N FEMALE ADPATOR",
                        "value": "N FEMALE TO N FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_N/N_FEMALE_TO_N_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO N MALE ADPATOR",
                        "value": "N MALE TO N MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_N/N_MALE_TO_N_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO N FEMALE ADPATOR BH",
                        "value": "N FEMALE TO N FEMALE ADPATOR BH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_N/N_FEMALE_TO_N_FEMALE_ADPATOR_BH.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_sma": {

                "question": "Which N To SMA product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N FEMALE TO SMA FEMALE ADPATOR BH",
                        "value": "N FEMALE TO SMA FEMALE ADPATOR BH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_SMA/N_FEMALE_TO_SMA_FEMALE_ADPATOR_BH.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO SMA MALE ADPATOR",
                        "value": "N FEMALE TO SMA MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_SMA/N_FEMALE_TO_SMA_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO SMA MALE ADPATOR",
                        "value": "N MALE TO SMA MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_SMA/N_MALE_TO_SMA_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO SMA FEMALE ADPATOR 4H",
                        "value": "N FEMALE TO SMA FEMALE ADPATOR 4H",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_SMA/N_FEMALE_TO_SMA_FEMALE_ADPATOR_4H.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO SMA FEMALE ADPATOR",
                        "value": "N MALE TO SMA FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_SMA/N_MALE_TO_SMA_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO SMA FEMALE ADPATOR",
                        "value": "N FEMALE TO SMA FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_SMA/N_FEMALE_TO_SMA_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_n_to_tnc": {

                "question": "Which N To TNC product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N MALE TO TNC FEMALE ADPATOR",
                        "value": "N MALE TO TNC FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_TNC/N_MALE_TO_TNC_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO TNC FEMALE ADPATOR",
                        "value": "N FEMALE TO TNC FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_TNC/N_FEMALE_TO_TNC_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N FEMALE TO TNC MALE ADPATOR",
                        "value": "N FEMALE TO TNC MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_TNC/N_FEMALE_TO_TNC_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N MALE TO TNC MALE ADPATOR",
                        "value": "N MALE TO TNC MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/N_To_TNC/N_MALE_TO_TNC_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_ntoc_adapter": {

                "question": "Which Ntoc Adapter product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "N F to C M Adapter",
                        "value": "N F to C M Adapter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/adaptor/NtoC_adapter/N_F_to_C_M_Adapter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N M to C F Adapter",
                        "value": "N M to C F Adapter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/adaptor/NtoC_adapter/N_M_to_C_F_Adapter.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_other_items": {

                "question": "Which Other Rf Adaptors Items product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMZ M SMZ M ADAPTER",
                        "value": "SMZ M SMZ M ADAPTER",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/SMZ_M_SMZ_M_ADAPTER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MINIDIN M TO DIN F ADAPTOR",
                        "value": "MINIDIN M TO DIN F ADAPTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/MINIDIN_M_TO_DIN_F_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M SMA F Adaptor 18GHZ",
                        "value": "SMA M SMA F Adaptor 18GHZ",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/SMA_M_SMA_F_Adaptor_18GHZ.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M SMA F RA ADAPTOR",
                        "value": "SMA M SMA F RA ADAPTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/SMA_M_SMA_F_RA_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC m SMA f adapter",
                        "value": "TNC m SMA f adapter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/TNC_m_SMA_f_adapter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N m UHF f adapter",
                        "value": "N m UHF f adapter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/N_m_UHF_f_adapter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F BNC F Adaptor",
                        "value": "N F BNC F Adaptor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/adaptor/N_F_BNC_F_Adaptor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BNC F SMA F ADAPTOR",
                        "value": "BNC F SMA F ADAPTOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/adaptor/BNC_F_SMA_F_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "tnc f sma m adapter",
                        "value": "tnc f sma m adapter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/tnc_f_sma_m_adapter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC M SMA F RP ADAPTOR",
                        "value": "TNC M SMA F RP ADAPTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/TNC_M_SMA_F_RP_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4.3 10 Female to N Male Adaptor",
                        "value": "4.3 10 Female to N Male Adaptor",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/4.3_10_Female_to_N_Male_Adaptor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA M N F ADAPTOR",
                        "value": "SMA M N F ADAPTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/SMA_M_N_F_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4.3 10 Male to N Female Connector",
                        "value": "4.3 10 Male to N Female Connector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Adaptor_Pic/4.3_10_Male_to_N_Female_Connector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TNC f SMA f ADAPTOR",
                        "value": "TNC f SMA f ADAPTOR",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/TNC_f_SMA_f_ADAPTOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4.3 10 Male Connector to N Female Connector Adaptor",
                        "value": "4.3 10 Male Connector to N Female Connector Adaptor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Adaptor_Pic/4.3_10_Male_Connector_to_N_Female_Connector_Adaptor.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "tnc f tnc f bh adapter",
                        "value": "tnc f tnc f bh adapter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/adaptor/tnc_f_tnc_f_bh_adapter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "N F BNC M Adaptor",
                        "value": "N F BNC M Adaptor",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/adaptor/N_F_BNC_M_Adaptor.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "rf_adaptors_sma_to_sma": {

                "question": "Which SMA To SMA product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SMA FEMALE TO SMA FEMALE ADPATOR 4H",
                        "value": "SMA FEMALE TO SMA FEMALE ADPATOR 4H",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_FEMALE_TO_SMA_FEMALE_ADPATOR_4H.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA MALE TO SMA FEMALE ADPATOR RA",
                        "value": "SMA MALE TO SMA FEMALE ADPATOR RA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_MALE_TO_SMA_FEMALE_ADPATOR_RA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA MALE TO SMA FEMALE ADPATOR",
                        "value": "SMA MALE TO SMA FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_MALE_TO_SMA_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA MALE TO SMA MALE ADPATOR",
                        "value": "SMA MALE TO SMA MALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_MALE_TO_SMA_MALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA FEMALE TO SMA FEMALE ADPATOR",
                        "value": "SMA FEMALE TO SMA FEMALE ADPATOR",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_FEMALE_TO_SMA_FEMALE_ADPATOR.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA MALE TO SMA MALE ADPATOR RA",
                        "value": "SMA MALE TO SMA MALE ADPATOR RA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_MALE_TO_SMA_MALE_ADPATOR_RA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMA FEMALE TO SMA FEMALE ADPATOR RA",
                        "value": "SMA FEMALE TO SMA FEMALE ADPATOR RA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/High_Frequency_Adapter/SMA_To_SMA/SMA_FEMALE_TO_SMA_FEMALE_ADPATOR_RA.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Which Installation product?
            # -------------------------------------------------

            "installation_tools": {

                "question": "Which Installation product?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Aviation Light",
                        "value": "Aviation Light",
                        "next": "installation_tools_aviation_light"
                    },

                    {
                        "text": "Crimping Tool",
                        "value": "Crimping Tool",
                        "next": "installation_tools_crimping_tool"
                    },

                    {
                        "text": "Earthing Kit",
                        "value": "Earthing Kit",
                        "next": "installation_tools_earthing_kit"
                    },

                    {
                        "text": "Entry Plate",
                        "value": "Entry Plate",
                        "next": "installation_tools_entry_plate"
                    },

                    {
                        "text": "Feeder Clamp",
                        "value": "Feeder Clamp",
                        "next": "installation_tools_feeder_clamp"
                    },

                    {
                        "text": "Hand Tools",
                        "value": "Hand Tools",
                        "next": "installation_tools_hand_tools"
                    },

                    {
                        "text": "Hosting Grip",
                        "value": "Hosting Grip",
                        "next": "installation_tools_hosting_grip"
                    },

                    {
                        "text": "Multi Purpose",
                        "value": "Multi Purpose",
                        "next": "installation_tools_multi_purpose"
                    },

                    {
                        "text": "Optical TOOL KIT",
                        "value": "Optical TOOL KIT",
                        "next": "installation_tools_optical_tool_kit"
                    },

                    {
                        "text": "Other Installation Tools Items",
                        "value": "Other Installation Tools Items",
                        "next": "installation_tools_other_items"
                    },

                    {
                        "text": "Safety BELT",
                        "value": "Safety BELT",
                        "next": "installation_tools_safety_belt"
                    },

                    {
                        "text": "Telecom Purpose",
                        "value": "Telecom Purpose",
                        "next": "installation_tools_telecom_purpose"
                    },

                    {
                        "text": "Weather Proofing Kit",
                        "value": "Weather Proofing Kit",
                        "next": "installation_tools_weather_proofing_kit"
                    }

                ]

            },

            "installation_tools_aviation_light": {

                "question": "Which Aviation Light product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Aviation Light",
                        "value": "Aviation Light",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Aviation_Light/Aviation_Light.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_crimping_tool": {

                "question": "Which Crimping Tool product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "CRIMPIMG TOOL RG174",
                        "value": "CRIMPIMG TOOL RG174",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Crimping_Tool/CRIMPIMG_TOOL_RG174.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_earthing_kit": {

                "question": "Which Earthing Kit product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Grounding Kit For 7 8 Clip",
                        "value": "Grounding Kit For 7 8 Clip",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Earthing_Kit/Grounding_Kit_For_7_8_Clip.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Grouding Bar",
                        "value": "Grouding Bar",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Earthing_Kit/Grouding_Bar.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_entry_plate": {

                "question": "Which Entry Plate product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "4 BOOT 4 hols for 7 8 1 2 cable hose clamp",
                        "value": "4 BOOT 4 hols for 7 8 1 2 cable hose clamp",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Entry_Plate/4_BOOT_4_hols_for_7_8_1_2_cable_hose_clamp.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "4 way hutch plate for 7 8 1 2",
                        "value": "4 way hutch plate for 7 8 1 2",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Entry_Plate/4_way_hutch_plate_for_7_8_1_2.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_feeder_clamp": {

                "question": "Which Feeder Clamp product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "6 WAY FEEDER CLAMP BS 1 5 8",
                        "value": "6 WAY FEEDER CLAMP BS 1 5 8",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Feeder_Clamp/6_WAY_FEEDER_CLAMP_BS_1_5_8.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "3 WAY FEEDER CLAMP SS 1 1 4",
                        "value": "3 WAY FEEDER CLAMP SS 1 1 4",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Feeder_Clamp/3_WAY_FEEDER_CLAMP_SS_1_1_4.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "2 WAY FEEDER CLAMP BS 1 2",
                        "value": "2 WAY FEEDER CLAMP BS 1 2",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Feeder_Clamp/2_WAY_FEEDER_CLAMP_BS_1_2.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_hand_tools": {

                "question": "Which Hand Tools product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "GRD 95 ring",
                        "value": "GRD 95 ring",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/GRD_95_ring.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SAGAR 400",
                        "value": "SAGAR 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/SAGAR_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Cutting Tools 1 2 7 8 Cable",
                        "value": "Cutting Tools 1 2 7 8 Cable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Cutting_Tools_1_2_7_8_Cable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BHOOMI 400",
                        "value": "BHOOMI 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/BHOOMI_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TRISHUL 3 IN 1",
                        "value": "TRISHUL 3 IN 1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/TRISHUL_3_IN_1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GARMIN GPS 585 COMBO",
                        "value": "GARMIN GPS 585 COMBO",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/GARMIN_GPS_585_COMBO.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "JAGUAR SERIES",
                        "value": "JAGUAR SERIES",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/JAGUAR_SERIES.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GRD 95 Hexagonal",
                        "value": "GRD 95 Hexagonal",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/GRD_95_Hexagonal.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TRISHAKTI",
                        "value": "TRISHAKTI",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/TRISHAKTI.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "garmin rino 750",
                        "value": "garmin rino 750",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/garmin_rino_750.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "virat 6",
                        "value": "virat 6",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/virat_6.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "yukon night vision binocular",
                        "value": "yukon night vision binocular",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/yukon_night_vision_binocular.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CUDDEBACK C1 CAMERA TRAP",
                        "value": "CUDDEBACK C1 CAMERA TRAP",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/CUDDEBACK_C1_CAMERA_TRAP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 45mm ACSR Cable Cutter DDQ45",
                        "value": "Max 45mm ACSR Cable Cutter DDQ45",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_45mm_ACSR_Cable_Cutter_DDQ45.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GARMIN GPS MAP 78s",
                        "value": "GARMIN GPS MAP 78s",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/GARMIN_GPS_MAP_78s.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HPCT 150A HEXAGONAL",
                        "value": "HPCT 150A HEXAGONAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/HPCT_150A_HEXAGONAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 100mmCuorAl Armored Cable Cutter DDQ100",
                        "value": "Max 100mmCuorAl Armored Cable Cutter DDQ100",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_100mmCuorAl_Armored_Cable_Cutter_DDQ100.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 45mm ACSR Cable Cutter DDQ45A",
                        "value": "Max 45mm ACSR Cable Cutter DDQ45A",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_45mm_ACSR_Cable_Cutter_DDQ45A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DISTO TM D2",
                        "value": "DISTO TM D2",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/DISTO_TM_D2.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "garmin montana 680",
                        "value": "garmin montana 680",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/garmin_montana_680.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CHETAK 16",
                        "value": "CHETAK 16",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/CHETAK_16.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "AGNNE 95",
                        "value": "AGNNE 95",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/AGNNE_95.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 30 mm ACSR Cable Cutter DDQ30A",
                        "value": "Max 30 mm ACSR Cable Cutter DDQ30A",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_30_mm_ACSR_Cable_Cutter_DDQ30A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "AAKASH 400 AAKASH 500",
                        "value": "AAKASH 400 AAKASH 500",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/AAKASH_400_AAKASH_500.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 100mmCu or Al Armored Cable Cutter J10",
                        "value": "Max 100mmCu or Al Armored Cable Cutter J10",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_100mmCu_or_Al_Armored_Cable_Cutter_J10.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "KOIZUMI PLACOM Kp 90 PLANIMETER",
                        "value": "KOIZUMI PLACOM Kp 90 PLANIMETER",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/KOIZUMI_PLACOM_Kp_90_PLANIMETER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RECONYX HC500 CAMERA TRAP",
                        "value": "RECONYX HC500 CAMERA TRAP",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/RECONYX_HC500_CAMERA_TRAP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "leica NA300",
                        "value": "leica NA300",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/leica_NA300.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GARMIN ETREX 10",
                        "value": "GARMIN ETREX 10",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/GARMIN_ETREX_10.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ysi pro dss parameter",
                        "value": "ysi pro dss parameter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/ysi_pro_dss_parameter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GARMIN GPS 12H",
                        "value": "GARMIN GPS 12H",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/GARMIN_GPS_12H.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 30mm Cu or Al cable Cutter VC30A",
                        "value": "Max 30mm Cu or Al cable Cutter VC30A",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_30mm_Cu_or_Al_cable_Cutter_VC30A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "garmin oregin 750",
                        "value": "garmin oregin 750",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/garmin_oregin_750.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HPCT 150A RING",
                        "value": "HPCT 150A RING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/HPCT_150A_RING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "OREGON FISHFINDER 350C",
                        "value": "OREGON FISHFINDER 350C",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/OREGON_FISHFINDER_350C.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CHAKRA 6",
                        "value": "CHAKRA 6",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/CHAKRA_6.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "EKLOVYA 120",
                        "value": "EKLOVYA 120",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/EKLOVYA_120.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "VIKRANT 50",
                        "value": "VIKRANT 50",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/VIKRANT_50.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HPCT 150B HEXAGONAL",
                        "value": "HPCT 150B HEXAGONAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/HPCT_150B_HEXAGONAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "LIFE STRAW",
                        "value": "LIFE STRAW",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/LIFE_STRAW.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "vectronic radio collar",
                        "value": "vectronic radio collar",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/vectronic_radio_collar.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ARJUN 50",
                        "value": "ARJUN 50",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/ARJUN_50.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "PRITHVI 1000",
                        "value": "PRITHVI 1000",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/PRITHVI_1000.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HPCT 150B RING",
                        "value": "HPCT 150B RING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/HPCT_150B_RING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GRD 185 HEXAGONAL",
                        "value": "GRD 185 HEXAGONAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/GRD_185_HEXAGONAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIGITAL WATER VELOCITY METER",
                        "value": "DIGITAL WATER VELOCITY METER",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/DIGITAL_WATER_VELOCITY_METER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SHAKTI 400",
                        "value": "SHAKTI 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/SHAKTI_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HAWKE LRF Pro 400 Metres",
                        "value": "HAWKE LRF Pro 400 Metres",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/HAWKE_LRF_Pro_400_Metres.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CUDDEBACK E2 IR CAMERA TRAP",
                        "value": "CUDDEBACK E2 IR CAMERA TRAP",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/CUDDEBACK_E2_IR_CAMERA_TRAP.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TEJAS 630",
                        "value": "TEJAS 630",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/TEJAS_630.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "coast light",
                        "value": "coast light",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/coast_light.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 55mm Cu or Al Armored Cable Cutter DDQ55",
                        "value": "Max 55mm Cu or Al Armored Cable Cutter DDQ55",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_55mm_Cu_or_Al_Armored_Cable_Cutter_DDQ55.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "rubber mastic tape",
                        "value": "rubber mastic tape",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/rubber_mastic_tape.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SPIDER 6",
                        "value": "SPIDER 6",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/SPIDER_6.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "leica total solution",
                        "value": "leica total solution",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/leica_total_solution.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CUDDEBACK E3 BLACK FLASH",
                        "value": "CUDDEBACK E3 BLACK FLASH",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/CUDDEBACK_E3_BLACK_FLASH.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HPCT20A HPCT20B",
                        "value": "HPCT20A HPCT20B",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/HPCT20A_HPCT20B.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "LUCI INFLATABLE SOLAR LIGHT",
                        "value": "LUCI INFLATABLE SOLAR LIGHT",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/LUCI_INFLATABLE_SOLAR_LIGHT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "VARUN 400",
                        "value": "VARUN 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/VARUN_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 130mm Cu or Al Armored Cable Cutter J130",
                        "value": "Max 130mm Cu or Al Armored Cable Cutter J130",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_130mm_Cu_or_Al_Armored_Cable_Cutter_J130.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 30mm ACSR Cable Cutter DDQ30",
                        "value": "Max 30mm ACSR Cable Cutter DDQ30",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_30mm_ACSR_Cable_Cutter_DDQ30.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "jop 427",
                        "value": "jop 427",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/jop_427.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SANGRAM 400 HEXAGONAL",
                        "value": "SANGRAM 400 HEXAGONAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/SANGRAM_400_HEXAGONAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 36mm Cu or Al cable Cutter VC36A",
                        "value": "Max 36mm Cu or Al cable Cutter VC36A",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_36mm_Cu_or_Al_cable_Cutter_VC36A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Hand Tools",
                        "value": "Hand Tools",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Hand_Tools.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 55mm Cu or Al Armored Cable Cutter DDQ55A",
                        "value": "Max 55mm Cu or Al Armored Cable Cutter DDQ55A",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_55mm_Cu_or_Al_Armored_Cable_Cutter_DDQ55A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CHAKRA 16",
                        "value": "CHAKRA 16",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/CHAKRA_16.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SURYA 400 HEXAGONAL",
                        "value": "SURYA 400 HEXAGONAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/SURYA_400_HEXAGONAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "HOBO U 23 01",
                        "value": "HOBO U 23 01",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/HOBO_U_23_01.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Ground penetrating radar",
                        "value": "Ground penetrating radar",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Ground_penetrating_radar.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GRD 185 RING",
                        "value": "GRD 185 RING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/GRD_185_RING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TIGER SERIES",
                        "value": "TIGER SERIES",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/TIGER_SERIES.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CHETAK 6",
                        "value": "CHETAK 6",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/CHETAK_6.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "pvc tape",
                        "value": "pvc tape",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/pvc_tape.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "LUV KUSH 6",
                        "value": "LUV KUSH 6",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/LUV_KUSH_6.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 30mm Cu Al cable Cutter D240",
                        "value": "Max 30mm Cu Al cable Cutter D240",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_30mm_Cu_Al_cable_Cutter_D240.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 40mm Cu or Al cable Cutter D500",
                        "value": "Max 40mm Cu or Al cable Cutter D500",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_40mm_Cu_or_Al_cable_Cutter_D500.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "garmin gps etrex 20x",
                        "value": "garmin gps etrex 20x",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/garmin_gps_etrex_20x.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "GARMIN GPS MAP 64s",
                        "value": "GARMIN GPS MAP 64s",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/GARMIN_GPS_MAP_64s.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "VISHAL 185 RING",
                        "value": "VISHAL 185 RING",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/VISHAL_185_RING.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "AUTOMATIC WEATHER STATION",
                        "value": "AUTOMATIC WEATHER STATION",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/AUTOMATIC_WEATHER_STATION.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Max 60mm Cu or Al cable Cutter VC60A",
                        "value": "Max 60mm Cu or Al cable Cutter VC60A",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/Max_60mm_Cu_or_Al_cable_Cutter_VC60A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ASHOKA 400",
                        "value": "ASHOKA 400",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/other_compressiontool/ASHOKA_400.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ESTWING Geological Hammer",
                        "value": "ESTWING Geological Hammer",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Tools/Hand_Tools/ESTWING_Geological_Hammer.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "simrat 16",
                        "value": "simrat 16",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Hand_Tools/Compression_tools/simrat_16.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_hosting_grip": {

                "question": "Which Hosting Grip product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Hoisting Grip lace up",
                        "value": "Hoisting Grip lace up",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Hosting_Grip/Hoisting_Grip_lace_up.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Hoisting Grip pre laced",
                        "value": "Hoisting Grip pre laced",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Microwave_components/Hosting_Grip/Hoisting_Grip_pre_laced.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_multi_purpose": {

                "question": "Which Multi Purpose product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Compact Tool Kit 9 Pc",
                        "value": "Compact Tool Kit 9 Pc",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Multi_Purpose/Compact_Tool_Kit_9_Pc.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Jumbo Tool Kit",
                        "value": "Jumbo Tool Kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Multi_Purpose/Jumbo_Tool_Kit.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_optical_tool_kit": {

                "question": "Which Optical TOOL KIT product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Anaerobic tool kit ST6011FT",
                        "value": "Anaerobic tool kit ST6011FT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/OPTICAL_TOOL_KIT/Anaerobic_tool_kit_ST6011FT.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_other_items": {

                "question": "Which Other Installation Tools Items product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "KRONE HIGHBAND 8 AND 10 Pair Disconnection Module",
                        "value": "KRONE HIGHBAND 8 AND 10 Pair Disconnection Module",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Krone/KRONE_HIGHBAND_8_AND_10_Pair_Disconnection_Module.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 10",
                        "value": "YFTL 10",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_10.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN CABLE LUG",
                        "value": "DIN CABLE LUG",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/DIN_CABLE_LUG.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "TL MTK TYPE SHORT FULL INSULATING MIDDLE JOINT",
                        "value": "TL MTK TYPE SHORT FULL INSULATING MIDDLE JOINT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/TL_MTK_TYPE_SHORT_FULL_INSULATING_MIDDLE_JOINT.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "CABLE LUG FOR JM TYPE",
                        "value": "CABLE LUG FOR JM TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CABLE_LUG_FOR_JM_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 12",
                        "value": "YFTL 12",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_12.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTLOS 04",
                        "value": "YFTLOS 04",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTLOS_04.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CIRCUIT BREAKER LUG",
                        "value": "CIRCUIT BREAKER LUG",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CIRCUIT_BREAKER_LUG.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "DTGA TYPE COPPER TERMINAL FIRST GLIMPSE OF THE MOUTH",
                        "value": "DTGA TYPE COPPER TERMINAL FIRST GLIMPSE OF THE MOUTH",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/DTGA_TYPE_COPPER_TERMINAL_FIRST_GLIMPSE_OF_THE_MOUTH.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "aviation warning lamps",
                        "value": "aviation warning lamps",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/aviation_warning_lamps.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "ALUMINIUM LUG",
                        "value": "ALUMINIUM LUG",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/ALUMINIUM_LUG.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL OS02",
                        "value": "YFTL OS02",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_OS02.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFL OS01",
                        "value": "YFL OS01",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFL_OS01.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Dual Wall Heat Shrink Tubing 3 1 ratio or 4 1 ratio",
                        "value": "Dual Wall Heat Shrink Tubing 3 1 ratio or 4 1 ratio",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Dual_Wall_Heat_Shrink_Tubing_3_1_ratio_or_4_1_ratio.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Semi Conductive tubing BDWT 36kv",
                        "value": "Semi Conductive tubing BDWT 36kv",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Semi_Conductive_tubing_BDWT_36kv.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Andrew Cutter For Aluminium Cable 78-HPT",
                        "value": "Andrew Cutter For Aluminium Cable 78-HPT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/Andrew_Cutter_For_Aluminium_Cable_78-HPT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TU TYPE FORK BARE ENDS",
                        "value": "TU TYPE FORK BARE ENDS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/TU_TYPE_FORK_BARE_ENDS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TU MTF TYPE FORK PRE INSULATING TERMINAL",
                        "value": "TU MTF TYPE FORK PRE INSULATING TERMINAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/TU_MTF_TYPE_FORK_PRE_INSULATING_TERMINAL.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "CABLE LUG FOR JM JGY TYPE",
                        "value": "CABLE LUG FOR JM JGY TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CABLE_LUG_FOR_JM_JGY_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "KRONE LSA PLUS DISCONNECTION MODULE",
                        "value": "KRONE LSA PLUS DISCONNECTION MODULE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Krone/KRONE_LSA_PLUS_DISCONNECTION_MODULE.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 06",
                        "value": "YFTL 06",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_06.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Roxtec Comseal 10 16 32 Product news EN",
                        "value": "Roxtec Comseal 10 16 32 Product news EN",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Roxtec_Comseal/Roxtec_Comseal_10_16_32_Product_news_EN.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Medium Wall HST with without hot melt adhesive",
                        "value": "Medium Wall HST with without hot melt adhesive",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Medium_Wall_HST_with_without_hot_melt_adhesive.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTLOS 03",
                        "value": "YFTLOS 03",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTLOS%20_03.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BIMETAL LUG ATL TYPE",
                        "value": "BIMETAL LUG ATL TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BIMETAL_LUG_ATL_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "BOLTED BRASS LUG WCMC TYPE",
                        "value": "BOLTED BRASS LUG WCMC TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BOLTED_BRASS_LUG_WCMC_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "Halogen free busbar insulation tubing BBTH 36kv",
                        "value": "Halogen free busbar insulation tubing BBTH 36kv",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Halogen_free_busbar_insulation_tubing_BBTH_36kv.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 13",
                        "value": "YFTL 13",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_13.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CABLE LUG FOR JM JGR TYPE",
                        "value": "CABLE LUG FOR JM JGR TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CABLE_LUG_FOR_JM_JGR_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "TO MTF TYPE CIRCULAR PRE INSTALING TERMINAL",
                        "value": "TO MTF TYPE CIRCULAR PRE INSTALING TERMINAL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/TO_MTF_TYPE_CIRCULAR_PRE_INSTALING_TERMINAL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "FEMALE PRE INSULATING JOINT",
                        "value": "FEMALE PRE INSULATING JOINT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/FEMALE_PRE_INSULATING_JOINT.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "Stress Control Tubing BSC 100 20kv",
                        "value": "Stress Control Tubing BSC 100 20kv",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Stress_Control_Tubing_BSC_100_20kv.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BIMETAL LUG DTL TYPE",
                        "value": "BIMETAL LUG DTL TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BIMETAL_LUG_DTL_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "CUTTING TOOL",
                        "value": "CUTTING TOOL",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/CUTTING_TOOL.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MALE PRE INSULATING JOINT",
                        "value": "MALE PRE INSULATING JOINT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/MALE_PRE_INSULATING_JOINT.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "high voltage insulating jacketing tape",
                        "value": "high voltage insulating jacketing tape",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/high_voltage_insulating_jacketing_tape.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 09",
                        "value": "YFTL 09",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_09.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 02",
                        "value": "YFTL 02",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_02.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "DIN ALUMINIUM LUG",
                        "value": "DIN ALUMINIUM LUG",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/DIN_ALUMINIUM_LUG.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "Cable ties Self Lockable",
                        "value": "Cable ties Self Lockable",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Tie_Heat_Shrinkable_Tubing/Cable_ties_Self_Lockable.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 05",
                        "value": "YFTL 05",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_05.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CABLE CUTTER",
                        "value": "CABLE CUTTER",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/CABLE_CUTTER.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BULLET SHAPED FEMALE FULL INSULATING JOINT",
                        "value": "BULLET SHAPED FEMALE FULL INSULATING JOINT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BULLET_SHAPED_FEMALE_FULL_INSULATING_JOINT.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "BULLET SHAPED MALE PRE INSULATING JOINT",
                        "value": "BULLET SHAPED MALE PRE INSULATING JOINT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BULLET_SHAPED_MALE_PRE_INSULATING_JOINT.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "CABLE LUG FOR JM JGK TYPE",
                        "value": "CABLE LUG FOR JM JGK TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CABLE_LUG_FOR_JM_JGK_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 07",
                        "value": "YFTL 07",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_07.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 11",
                        "value": "YFTL 11",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_11.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Heavy Wall HST with without hot melt adhesive",
                        "value": "Heavy Wall HST with without hot melt adhesive",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Heavy_Wall_HST_with_without_hot_melt_adhesive.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BIMETAL LUG B TYPE",
                        "value": "BIMETAL LUG B TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BIMETAL_LUG_B_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 08",
                        "value": "YFTL 08",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_08.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Heat Shrinkable Tubing",
                        "value": "Heat Shrinkable Tubing",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Tie_Heat_Shrinkable_Tubing/Heat_Shrinkable_Tubing.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "UYConnector",
                        "value": "UYConnector",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/UYConnector.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TZ TYPE NEEDLE BARE ENDS",
                        "value": "TZ TYPE NEEDLE BARE ENDS",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/TZ_TYPE_NEEDLE_BARE_ENDS.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 03",
                        "value": "YFTL 03",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_03.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "CABLE LUG FOR DT TYPE",
                        "value": "CABLE LUG FOR DT TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CABLE_LUG_FOR_DT_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "YFTL 04",
                        "value": "YFTL 04",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/toolbox/YFTL_04.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "TZ MTF",
                        "value": "TZ MTF",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/TZ_MTF.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "BIMETAL LUG A TYPE",
                        "value": "BIMETAL LUG A TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BIMETAL_LUG_A_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "Andrew Cutter For Copper Cable MCPT 78",
                        "value": "Andrew Cutter For Copper Cable MCPT 78",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_Assembly/Andrew_Cutter_For_Copper_Cable_MCPT_78.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Stress Control Tubing BSC 360 36kv",
                        "value": "Stress Control Tubing BSC 360 36kv",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Heat_shrink_tubing/Stress_Control_Tubing_BSC_360_36kv.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "BOLTED COPPER LUG WCMC TYPE",
                        "value": "BOLTED COPPER LUG WCMC TYPE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/BOLTED_COPPER_LUG_WCMC_TYPE.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "CIRCULAR NAKED TERMINAL TO STYLE",
                        "value": "CIRCULAR NAKED TERMINAL TO STYLE",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Cable_lugs/CIRCULAR_NAKED_TERMINAL_TO_STYLE.PDF",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_safety_belt": {

                "question": "Which Safety BELT product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SFETYY BELT CLASS D",
                        "value": "SFETYY BELT CLASS D",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/SAFETY_BELT/SFETYY_BELT_CLASS_D.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SAFETY HELMET",
                        "value": "SAFETY HELMET",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/SAFETY_BELT/SAFETY_HELMET.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SAFETY BELT CLASS A",
                        "value": "SAFETY BELT CLASS A",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/SAFETY_BELT/SAFETY_BELT_CLASS_A.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SAFETY BELT CLASS P",
                        "value": "SAFETY BELT CLASS P",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/SAFETY_BELT/SAFETY_BELT_CLASS_P.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "REFLECTIVE SAFETY JACKET",
                        "value": "REFLECTIVE SAFETY JACKET",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/SAFETY_BELT/REFLECTIVE_SAFETY_JACKET.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_telecom_purpose": {

                "question": "Which Telecom Purpose product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Telecom Network Installation Kit",
                        "value": "Telecom Network Installation Kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Telecom_purpose/Telecom_Network_Installation_Kit.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Communication tool kit",
                        "value": "Communication tool kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Telecom_purpose/Communication_tool_kit.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Telecom Datacomm Installation Kit",
                        "value": "Telecom Datacomm Installation Kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Telecom_purpose/Telecom_Datacomm_Installation_Kit.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Data Telephone Pro Kit",
                        "value": "Data Telephone Pro Kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Telecom_purpose/Data_Telephone_Pro_Kit.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Deluxe Telecom Installer kit",
                        "value": "Deluxe Telecom Installer kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Tools/Telecom_purpose/Deluxe_Telecom_Installer_kit.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "installation_tools_weather_proofing_kit": {

                "question": "Which Weather Proofing Kit product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "3M Rubber Mastic Tape 28CT",
                        "value": "3M Rubber Mastic Tape 28CT",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Weather_Proofing_Kit/3M_Rubber_Mastic_Tape_28CT.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Scapa Rubber Mastic Tape 2585",
                        "value": "Scapa Rubber Mastic Tape 2585",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Weather_Proofing_Kit/Scapa_Rubber_Mastic_Tape_2585.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Cotran Rubber Mastic Tape KC80",
                        "value": "Cotran Rubber Mastic Tape KC80",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Weather_Proofing_Kit/Cotran_Rubber_Mastic_Tape_KC80.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Weather Profing Kit",
                        "value": "Weather Profing Kit",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Installation_Kit/Weather_Proofing_Kit/Weather_Profing_Kit.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Which Test & Measurement product?
            # -------------------------------------------------

            "test_measurement": {

                "question": "Which Test & Measurement product?",

                "key": "subcategory",

                "options": [

                    {
                        "text": "Other Test Measurement Items",
                        "value": "Other Test Measurement Items",
                        "next": "test_measurement_other_items"
                    },

                    {
                        "text": "RF Test Equipment",
                        "value": "RF Test Equipment",
                        "next": "test_measurement_rf_test_equipment"
                    },

                    {
                        "text": "Site Master",
                        "value": "Site Master",
                        "next": "test_measurement_site_master"
                    }

                ]

            },

            "test_measurement_other_items": {

                "question": "Which Other Test Measurement Items product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "SFP Stock List",
                        "value": "SFP Stock List",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Optical_Test_Equipment/SFP_Stock_List.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Semi automatic shield box",
                        "value": "Semi automatic shield box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/Semi_automatic_shield_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Pneumatic Shield Box",
                        "value": "Pneumatic Shield Box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/Pneumatic_Shield_Box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "M2020 Manual Sheild Box",
                        "value": "M2020 Manual Sheild Box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/M2020_Manual_Sheild_Box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Mini 4S Splicer",
                        "value": "Mini 4S Splicer",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Optical_Test_Equipment/Mini_4S_Splicer.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "LNA",
                        "value": "LNA",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/LNA.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "MS710",
                        "value": "MS710",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/MS710.PDF",
                        "next": "quantity"
                    },

                    {
                        "text": "lock type manual shield box",
                        "value": "lock type manual shield box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/lock_type_manual_shield_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "conductive fabric ZS 260 005 80g RS",
                        "value": "conductive fabric ZS 260 005 80g RS",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/conductive_fabric_ZS_260_005_80g_RS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Nickel mesh ZA 130T",
                        "value": "Nickel mesh ZA 130T",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/Nickel_mesh_ZA_130T.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Test Measurement Equipment",
                        "value": "Test Measurement Equipment",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/Test_Measurement_Equipment.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Test Measurement Equipment1",
                        "value": "Test Measurement Equipment1",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/Test_Measurement_Equipment1.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Manual RF Sheild Box",
                        "value": "Manual RF Sheild Box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/Manual_RF_Sheild_Box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "agilent u200a power meter",
                        "value": "agilent u200a power meter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/agilent_u200a_power_meter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Silver fabric ZHZZB",
                        "value": "Silver fabric ZHZZB",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/Silver_fabric_ZHZZB.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RF shield box SD5050",
                        "value": "RF shield box SD5050",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/RF_shield_box_SD5050.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "conductive fabric with adhesive ZS 260 005 120g CA PF",
                        "value": "conductive fabric with adhesive ZS 260 005 120g CA PF",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/conductive_fabric_with_adhesive_ZS_260_005_120g_CA_PF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "conductive fabric 230 005PF",
                        "value": "conductive fabric 230 005PF",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/conductive_fabric_230_005PF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "150-CB",
                        "value": "150-CB",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/CHAMBER/150-CB.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "conductive fabric ZS 260 005 70g PF",
                        "value": "conductive fabric ZS 260 005 70g PF",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/conductive_fabric_ZS_260_005_70g_PF.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RF shield box",
                        "value": "RF shield box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/RF_shield_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Silver fabric ZHLXG",
                        "value": "Silver fabric ZHLXG",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/Silver_fabric_ZHLXG.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "conductive fabric with adhesive ZS 260 005 125g CA RS",
                        "value": "conductive fabric with adhesive ZS 260 005 125g CA RS",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/conductive_fabric_with_adhesive_ZS_260_005_125g_CA_RS.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "conductive sponge ZT-1.00mm",
                        "value": "conductive sponge ZT-1.00mm",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/EMI_EMC_Shilding_product/conductive_sponge_ZT-1.00mm.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "UHF TEM Cell",
                        "value": "UHF TEM Cell",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/UHF_TEM_Cell.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "SMD 4020 Semi automatic shield box",
                        "value": "SMD 4020 Semi automatic shield box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/SMD_4020_Semi_automatic_shield_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "M4040 manual shield box",
                        "value": "M4040 manual shield box",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Shield_Box/M4040_manual_shield_box.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "18-CS",
                        "value": "18-CS",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/CHAMBER/18-CS.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "test_measurement_rf_test_equipment": {

                "question": "Which RF Test Equipment product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "E1 BER Tester",
                        "value": "E1 BER Tester",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/E1_BER_Tester.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "RF Power meter",
                        "value": "RF Power meter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/RF_Power_meter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Frquency meter",
                        "value": "Frquency meter",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/Frquency_meter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "JDSU Site Master 724",
                        "value": "JDSU Site Master 724",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/Site_Master/JDSU_Site_Master_724.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Anritsu Site Master",
                        "value": "Anritsu Site Master",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/Site_Master/Anritsu_Site_Master.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Signal generator",
                        "value": "Signal generator",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/Signal_generator.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Network Analyzer",
                        "value": "Network Analyzer",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/Network_Analyzer.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "matravi digital clamp meter",
                        "value": "matravi digital clamp meter",
                        "price": None,
                        "datasheet_url": "http://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/matravi_digital_clamp_meter.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "Bird Site Master",
                        "value": "Bird Site Master",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/RF_Test_Equipment/Site_Master/Bird_Site_Master.pdf",
                        "next": "quantity"
                    }

                ]

            },

            "test_measurement_site_master": {

                "question": "Which Site Master product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "Pricelist for optical cable products 2017",
                        "value": "Pricelist for optical cable products 2017",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Test_and_Measuring_Instrument/Site_Master/Bird_Site_master/Pricelist_for_optical_cable_products_2017.pdf",
                        "next": "quantity"
                    }

                ]

            },

            # -------------------------------------------------
            # Masts
            # -------------------------------------------------

            "masts": {

                "question": "Which Mast product would you like?",

                "key": "product_variant",

                "options": [

                    {
                        "text": "8.5 Telecom Tower Mast",
                        "value": "8.5 Telecom Tower Mast",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Mast/Mast/8.5_Telecom_Tower_Mast.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "10m Telecom Tower Mast",
                        "value": "10m Telecom Tower Mast",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Mast/Mast/10m_Telecom_Tower_Mast.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "12m Telecom Tower Mast",
                        "value": "12m Telecom Tower Mast",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Mast/Mast/12m_Telecom_Tower_Mast.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "18m Telecom Tower Mast",
                        "value": "18m Telecom Tower Mast",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Mast/Mast/18m_Telecom_Tower_Mast.pdf",
                        "next": "quantity"
                    },

                    {
                        "text": "6m Telecom Tower Mast",
                        "value": "6m Telecom Tower Mast",
                        "price": None,
                        "datasheet_url": "https://www.rfconnector.in/catalog/Mast/Mast/6m_Telecom_Tower_Mast.pdf",
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
