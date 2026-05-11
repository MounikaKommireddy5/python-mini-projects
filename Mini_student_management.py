students = []

def add_student(name):
    students.append(name)

def show_students():
    print("Student List:")
    for s in students:
        print(s)

add_student("Mounika")
add_student("Ravi")
add_student("Anil")

show_students()
