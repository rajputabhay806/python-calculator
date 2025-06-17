# Make a Calculator
while True:
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n6.Exit\n")
    choice = int(input("Enter user choice: "))

    if choice == 6:
        print("Exit")
        break

    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))

    if choice == 1:
        print(f"Addition = {a+b}")
    elif choice == 2:
        print(f"Subtraction = {a-b}")
    elif choice == 3:
        print(f"Multiply = {a*b}")
    elif choice == 4:
        print(f"Division = {a/b}")
    elif choice == 5:
        print(f"Modulus = {a%b}")
    else:
        print("Please enter choice between 1 to 6.")
