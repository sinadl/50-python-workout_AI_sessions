from datetime import date

family = {
    "father": date(1970, 5, 15),
    "mother": date(1975, 8, 22),
    "sister": date(2000, 3, 10),
    "brother": date(2005, 11, 5)
}

name = input("Enter a family member's name: ")

if name in family:
    birthday = family[name]
    today = date.today()

    age_in_days = (today - birthday).days

    print(f"{name} is {age_in_days:,} days old.")
else:
    print("Person not found.")