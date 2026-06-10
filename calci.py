n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("\n1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/) gives quotient")
print("5. Modulus (%) gives remainder")
print("6. Power (**)");
print("7. floor division (//) gives quotient without decimal part")
print("8. Exit")
while True:
    choice = input("\nEnter your choice of operation (1/2/3/4/5/6/7/8): ")
    if choice == '1':
        result = n1 + n2
        print(f"\nResult: {n1} + {n2} = {result}")
    elif choice == '2':
        result = n1 - n2
        print(f"\nResult: {n1} - {n2} = {result}")
    elif choice == '3':
        result = n1 * n2
        print(f"\nResult: {n1} * {n2} = {result}")
    elif choice == '4':
        if n2 != 0:
            result = n1 / n2
            print(f"\nResult: {n1} / {n2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    elif choice == '5':
        result = n1 % n2
        print(f"\nResult: {n1} % {n2} = {result}")
    elif choice == '6':
        result = n1 ** n2
        print(f"\nResult: {n1} ** {n2} = {result}")
    elif choice == '7':
        if n2 != 0:
            result = n1 // n2
            print(f"\nResult: {n1} // {n2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    elif choice == '8':
        print("\nExiting the calculator.")
        exit()
    else:
        print("\nInvalid choice. Please select a valid operation.") 