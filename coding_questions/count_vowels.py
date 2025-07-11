n=input("Enetr a string : ").lower()
a=['a','e','i','o','u']
count=0
for i in n:
    for j in a:
        if i==j:
            count=count+1
print(f"Vowels Count : {count}")