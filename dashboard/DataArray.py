# Choices for expense account (value, display label)
EXPENSE_ACCOUNT_CHOICES = [
    ("cost_of_goods_sold", "Cost of Goods Sold"),
    ("consumable", "Consumable"),
    ("electricity", "Electricity"),
    ("water", "Water"),
    ("rent", "Rent"),
    ("repair_and_maintenance", "Repair and Maintenance"),
    ("fuel_expense", "Fuel Expense"),
    ("courier", "Courier"),
    ("conveyance", "Conveyance"),
    ("meals_and_entertainments", "Meals and Entertainments"),
    ("embroidery", "Embroidery"),  # Added from items data array
]
# List of employees as tuples for section form display (name, email)
EMPLOYEE_LIST = [
    ("Ajay Kumar", "ajay.kumar@factry.in"),
    ("Priya Sharma", "priya.sharma@factry.in"),
    ("Rahul Verma", "rahul.verma@factry.in"),
    ("Sneha Singh", "sneha.singh@factry.in"),
    ("Vikram Patel", "vikram.patel@factry.in"),
    ("Anjali Mehra", "anjali.mehra@factry.in"),
    ("Rohit Gupta", "rohit.gupta@factry.in"),
    ("Neha Joshi", "neha.joshi@factry.in"),
    ("Amit Sinha", "amit.sinha@factry.in"),
    ("Pooja Desai", "pooja.desai@factry.in"),
]

# Choices for GST treatment (value, display label)
GST_TREATMENT_CHOICES = [
    ("registered_business_regular", "Registered Business - Regular"),
    ("registered_business_composition", "Registered Business - Composition"),
    ("unregistered_business", "Unregistered Business"),
    ("consumer", "Consumer"),
    ("overseas", "Overseas"),
    ("non_gst_supply", "Non-GST Supply"),
    ("out_of_scope", "Out of Scope"),
]

# Choices for Indian states (value, display label)
INDIAN_STATE_CHOICES = [
    ("andhra_pradesh", "Andhra Pradesh"),
    ("arunachal_pradesh", "Arunachal Pradesh"),
    ("assam", "Assam"),
    ("bihar", "Bihar"),
    ("chhattisgarh", "Chhattisgarh"),
    ("goa", "Goa"),
    ("gujarat", "Gujarat"),
    ("haryana", "Haryana"),
    ("himachal_pradesh", "Himachal Pradesh"),
    ("jharkhand", "Jharkhand"),
    ("karnataka", "Karnataka"),
    ("kerala", "Kerala"),
    ("madhya_pradesh", "Madhya Pradesh"),
    ("maharashtra", "Maharashtra"),
    ("manipur", "Manipur"),
    ("meghalaya", "Meghalaya"),
    ("mizoram", "Mizoram"),
    ("nagaland", "Nagaland"),
    ("odisha", "Odisha"),
    ("punjab", "Punjab"),
    ("rajasthan", "Rajasthan"),
    ("sikkim", "Sikkim"),
    ("tamil_nadu", "Tamil Nadu"),
    ("telangana", "Telangana"),
    ("tripura", "Tripura"),
    ("uttar_pradesh", "Uttar Pradesh"),
    ("uttarakhand", "Uttarakhand"),
    ("west_bengal", "West Bengal"),
    ("andaman_and_nicobar_islands", "Andaman and Nicobar Islands"),
    ("chandigarh", "Chandigarh"),
    ("dadra_and_nagar_haveli_and_daman_and_diu", "Dadra and Nagar Haveli and Daman and Diu"),
    ("delhi", "Delhi"),
    ("jammu_and_kashmir", "Jammu and Kashmir"),
    ("ladakh", "Ladakh"),
    ("lakshadweep", "Lakshadweep"),
    ("puducherry", "Puducherry"),
]

# Combined choices for tax and tax group (value, display label)
TAX_AND_TAX_GROUP_CHOICES = [
    ("igst_0", "IGST 0%"),
    ("igst_5", "IGST 5%"),
    ("igst_12", "IGST 12%"),
    ("igst_18", "IGST 18%"),
    ("igst_25", "IGST 25%"),
    ("gst_0", "GST 0%"),
    ("gst_5", "GST 5%"),
    ("gst_12", "GST 12%"),
    ("gst_18", "GST 18%"),
    ("gst_25", "GST 25%"),
]

