import sys
from filemgmt import FileMGMT

def main(file_name):
    student_list = FileMGMT.ReadFromFile(file_name)
    
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit] ")
        #create elem
        if choice.lower() == "c":
            print("\n----New element will be created:----\n")
            student_list.addNewElement()
            student_list.printAllList()
        #update elem
        elif choice.lower() == "u":
            print("\n----Existing element will be updated----\n")
            student_list.updateElement()
            student_list.printAllList()
        #delete elem
        elif choice.lower() == "d":
            print("\n----Element will be deleted----\n")
            student_list.deleteElement()
            student_list.printAllList()
        #print elems
        elif choice.lower() == "p":
            print("\n----List will be printed----\n")
            student_list.printAllList()
        #save and exit
        elif choice.lower() == "x":
            if student_list == FileMGMT.ReadFromFile(file_name):
                print("\n----Exit----\n")
                break
            else:
                FileMGMT.FileSave(student_list, file_name)
                print("\n----Exit----\n")
                break           
        else:
            print("\n----Wrong choice----\n")

if __name__ == "__main__":
    #recieving cmd argument
    if len(sys.argv) < 2:
        print("You have not entered an argument for the command line!")
        sys.exit()
    else:
        file_name = sys.argv[1]
        main(file_name)
