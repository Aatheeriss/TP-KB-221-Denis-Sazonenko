import logging

logging.basicConfig(level=logging.INFO, filename="topic_07\calculator\py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

class Operations:

    def operationsInput():
        try:
            a = float(input("Enter 1 number: "))
            b = float(input("Enter 2 number: "))
        except ValueError:
            logging.error(ValueError, exc_info=True)
            print("Wrong number, try again!")
            return None, None, None
            
        action = input("Enter action (+, -, *, /): ")
        if action not in "+-/*":
            logging.info("User entered wrong action.")
            print("Wrong action, try again!")
            return None, None, None
        return a, b, action

