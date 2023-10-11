try:
    #insertion function which repeats until getting valid values of required functions
    def insertion():
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

    #calculation function (catches division by zero exeption)
    def calculation(a, b, action):
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
    #main
    def main():
        a, b, action = insertion()
        calculation(a, b, action)

    while True:     
        main()

except KeyboardInterrupt:
    print('\n\nBye!')
    exit
      