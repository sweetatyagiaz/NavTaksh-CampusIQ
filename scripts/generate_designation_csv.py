import pandas as pd

designations = [

    ("DES001", "Principal", "School Head"),
    ("DES002", "Vice Principal", "Deputy School Head"),
    ("DES003", "Academic Director", "Academic Leadership"),
    ("DES004", "Academic Coordinator", "Academic Coordination"),

    ("DES005", "PGT Mathematics", "Post Graduate Teacher"),
    ("DES006", "PGT Physics", "Post Graduate Teacher"),
    ("DES007", "PGT Chemistry", "Post Graduate Teacher"),
    ("DES008", "PGT Biology", "Post Graduate Teacher"),
    ("DES009", "PGT English", "Post Graduate Teacher"),
    ("DES010", "PGT Computer Science", "Post Graduate Teacher"),
    ("DES011", "PGT Economics", "Post Graduate Teacher"),
    ("DES012", "PGT Commerce", "Post Graduate Teacher"),

    ("DES013", "TGT Mathematics", "Trained Graduate Teacher"),
    ("DES014", "TGT Science", "Trained Graduate Teacher"),
    ("DES015", "TGT English", "Trained Graduate Teacher"),
    ("DES016", "TGT Hindi", "Trained Graduate Teacher"),
    ("DES017", "TGT Social Science", "Trained Graduate Teacher"),
    ("DES018", "TGT Sanskrit", "Trained Graduate Teacher"),

    ("DES019", "PRT", "Primary Teacher"),
    ("DES020", "Nursery Teacher", "Pre Primary Teacher"),

    ("DES021", "Librarian", "Library Management"),
    ("DES022", "Sports Teacher", "Physical Education"),
    ("DES023", "Art Teacher", "Arts Department"),
    ("DES024", "Music Teacher", "Music Department"),

    ("DES025", "Counsellor", "Student Counselling"),
    ("DES026", "Special Educator", "Inclusive Education"),

    ("DES027", "HR Manager", "Human Resources"),
    ("DES028", "HR Executive", "Human Resources"),

    ("DES029", "Accountant", "Finance Department"),
    ("DES030", "Finance Manager", "Finance Department"),

    ("DES031", "Administrative Officer", "Administration"),
    ("DES032", "Office Assistant", "Administration"),

    ("DES033", "IT Manager", "Information Technology"),
    ("DES034", "System Administrator", "Information Technology"),
    ("DES035", "IT Support Engineer", "Information Technology"),

    ("DES036", "Transport Manager", "Transport Department"),
    ("DES037", "Driver", "Transport Department"),

    ("DES038", "Hostel Warden", "Hostel Department"),

    ("DES039", "Security Supervisor", "Security Department"),
    ("DES040", "Security Guard", "Security Department"),
]

rows = []

for code, name, description in designations:

    rows.append({

        "slug": code.lower(),
        "code": code,
        "name": name,
        "description": description,
        "is_active": 1
    })

data = pd.DataFrame(rows)

data.to_csv(
    "designations.csv",
    index=False
)

print(
    f"{len(data)} designations generated"
)