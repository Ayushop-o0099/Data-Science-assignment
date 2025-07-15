def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter number: "))
print("Factorial:", factorial(num))