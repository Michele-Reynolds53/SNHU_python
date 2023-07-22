# create function add_grade
def add_grade(student_grades):
    print('Entering grade. \n')
    name, grade = input(grade_prompt).split()
    student_grades[name] = grade

# create function delete_name
def delete_name(student_grades):
    print('Deleting grade.\n')
    name = input(delete_prompt)
    if name in student_grades:
        del student_grades[name]
    else:
        print('Name not found in the student grades.')


# create function print_grades

def print_grades(student_grades):
    print('Printing grades.\n')
    for name, grade in student_grades.items():
        print(name, 'has a', grade)

# dictionary to store student names and grades and menu prompt to make changes
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
delete_prompt = "Enter name to delete:\n"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

command = input(menu_prompt).lower().strip()

# options to alter student records
while command != '4':  # Exit when the user enters '4'
    if command == '1':
        add_grade(student_grades)
    elif command == '2':
        delete_name(student_grades)
    elif command == '3':
        print_grades(student_grades)
    else:
        print('Unrecognized command.\n')

    command = input().lower().strip()

