import functions
import operations

while True:
    continue_check = (input('Do you want to continue?[Y/N]')).upper()
    if continue_check == "Y":
        a, b, action = operations.getOperationsData()

    match action:
        case "+":
            result = functions.addNums(a, b)
        case "-":
            result = functions.subtractNums(a, b)
        case "*":
            result = functions.multiplicateNums(a, b)
        case "/":
            result = functions.divideNums(a, b)

    print(result)