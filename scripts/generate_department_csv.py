import pandas as pd

departments = [
    ("DEP001", "Administration", "School Administration"),
    ("DEP002", "Academics", "Academic Operations"),
    ("DEP003", "Primary Section", "Primary School Department"),
    ("DEP004", "Middle Section", "Middle School Department"),
    ("DEP005", "Secondary Section", "Secondary School Department"),
    ("DEP006", "Senior Secondary Section", "Senior Secondary Department"),
    ("DEP007", "Mathematics", "Mathematics Department"),
    ("DEP008", "Science", "Science Department"),
    ("DEP009", "Computer Science", "Computer Science Department"),
    ("DEP010", "English", "English Department"),
    ("DEP011", "Hindi", "Hindi Department"),
    ("DEP012", "Social Science", "Social Science Department"),
    ("DEP013", "Commerce", "Commerce Department"),
    ("DEP014", "Arts", "Arts Department"),
    ("DEP015", "Physical Education", "Sports and Physical Education"),
    ("DEP016", "Library", "Library Services"),
    ("DEP017", "Examinations", "Examination Cell"),
    ("DEP018", "Student Affairs", "Student Welfare and Affairs"),
    ("DEP019", "Admissions", "Admissions Department"),
    ("DEP020", "Finance", "Accounts and Finance"),
    ("DEP021", "Human Resources", "Human Resource Management"),
    ("DEP022", "IT Services", "Information Technology Services"),
    ("DEP023", "Transport", "Transport Management"),
    ("DEP024", "Hostel", "Hostel Administration"),
    ("DEP025", "Security", "Campus Security Department"),
]

rows = []

for code, name, description in departments:

    rows.append({
        "slug": code.lower(),
        "code": code,
        "name": name,
        "description": description,
        "is_active": 1
    })

data = pd.DataFrame(rows)

data.to_csv(
    "departments.csv",
    index=False
)

print(
    f"{len(data)} departments generated"
)