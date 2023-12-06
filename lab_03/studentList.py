from student import Student
from utils import Utils

#list of students init
class StudentList:
    
    def __init__(self):
        self.students = []
  
    #add new elem func
    def addNewElement(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        mail = input("Please enter student mail: ")
        age = input("Please enter student age: ")

        new_student = Student(Utils.saniitizing(name), phone, mail, age)
        insertPos = 0
        for student in self.students:
            if name > student.name:
                insertPos += 1
            else:
                break
        self.students.insert(insertPos, new_student)
  
    #update elem func        
    def updateElement(self):
        old_name = Utils.saniitizing(input("Enter existing element: "))
        for index, student in enumerate(self.students):
            if old_name == student.name:

                #deleting old object
                del self.students[index]
                
                #providing new info 
                new_name = Utils.saniitizing(input("Enter new name: "))
                new_phone = input("Enter new phone: ")
                new_mail = input("Enter new mail: ")
                new_age = input("Enter new age: ")
                new_student = Student(new_name, new_phone, new_mail, new_age)

                #inserting
                insertPos = 0
                for insertPos, existing_student in enumerate(self.students):
                    if new_student.name > existing_student.name:
                        insertPos += 1
                    else:
                        break
                self.students.insert(insertPos, new_student)
        print("\nStudent not found\n")
        
    #delete elem func
    def deleteElement(self):
        name = Utils.saniitizing(input("Enter name to delete: "))
        for index, student in enumerate(self.students):
            if name == student.name:
                del self.students[index]

    #print all list func
    def printAllList(self):
        for student in self.students:
            str_for_print = "Student name is {}, Phone is {}, Mail is {}, Age is {}".format(
                student.name, student.phone, student.mail, student.age)
            print(str_for_print)
