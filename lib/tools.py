import json
from classes.Student import Student


# I need a function that shows a main menu and gets their chosenn option - List Students, Add a Student, and Exit
def showMainMenu():
    # Using a triple """ to allow for multi-line strings
    errorMessage = "\n*** You must enter a valid number option ***"
    choice = input("""
          Please type an option from the list below (Enter the option number):
          1. List Students
          2. Add a Student
          3. Exit
          
          -> """)

    try:
        menuOption = int(choice)

        if menuOption == 1:
            listStudents()
        elif menuOption == 2:
            addStudent()
        elif menuOption == 3:
            print("\n--- Thanks for using the Student Tracker! ---\n")
            exit()
        else:
            print(errorMessage)

        showMainMenu()
    except ValueError:
        print(errorMessage)
        showMainMenu()


# I need a function to retrieve the students from the data file and print them out in a nicely formatted manner
def listStudents():
    try:
        with open('data.json', 'r') as file:
            students = json.load(file)

            print("\nStudent List:")

            for student in students:
                print(
                    f"\nFirst Name: {student['first_name']}\nLast Name: {student['last_name']}\nCourse: {student['course_type']}\nUniversity: {student['university']}\n----"
                )

            if not len(students):
                print("\nNo students have been added")

    except FileNotFoundError:
        print("The students.json file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the students.json file.")


# I need a function to get the information for a student from the user and add that student to the data file
def addStudent():
    first_name = input("Please enter the first name of the student: ")
    last_name = input("Please enter the last name of the student: ")
    course_type = input("Please enter the course type for the student: ")
    university = input("Please enter the university for the student: ")

    if (not first_name or not last_name or not course_type or not university):
        print("You must enter all of the student information")
        addStudent()

    student = Student(first_name, last_name, course_type, university)

    try:
        # Read existing data
        with open('data.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from the data.json file.")
        return

    students.append(student.toDictionary())

    with open('data.json', 'w') as file:
        json.dump(students, file, indent=4)

    print("\nStudent added successfully.\n")
