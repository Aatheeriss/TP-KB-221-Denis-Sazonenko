#1. extend()
def extendTesting():

    list1 = [1, 2, 3, 4, 5] 
    list2 = [6, 7, 8, 9, 0]

    list1.extend(list2)
    print(list1)
    return

#2. append()
def appendTesting():

    list1 = ['Hello', 'I', 'am']
    list1.append('Denis')

    print(list1)
    return

#3. insert(id, val)
def insertTesting():

    list1 = ['Hello', 'I', 'Denis']
    list1.insert(2, 'am')

    print(list1)
    return

#4. remove()
def removeTesting():

    list1 = ['Hello', 'I', 'removeMEpLeAsE', 'am', 'Denis']
    list1.remove('removeMEpLeAsE')
    
    print(list1)
    return

#5. clear()
def clearTesting():

    list1 = [1, 2, 3, 4, 5]
    list1.clear()
    list1.append('list is empty but this message')

    print(list1)
    return

#6. sort()
def sortTesting():

    list1 = [2, 5, 3, 1, 4]
    list1.sort()

    print(list1)
    return

#7. reverse()
def reverseTesting():

    list1 =[5, 4, 3, 2, 1]
    list1.reverse()

    print(list1)
    return

#8. copy()
def copyTesting():

    list1 = [1, 2, 3, 4, 5]

    print(list1.copy())
    return

def main():
    a = input("Enter number 1-8:\n 1. extend()\n 2. append()\n 3. insert()\n 4. remove()\n 5. clear()\n 6. sort()\n 7. reverse()\n 8. copy()\n")

    match a:
        case "1":
            extendTesting()
        case "2":
            appendTesting()
        case "3":
            insertTesting()
        case "4":
            removeTesting()
        case "5":
            clearTesting()
        case "6":
            sortTesting()
        case "7":
            reverseTesting()
        case "8":
            copyTesting()
        case _:
            print("Try again!")
    
    print("\n\n-_-_-_-_-_-_-_-_-_-_-_-_-\n\n")
    
    return

while True:
    main()
    