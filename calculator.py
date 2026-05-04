# Calculator with loop

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: division by zero")

    else:
        print("Invalid operation")

    # 👇 ye part important hai
    again = input("Do you want to continue? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator closed")
        break