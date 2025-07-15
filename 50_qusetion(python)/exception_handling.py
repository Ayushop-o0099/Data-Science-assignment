try:
    num = int(input("Enter number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This always runs.")