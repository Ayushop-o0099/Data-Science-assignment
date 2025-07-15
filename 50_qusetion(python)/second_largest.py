lst = list(map(int, input("Enter numbers: ").split()))
unique = list(set(lst))
unique.sort()
print("Second largest:", unique[-2])