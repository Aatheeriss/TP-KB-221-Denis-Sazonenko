a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

action = input("Enter action (+, -, *, /): ").strip()

if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
else:
    print("Invalid action. Please enter +, -, *, or /.")
