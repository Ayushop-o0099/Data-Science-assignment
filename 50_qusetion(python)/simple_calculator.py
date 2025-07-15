def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
if op in operations:
    print("Result:", operations[op](a, b))
else:
    print("Invalid operator.")