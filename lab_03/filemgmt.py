from student import Student
from studentList import StudentList
import csv

class FileMGMT:

    #read from file func
    @staticmethod
    def ReadFromFile(file_name):
        list_of_students = StudentList()
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["name"], row["phone"], row["mail"], row["age"])
                list_of_students.students.append(student)
        return list_of_students
    
    #file save func
    @staticmethod
    def FileSave(list_of_students, file_name):
        if not list_of_students.students:
            print("\n----No data to save.----\n")
            return
        else:   
            with open(file_name, "w", newline='') as csvfile:
                fieldnames = ["name", "phone", "mail", "age"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in list_of_students.students:
                    writer.writerow({"name": row.name, "phone": row.phone, "mail": row.mail, "age": row.age}) 
            