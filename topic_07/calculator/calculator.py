import operations
import functions
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="topic_07/calculator/py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)

while True:
    a, b, action = operations.Operations.operationsInput()
    if a is None or b is None or action is None:
        continue

    result = None

    if action == "+":
        result = functions.Functions.add(a, b)
    elif action == "-":
        result = functions.Functions.subtract(a, b)
    elif action == "*":
        result = functions.Functions.multiply(a, b)
    elif action == "/":
        result = functions.Functions.divide(a, b)
    else:
        print("Unsupported operation.")
        continue

    def main():
        print("Result: " + str(result))
        logging.info(f"User entered {a}, {b} and '{action}'; recieved the result: {result}")

    main()

    trigger = input("Continue? [Y/N]").upper()
    if trigger != "Y":
        break
