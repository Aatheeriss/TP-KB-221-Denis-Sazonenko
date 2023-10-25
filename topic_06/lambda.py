students = []

with open("topic_06\students.txt") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        
        student = {} 
        student["name"] = name
        student["mark"] = mark        
        students.append(student)

def get_mark(student):
    return student["mark"]

for student in sorted(students, key=get_mark):
    print(f"Name is {student['name']} mark is {student['mark']}") 