# List of apparel industry vendors as tuples (company name, email)
APPAREL_VENDOR_LIST = [
    {"id": 1, "name": "Raymond Ltd. Textile and Apparel Division", "email": "contact@raymond.in"},
    {"id": 2, "name": "Aditya Birla Fashion & Retail Limited", "email": "info@abfrl.com"},
    {"id": 3, "name": "Arvind Limited Fabrics and Garments", "email": "sales@arvind.com"},
    {"id": 4, "name": "Shahi Exports Private Limited Garment Manufacturing", "email": "info@shahi.co.in"},
    {"id": 5, "name": "Gokaldas Exports Limited Apparel Solutions", "email": "contact@gokaldasexports.com"},
    {"id": 6, "name": "Page Industries Limited", "email": "support@jockeyindia.com"},
    {"id": 7, "name": "Monte Carlo Fashions Limited Knitwear and Garments", "email": "info@montecarlocorporate.com"},
    {"id": 8, "name": "TCNS Clothing Company Limited ", "email": "enquiry@tcnsclothing.com"},
    {"id": 9, "name": "Kewal Kiran Clothing Limited ", "email": "info@kewalkiran.com"},
    {"id": 10, "name": "Future Lifestyle Fashions Limited Apparel Retail", "email": "contact@futurelifestyle.in"},
]

# List of apparel industry customers as tuples (company name, email)
APPAREL_CUSTOMER_LIST = [
    {"id": 1, "name": "Pantaloons Pvt. Ltd.", "email": "contact@pantaloons.com"},
    {"id": 2, "name": "Shoppers Stop Limited", "email": "info@shoppersstop.com"},
    {"id": 3, "name": "Lifestyle International Pvt. Ltd.", "email": "support@lifestylestores.com"},
    {"id": 4, "name": "Central Retail Stores", "email": "enquiry@centralandme.com"},
    {"id": 5, "name": "Reliance Trends Ltd.", "email": "info@reliancetrends.com"},
    {"id": 6, "name": "Max Fashion Retail", "email": "contact@maxfashion.com"},
    {"id": 7, "name": "Westside Department Stores", "email": "support@westside.com"},
    {"id": 8, "name": "V-Mart Retail Ltd.", "email": "info@vmart.co.in"},
    {"id": 9, "name": "Fabindia Overseas Pvt. Ltd.", "email": "contact@fabindia.net"},
    {"id": 10, "name": "Biba Apparels Pvt. Ltd.", "email": "info@biba.in"},
]

# Choices for payment methods (value, display label)
PAYMENT_METHOD_CHOICES = [
    ("bank_transfer", "Bank Transfer"),
    ("upi", "UPI Payment"),
    ("google_pay", "Google Pay"),
    ("phonepe", "PhonePe"),
    ("paytm", "Paytm"),
    ("cash", "Petty Cash"),
    ("cheque", "Cheque"),
    ("credit_card", "Credit Card"),
    ("debit_card", "Debit Card"),
    ("net_banking", "Net Banking"),
    ("neft", "NEFT"),
    ("rtgs", "RTGS"),
    ("imps", "IMPS"),
    ("demand_draft", "Demand Draft"),
]

# List of items used in apparel manufacturing (item name, description)
APPAREL_MANUFACTURING_ITEMS = [
    ("fabric", "Base material for garments (cotton, polyester, etc.)"),
    ("thread", "Sewing thread for stitching"),
    ("sewing_machine_needle", "Needle for sewing machines"),
    ("thread_cutter", "Tool for cutting thread"),
    ("buttons", "Fasteners for garments"),
    ("zippers", "Zipper closures"),
    ("interlining", "Material for structure and support"),
    ("elastic", "Stretchable band for waistbands, cuffs, etc."),
    ("labels", "Brand and care labels"),
    ("hooks_and_eyes", "Small fasteners for closures"),
    ("velcro", "Hook and loop fastener"),
    ("lining_material", "Inner fabric for comfort and finish"),
    ("scissors", "Cutting tool for fabric and thread"),
    ("measuring_tape", "Tool for measuring fabric and garments"),
    ("tailor_chalk", "Marking tool for fabric"),
    ("pattern_paper", "Paper for garment patterns"),
    ("sewing_machine_oil", "Lubricant for sewing machines"),
    ("bobbin", "Thread spool for sewing machines"),
    ("seam_ripper", "Tool for removing stitches"),
    ("pressing_iron", "Iron for pressing garments"),
    ("cutting_table", "Table for fabric cutting"),
    ("pins_and_needles", "For holding fabric pieces together"),
    ("embroidery_thread", "Thread for decorative stitching"),
    ("fusible_tape", "Tape for bonding fabric layers"),
    ("snap_buttons", "Press-stud fasteners"),
]

