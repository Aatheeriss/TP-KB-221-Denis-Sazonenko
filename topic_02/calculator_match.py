a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

action = input("Enter action (+, -, *, /): ").strip()

match action:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        try:
            result = a / b
            print(result)
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
    case _:
        print("Invalid action. Please enter +, -, *, or /.")