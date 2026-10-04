import pandas as pd

subjects = [

    ("SUB001", "English", "English Language"),
    ("SUB002", "Hindi", "Hindi Language"),
    ("SUB003", "Sanskrit", "Sanskrit Language"),
    ("SUB004", "French", "French Language"),
    ("SUB005", "German", "German Language"),

    ("SUB006", "Mathematics", "Mathematics"),
    ("SUB007", "Applied Mathematics", "Applied Mathematics"),

    ("SUB008", "Science", "General Science"),
    ("SUB009", "Physics", "Physics"),
    ("SUB010", "Chemistry", "Chemistry"),
    ("SUB011", "Biology", "Biology"),

    ("SUB012", "Environmental Studies", "EVS"),

    ("SUB013", "Social Science", "Social Science"),
    ("SUB014", "History", "History"),
    ("SUB015", "Geography", "Geography"),
    ("SUB016", "Political Science", "Political Science"),
    ("SUB017", "Economics", "Economics"),

    ("SUB018", "Commerce", "Commerce"),
    ("SUB019", "Accountancy", "Accountancy"),
    ("SUB020", "Business Studies", "Business Studies"),

    ("SUB021", "Computer Science", "Computer Science"),
    ("SUB022", "Information Technology", "Information Technology"),
    ("SUB023", "Artificial Intelligence", "Artificial Intelligence"),
    ("SUB024", "Data Science", "Data Science"),

    ("SUB025", "Physical Education", "Physical Education"),
    ("SUB026", "Health Education", "Health Education"),

    ("SUB027", "Art Education", "Art Education"),
    ("SUB028", "Drawing", "Drawing"),
    ("SUB029", "Painting", "Painting"),
    ("SUB030", "Music", "Music"),
    ("SUB031", "Dance", "Dance"),
    ("SUB032", "Drama", "Drama"),

    ("SUB033", "Psychology", "Psychology"),
    ("SUB034", "Sociology", "Sociology"),
    ("SUB035", "Philosophy", "Philosophy"),

    ("SUB036", "Legal Studies", "Legal Studies"),
    ("SUB037", "Entrepreneurship", "Entrepreneurship"),

    ("SUB038", "Agriculture", "Agriculture"),
    ("SUB039", "Home Science", "Home Science"),

    ("SUB040", "Robotics", "Robotics"),
    ("SUB041", "Coding", "Coding"),

    ("SUB042", "General Knowledge", "General Knowledge"),
    ("SUB043", "Moral Education", "Moral Education"),

    ("SUB044", "Library Science", "Library Science"),
    ("SUB045", "Work Education", "Work Education"),

    ("SUB046", "Yoga", "Yoga"),
    ("SUB047", "NCC", "National Cadet Corps"),
    ("SUB048", "Scouts and Guides", "Scouts and Guides"),

    ("SUB049", "Life Skills", "Life Skills"),
    ("SUB050", "Communication Skills", "Communication Skills"),
]

rows = []

for code, name, description in subjects:

    rows.append({

        "slug": code.lower(),

        "code": code,

        "name": name,

        "description": description
    })

data = pd.DataFrame(rows)

data.to_csv(
    "subjects.csv",
    index=False
)

print(
    f"{len(data)} subjects generated"
)