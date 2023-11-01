students = []

with open("topic_06\students.txt") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        
        student = {} 
        student["name"] = name
        student["mark"] = mark        
        students.append(student)

for student in sorted(students, key=lambda student: student["mark"]):
    print(f"Name is {student['name']} mark is {student['mark']}") 


