def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b
    if answer > 0:
        print(str(a), " - ", str(b), " = ", str(answer))
        print("Result is in a positive value")
    else:
        print("Your given First value is greater than Second, so the result is in a negative value")
        print(str(a), " - ", str(b), " = ", str(answer))


def multiply(a, b):
    answer = a * b
    print(a, "*", b, " = ", answer)


def division(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        answer = a / b
        print(a, "/", b, " = ", answer)


while True:
    print("A. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Choose your Operator : ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Submit First Number : "))
        b = input("Submit Second Number : ")
        if b.isdigit():  # Check if the input is a valid integer
            b = int(b)
            add(a, b)
        else:
            print("Invalid input for the second number. Please enter a valid integer.")

    elif choice == "s" or choice == "S":
        print("Subtraction")
        a = int(input("Submit First Number : "))
        b = int(input("Submit Second Number : "))
        sub(a, b)

    elif choice == "M" or choice == "m":
        print("Multiplication")
        a = int(input("Submit First Number : "))
        b = int(input("Submit Second Number : "))
        multiply(a, b)

    elif choice == "D" or choice == "d":
        a = int(input("Submit First Number : "))
        b = int(input("Submit Second Number : "))
        division(a, b)

    elif choice == "E" or choice == "e":
        print("Program ended")
        quit()

    else:
        print("Invalid choice. Please try again.")
