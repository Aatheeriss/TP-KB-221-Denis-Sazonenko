def positionFind(list1, element):
    list_start = 0
    list_end = len(list1) - 1

    while list_start <= list_end:
        list_mid = (list_start + list_end) // 2
        if list1[list_mid] == element:
            print("Element is already in list. Position is: " + str(list_mid))
            return
        elif list1[list_mid] < element:
            list_start = list_mid + 1
        else:
            list_end = list_mid - 1
    print ("Position to add is: " + str(list_start))
    return 

list1 = [1, 3, 5, 7, 9]

while True:
    print(list1)
    element = input("Enter the element to find position to add: ")
    element = int(element)
    position = positionFind(list1, element)
    