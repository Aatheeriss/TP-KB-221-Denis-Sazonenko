import sys
import csv

def sanitizing(var):
    var = var.strip()
    var = var.capitalize()
    return var

def ReadFromFile(file_name):
    students = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"Name": row["Name"], "Phone": row["Phone"], "Mail": row["Mail"], "Age": row["Age"]})
    return students

def printAllList(list_of_students):
    for elem in list_of_students:
        strForPrint = "Student name is " + elem["Name"] + ",  Phone is " + elem["Phone"] + ", Mail is " + elem["Mail"] + ", Age is " + elem["Age"]
        print(strForPrint)

def addNewElement(list_of_students):
    name = sanitizing(input("Please enter student name: "))
    phone = input("Please enter student phone: ")
    mail = input("Please enter student mail: ")
    age = input("Please enter student age: ")

    newItem = {"Name": name, "Phone": phone, "Mail": mail, "Age": age}

    # Find insert position
    insertPosition = 0
    for item in list_of_students:
        if name > item["Name"]:
            insertPosition += 1
        else:
            break
    list_of_students.insert(insertPosition, newItem)
    print("\n----New element has been added----\n")
    return list_of_students

def updateElement(list_of_students):
    name = sanitizing(input("\nPlease enter name to be updated: "))
    for index, student in enumerate(list_of_students):
        if name == student["Name"]:
            new_name = input("Enter new name: ").capitalize()
            new_age = input("Enter new age: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            newElement = {"Name": new_name, "Age": new_age, "Phone": new_phone, "Mail": new_email}

            del list_of_students[index]
            insertPos = 0
            for pos, elem in enumerate(list_of_students):
                if new_name > elem["Name"]:
                    insertPos = pos + 1
                else:
                    break
            list_of_students.insert(insertPos, newElement)
            print("\n----Element has been updated----\n")
            return list_of_students
    else:
        print("\n----Student not found----\n")
        return list_of_students
   
def deleteElement(list_of_students):
    name = sanitizing(input("\nPlease enter name to be deleted:"))
    deletePosition = -1
    for item in list_of_students:
        if name == item["Name"]:
            deletePosition = list_of_students.index(item)
            break
    if deletePosition == -1:
        print("\n----Element was not found----\n")
        return list_of_students 
    else:
        print("Delete position " + str(deletePosition))
        # list.pop(deletePosition)
        del list_of_students[deletePosition]
        print("\n----Deleted successfully!----\n")
    return list_of_students

def FileSave(list_of_students, file_name):
    if not list_of_students:
        print("\n----No data to save.----\n")
        return
    
    with open(file_name, "w", newline='') as csvfile:
        fieldnames = ["Name", "Phone", "Mail", "Age"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_students:
            writer.writerow(row)
    print('\n----Saved successfully!----\n')

def main(file_name):
    list_of_students = ReadFromFile(file_name)
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit] ")
        if choice.lower() == "c":
            print("\n----New element will be created:----\n")
            list_of_students = addNewElement(list_of_students)
            printAllList(list_of_students)
        elif choice.lower() == "u":
            print("\n----Existing element will be updated----\n")
            list_of_students = updateElement(list_of_students)
            printAllList(list_of_students)
        elif choice.lower() == "d":
            print("\n----Element will be deleted----\n")
            list_of_students = deleteElement(list_of_students)
            printAllList(list_of_students)
        elif choice.lower() == "p":
            print("\n----List will be printed----\n")
            printAllList(list_of_students)
        elif choice.lower() == "x":         
            if list_of_students == ReadFromFile(file_name):
                print("\n----Exit----\n")
                break
            else:
                FileSave(list_of_students, file_name)
                print("\n----Exit----\n")
                break           
        else:
            print("\n----Wrong choice----\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You have not entered an argument for the command line!")
        sys.exit()
    else:
        file_name = sys.argv[1]
        main(file_name)
#main()
