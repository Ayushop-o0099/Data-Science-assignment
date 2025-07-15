def menu():
    print("1. Greet\n2. Add\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        print("Hello User!")
    elif choice == '2':
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("Sum:", a + b)
    else:
        print("Goodbye!")

menu()