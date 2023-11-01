import logging

logging.basicConfig(level=logging.INFO, filename="topic_07\calculator\py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

class Functions:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        try:        
            return a / b
        except ZeroDivisionError:
            print("Division by zero is not allowed!!!")
            logging.error("ZeroDivisionError", exc_info=True)