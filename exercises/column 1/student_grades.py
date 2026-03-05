student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"'{name}' got an {grade}.")

def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"'{name}' was removed.")
    else:
        print(f"'{name}' was not found.")

def display_students():
    print("Students:")
    for name, grade in student_grades.items():
        print(f"'{name}', Grade: {grade}")

def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"'{name}' now has {grade}.")
    else:
        print(f"'{name}' was not found.")

def find_grade(name):
    if name in student_grades:
        print(student_grades.get(name))
    else:
        print(f"'{name}' not found.")

def average_grade():
    total_sum = sum(student_grades.values())
    count = len(student_grades)
    average = total_sum / count
    print(f"The average is: {average}")
        


add_student("Alice", 80)
add_student("Joe", 90)
add_student("Jack", 85)
add_student("Grace", 96)

display_students()

remove_student("Cameron")
remove_student("Joe")

update_grade("Alice", 87)

display_students()

find_grade("Jack")

average_grade()