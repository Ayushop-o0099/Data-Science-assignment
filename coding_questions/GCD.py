def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter a Number : "))
num2 = int(input("Enter a Number : "))
print("GCD is:", gcd(num1, num2))
