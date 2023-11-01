import functions
import operations
import logging

logging.basicConfig(level=logging.INFO, filename="topic_07\calculator\py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
while True:
    a, b, action = operations.Operations.operationsInput()
    if a or b or action is None:
         continue
    else:    
        def result():
            match action:
                    case "+":
                        return functions.Functions.add(a, b)              
                    case "-":
                        return functions.Functions.subtract(a, b)               
                    case "*":
                        return functions.Functions.multiply(a, b)              
                    case "/":
                        return functions.Functions.divide(a, b)
                
    def main():
        print("Result is: " + str(result()))
        logging.info("User entered {a}, {b} and '{action}'; recieved result: " + str(result()))   

    while True:
        main()
        trigger = input("Continue [Y/N]").upper()
        if trigger != "Y":
            break