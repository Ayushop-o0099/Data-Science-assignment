import re
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

email = input("Enter email: ")
print("Valid email" if is_valid_email(email) else "Invalid email")