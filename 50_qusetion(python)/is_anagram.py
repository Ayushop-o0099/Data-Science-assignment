s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()
print("Anagram" if sorted(s1) == sorted(s2) else "Not anagram")