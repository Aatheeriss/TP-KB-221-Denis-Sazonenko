import logging

logging.basicConfig(level=logging.INFO, filename="topic_06\calculator_with_logging\py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def addNums(a, b):
    result = a + b
    logging.info(f"User recieved a result of {result}")
    return result

def subtractNums(a, b):
    result = a - b
    logging.info(f"User recieved a result of {result}")
    return result

def multiplicateNums(a, b):
    result = a*b
    logging.info(f"User recieved a result of {result}")
    return result

def divideNums(a, b):
    try:
        result = a / b         
        logging.info(f"User recieved a result of {result}")
        return result
    
    except ZeroDivisionError:
        logging.error("ZeroDivisionError", exc_info=True)
        print("Division by zero is not allowed!")
    