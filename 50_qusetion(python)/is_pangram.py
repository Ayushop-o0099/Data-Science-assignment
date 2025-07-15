import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))

print(is_pangram(input("Enter a string: ")))