# Detailed data for apparel manufacturing items
APPAREL_MANUFACTURING_ITEM_DETAILS = [
    {
        "name": "fabric",
        "unit": "meter",
        "hsn_code": "5208",
        "tax_preference": "taxable",
        "cost": 150.0,
        "account": "cost_of_goods_sold",
        "tax_rates": {
            "igst": 5,
            "gst": 5
        }
    },
    {
        "name": "thread",
        "unit": "spool",
        "hsn_code": "5401",
        "tax_preference": "taxable",
        "cost": 20.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "sewing_machine_needle",
        "unit": "box",
        "hsn_code": "8452",
        "tax_preference": "taxable",
        "cost": 50.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "thread_cutter",
        "unit": "piece",
        "hsn_code": "8213",
        "tax_preference": "taxable",
        "cost": 30.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "buttons",
        "unit": "packet",
        "hsn_code": "9606",
        "tax_preference": "taxable",
        "cost": 15.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "zippers",
        "unit": "piece",
        "hsn_code": "9607",
        "tax_preference": "taxable",
        "cost": 25.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "interlining",
        "unit": "meter",
        "hsn_code": "5903",
        "tax_preference": "taxable",
        "cost": 40.0,
        "account": "cost_of_goods_sold",
        "tax_rates": {
            "igst": 5,
            "gst": 5
        }
    },
    {
        "name": "elastic",
        "unit": "meter",
        "hsn_code": "5604",
        "tax_preference": "taxable",
        "cost": 10.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "labels",
        "unit": "piece",
        "hsn_code": "5807",
        "tax_preference": "taxable",
        "cost": 2.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "hooks_and_eyes",
        "unit": "packet",
        "hsn_code": "8308",
        "tax_preference": "taxable",
        "cost": 12.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "velcro",
        "unit": "meter",
        "hsn_code": "5806",
        "tax_preference": "taxable",
        "cost": 18.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "lining_material",
        "unit": "meter",
        "hsn_code": "5513",
        "tax_preference": "taxable",
        "cost": 35.0,
        "account": "cost_of_goods_sold",
        "tax_rates": {
            "igst": 5,
            "gst": 5
        }
    },
    {
        "name": "scissors",
        "unit": "piece",
        "hsn_code": "8213",
        "tax_preference": "taxable",
        "cost": 60.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "measuring_tape",
        "unit": "piece",
        "hsn_code": "9017",
        "tax_preference": "taxable",
        "cost": 25.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "tailor_chalk",
        "unit": "box",
        "hsn_code": "9609",
        "tax_preference": "taxable",
        "cost": 8.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "pattern_paper",
        "unit": "sheet",
        "hsn_code": "4811",
        "tax_preference": "taxable",
        "cost": 5.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "sewing_machine_oil",
        "unit": "liter",
        "hsn_code": "2710",
        "tax_preference": "taxable",
        "cost": 120.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "bobbin",
        "unit": "piece",
        "hsn_code": "8452",
        "tax_preference": "taxable",
        "cost": 7.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "seam_ripper",
        "unit": "piece",
        "hsn_code": "8213",
        "tax_preference": "taxable",
        "cost": 15.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "pressing_iron",
        "unit": "piece",
        "hsn_code": "8516",
        "tax_preference": "taxable",
        "cost": 800.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "cutting_table",
        "unit": "piece",
        "hsn_code": "9403",
        "tax_preference": "taxable",
        "cost": 5000.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "pins_and_needles",
        "unit": "box",
        "hsn_code": "7319",
        "tax_preference": "taxable",
        "cost": 10.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 18,
            "gst": 18
        }
    },
    {
        "name": "embroidery_thread",
        "unit": "spool",
        "hsn_code": "5402",
        "tax_preference": "taxable",
        "cost": 30.0,
        "account": "embroidery",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "fusible_tape",
        "unit": "roll",
        "hsn_code": "5906",
        "tax_preference": "taxable",
        "cost": 20.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    },
    {
        "name": "snap_buttons",
        "unit": "packet",
        "hsn_code": "9606",
        "tax_preference": "taxable",
        "cost": 18.0,
        "account": "consumable",
        "tax_rates": {
            "igst": 12,
            "gst": 12
        }
    }
]

# List of payment terms (value, display label)
PAYMENT_TERMS_CHOICES = [
    ("net0", "Net 0 days"),
    ("net7", "Net 7 days"),
    ("net15", "Net 15 days"),
    ("net30", "Net 30 days"),
    ("net45", "Net 45 days"),
    ("net60", "Net 60 days"),
]