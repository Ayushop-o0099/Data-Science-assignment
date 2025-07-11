def fibo(n):
    count=1
    a=0
    b=1
    print(a,end=' ')
    print(b,end=' ')
    while count<=n-2:
        temp=a+b
        a=b
        b=temp
        print(temp,end=' ')
        count=count+1
n=int(input("Enter a number : "))
fibo(n)