def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
s1 = input("Enetr a string : ").lower()
s2 = input("Enetr a string : ").lower()
print("Anagrams :" , are_anagrams(s1, s2))
