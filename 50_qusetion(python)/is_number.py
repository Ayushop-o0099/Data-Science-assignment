def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number(input("Enter something: ")))