laptop = {
        "brand": "lenovo",
        "series": "legion"
    }

#1. update()
def updateTesting():

    laptop.update({"serial number": "LL252433"})
    print(laptop)

    return

#2. del()
def delTesting():

    del laptop["brand"]
    print(laptop)

    return

#3. clear()
def clearTesting():

    laptop.clear()
    print(laptop)

    return

#4. keys()
def keysTesting():

    laptop.keys()
    laptop["brand"] = "asus"
    print(laptop)

    return

#5. values()
def valuesTesting():
    
    laptop.values()
    laptop["brand"] = "asus"
    print(laptop)

    return

#6. items()
def itemsTesting():

    laptop.items()
    laptop["brand"] = "asus"
    print(laptop)

    return

def main():
    a = input("Enter number 1-6:\n 1. update()\n 2. del()\n 3. clear()\n 4. keys()\n 5. values()\n 6. items()\n")

    match a:
        case "1":
            updateTesting()
        case "2":
            delTesting()
        case "3":
            clearTesting()
        case "4":
            keysTesting()
        case "5":
            valuesTesting()
        case "6":
            itemsTesting()
        case _:
            print("Try again!")
    
    print("\n\n-_-_-_-_-_-_-_-_-_-_-_-_-\n\n")
    
    return

while True:
    main()