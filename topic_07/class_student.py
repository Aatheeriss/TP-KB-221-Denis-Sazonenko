class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
students = [
    Student("Artem", 18),
    Student("Denis", 19),
    Student("Misha", 17),
    Student("Anna", 16)
]

sorted_students = sorted(students, key=lambda student: student.age)
for student in sorted_students:
    print(f"Student: {student.name}, Age: {student.age}")