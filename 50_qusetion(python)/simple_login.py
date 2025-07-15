users = {"admin": "pass123", "user": "1234"}
uname = input("Username: ")
pwd = input("Password: ")

if users.get(uname) == pwd:
    print("Login successful")
else:
    print("Login failed")