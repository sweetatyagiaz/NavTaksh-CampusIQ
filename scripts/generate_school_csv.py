import pandas as pd
import random

schools = [

    ("Delhi Public School Faridabad", "DPSF", "Faridabad", "Haryana"),
    ("Ryan International School", "RIS", "Faridabad", "Haryana"),
    ("St Xavier School", "SXS", "Faridabad", "Haryana"),
    ("Modern Public School", "MPS", "Delhi", "Delhi"),
    ("Spring Dale School", "SDS", "Delhi", "Delhi"),
    ("Blue Bells School", "BBS", "Gurugram", "Haryana"),
    ("Amity International School", "AIS", "Noida", "Uttar Pradesh"),
    ("Bal Bharati Public School", "BBPS", "Delhi", "Delhi"),
    ("DAV Public School", "DAVPS", "Faridabad", "Haryana"),
    ("Army Public School", "APS", "Delhi", "Delhi"),
    ("Tagore International School", "TIS", "Delhi", "Delhi"),
    ("Lotus Valley International School", "LVIS", "Noida", "Uttar Pradesh"),
    ("Shiv Nadar School", "SNS", "Noida", "Uttar Pradesh"),
    ("Heritage School", "HS", "Gurugram", "Haryana"),
    ("Pathways School", "PS", "Gurugram", "Haryana"),
    ("Scottish High International School", "SHIS", "Gurugram", "Haryana"),
    ("The Shri Ram School", "TSRS", "Gurugram", "Haryana"),
    ("GD Goenka Public School", "GDGPS", "Gurugram", "Haryana"),
    ("Indus World School", "IWS", "Indore", "Madhya Pradesh"),
    ("Greenwood High International School", "GHIS", "Bengaluru", "Karnataka"),
    ("National Public School", "NPS", "Bengaluru", "Karnataka"),
    ("Chinmaya Vidyalaya", "CV", "Chennai", "Tamil Nadu"),
    ("PSBB Senior Secondary School", "PSBB", "Chennai", "Tamil Nadu"),
    ("La Martiniere College", "LMC", "Lucknow", "Uttar Pradesh"),
    ("Mayo College", "MC", "Ajmer", "Rajasthan"),

]

rows = []

for index, school in enumerate(schools, start=1):

    name, short_name, city, state = school

    rows.append({

        "code": f"SCH{index:03d}",

        "name": name,

        "short_name": short_name,

        "registration_number": f"REG{1000 + index}",

        "affiliation_number": f"AFF{5000 + index}",

        "udise_code": f"0619{index:08d}",

        "gst_number": "",

        "latitude": "",

        "longitude": "",

        "email": f"info{index}@school.edu.in",

        "phone": f"98{random.randint(10000000,99999999)}",

        "address_line_1": f"Sector {random.randint(1,99)}",

        "city": city,

        "state": state,

        "country": "India",

        "postal_code": random.randint(
            100000,
            999999
        ),

        "website": f"https://www.school{index}.edu.in",

        "primary_color": "#1E88E5",

        "secondary_color": "#43A047",

        "academic_session_start_month": 4,

        "is_active": 1

    })

data = pd.DataFrame(rows)

data.to_csv(
    "schools.csv",
    index=False
)

print(
    f"{len(data)} schools generated"
)