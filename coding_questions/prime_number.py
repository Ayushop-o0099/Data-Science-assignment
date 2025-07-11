n=int(input("Enter a number : "))
flag=True
for x in range(2,n):
    if n%x==0:
        flag=False
if flag==True:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")