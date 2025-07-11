def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == num

num = int(input("Enter a number : "))
print(f"{num} is Armstrong : {is_armstrong(num)}")
