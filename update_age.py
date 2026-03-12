from datetime import date

# Change this to your actual birthday
BIRTH_DATE = date(2006, 9, 1) # Format: YYYY, M, D

def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year

def update_readme():
    age = str(calculate_age(BIRTH_DATE))
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the tags and replace the content between them
    import re
    new_content = re.sub(r'(<!-- age -->).*?(<!-- /age -->)', rf'\g<1>{age}\g<2>', content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()