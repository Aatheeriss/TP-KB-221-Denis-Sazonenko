def getOperationsData():
    while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                action = input("Enter action (+, -, *, /): ").strip()

                if action not in ('+', '-', '*', '/'):
                    print("Invalid action. Please enter +, -, *, or /.")
                    continue

                return a, b, action
            except ValueError:
                print('Invalid input. Please enter valid numbers.')