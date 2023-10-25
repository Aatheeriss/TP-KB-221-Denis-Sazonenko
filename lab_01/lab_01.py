
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
#ADDED 2 MORE FIELDS
list = [
    {"name":"Bob", "phone":"0631234567", "mail":"bob@example.com", "age":"17"},
    {"name":"Emma", "phone":"0631234567", "mail":"emma@example.com", "age":"18"},
    {"name":"Jon",  "phone":"0631234567", "mail":"jon@example.com", "age":"20"},
    {"name":"Zak",  "phone":"0631234567", "mail":"zak@example.com", "age":"20"}
]

#BUBBLE SORT IMPLEMENTED
def sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if list[j]["name"] > list[j + 1]["name"]:
                list[j], list[j + 1] = list[j + 1], list[j]

#SANITIZING
def sanitizing(var):
    var = var.strip()
    var = var.capitalize()
    
    return var

#ADDED 2 MORE FIELDS TO OUTPUT
def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Mail is " + elem["mail"] + ", Age is " + elem["age"]  
        print(strForPrint)
    return

#ADDED 2 MORE FIELDS TO INPUT
def addNewElement():
    name = sanitizing(input("Pease enter student name: "))
    phone = input("Please enter student phone: ")
    mail = input("Please enter student mail: ")
    age = input("Please enter student age: ")

    newItem = {"name": name, "phone": phone, "mail": mail, "age": age}

    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = sanitizing(input("Please enter name to be delated: "))
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return

#UPDATE IMPLEMENTED
def updateElement():
    name = sanitizing(input("Please enter name to be updated: "))
    for student in list:
        if name == student["name"]:
            student["name"] = sanitizing(input("Enter new student name: "))
            student["phone"] = input("Enter new student phone: ")
            student["mail"] = input("Enter new student mail: ")
            student["age"] = input("Enter new student age: ")
            sort(list)
            print("Student information has been updated!")
            print(f"Name: {student['name']}, Phone: {student['phone']}, Mail: {student['mail']}, Age: {student['age']}")
            return
    print("Student not found.")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

main()