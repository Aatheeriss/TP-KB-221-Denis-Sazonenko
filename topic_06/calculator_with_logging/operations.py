import logging

logging.basicConfig(level=logging.INFO, filename="\topic_06\calculator_with_logging\py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def getOperationsData():
    while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                action = input("Enter action (+, -, *, /): ").strip()
                logging.info(f"User entered the values of a and b: {a} and {b}, action: {action}.")

                if action not in ('+', '-', '*', '/'):
                    print("Invalid action. Please enter +, -, *, or /.")
                    logging.info(f"User entered invalid action. Retrying.")
                    continue

                return a, b, action
            except ValueError:
                print('Invalid input. Please enter valid numbers.')
                logging.error("ValueError", exc_info=True)