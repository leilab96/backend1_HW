import unicodedata

"""Generates a password from the last name."""
def generate_password(last_name):
    password = last_name.lower() + "123Start"
    return password
  
"""Generates an email address from a name."""
def generate_email(name):
    email = ""
    for n in name:
        n = unicodedata.normalize('NFKD', n).encode('ASCII', 'ignore').decode('utf-8')
        email += n.lower()
        email += "."
    email = email[:-1] + "@company.hu"
    return email

"""Generates a list of users with email addresses and passwords."""
def generate_users(names):

    users = []
    for name in names:
        last_name = name[0]
        email = generate_email(name)
        password = generate_password(last_name)
        user = {
            "name": " ".join(name),
            "email": email,
            "password": password
        }
        users.append(user)
    return sorted(users, key=lambda x: x["name"])

names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = generate_users(names)

with open("nevek.txt", "w", encoding="utf-8") as f:
    for user in users:
        f.write(f"{user['name']} {user['email']} {user['password']}\n")
