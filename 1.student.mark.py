import sys
from datetime import datetime

students = {}
courses = {}
marks = {}

# input functions

def input_students():
    print("\n--- Input Student Info ---")
    while True:
        try:
            num_students = int(input("Enter the number of students to add: "))
            if num_students > 0:
                break
            print("The number must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(num_students):
        print(f"\n Student number {i+1}:")
        student_id = input("  Enter Student ID: ").strip().upper()
        if student_id in students:
            print(f"  ID {student_id} already exists. Skipping.")
            continue
            
        student_name = input("  Enter Student Name: ").strip()
        while True:
            try:
                dob_str = input("  Enter Date of Birth (DD-MM-YYY): ").strip()
                datetime.strptime(dob_str, '%d-%m-%Y')
                break
            except ValueError:
                print("  Invalid date format. Please use YYYY-MM-DD.")
        
        students[student_id] = {'name': student_name, 'dob': dob_str}
        print(f"  Successfully added: {student_id} - {student_name}")

def input_courses():
    print("\n--- Input Course Info ---")
    while True:
        try:
            num_courses = int(input("Enter the number of courses to add: "))
            if num_courses > 0:
                break
            print("The number must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(num_courses):
        print(f"\nCourse number {i+1}:")
        course_id = input("  Enter Course ID: ").strip().upper()
        if course_id in courses:
            print(f"  ID {course_id} already exists. Skipping.")
            continue
            
        course_name = input("  Enter Course Name: ").strip()
        courses[course_id] = course_name
        print(f"  Successfully added: {course_id} - {course_name}")

def check_empty(data_dict, item_name):
    if not data_dict:
        print(f"No {item_name} information has been entered.")
        return True
    return False

def input_marks_for_course():
    if check_empty(courses, "courses"):
        return
    if check_empty(students, "students"):
        return

    list_courses()

    course_id = input("\nSelect the Course ID to input marks for: ").strip().upper()
    
    if course_id not in courses:
        print("Course ID not found.")
        return

    course_name = courses[course_id]
    print(f"\n--- Input marks for course: {course_name} ({course_id}) ---")

    for student_id, student_data in students.items():
        student_name = student_data['name']
        while True:
            try:
                mark_input = input(f"  Enter mark for {student_name} ({student_id}): ").strip()
                if not mark_input:
                    print("  Skipping this student.")
                    break
                    
                mark = float(mark_input)
                if 0 <= mark <= 20:
                    if student_id not in marks:
                        marks[student_id] = {}
                    
                    marks[student_id][course_id] = mark
                    print("  Mark saved.")
                    break
                else:
                    print("  Mark must be between 0 and 20.")
            except ValueError:
                print("  Invalid input. Please enter a number.")

#listing functions

def list_students():
    print("\n--- List of Students ---")
    if check_empty(students, "students"):
        return

    print("ID \t| Student Name \t\t| Date of Birth")
    print("-" * 50)
    for student_id, data in students.items():
        print(f"{student_id} \t| {data['name']:20} \t| {data['dob']}")

def list_courses():
    print("\n--- List of Courses ---")
    if check_empty(courses, "courses"):
        return
    
    print("ID \t| Course Name")
    print("-" * 30)
    for course_id, course_name in courses.items():
        print(f"{course_id} \t| {course_name}")

def show_student_marks_for_course():
    if check_empty(courses, "courses") or check_empty(students, "students"):
        return
    
    list_courses()
    course_id = input("\nSelect the Course ID to view marks for: ").strip().upper()

    if course_id not in courses:
        print("Course ID not found.")
        return
    
    course_name = courses[course_id]
    print(f"\n--- Marks Table for Coruses: {course_name} ({course_id}) ---")
    
    found_marks = False
    print("ID \t| Student Name \t\t| Mark")
    print("-" * 40)
    
    for student_id, student_data in students.items():
        student_name = student_data['name']
        mark = marks.get(student_id, {}).get(course_id, "None")
        
        if mark != "None":
            found_marks = True
            
        print(f"{student_id} \t| {student_name:20} \t| {mark}")
        
    if not found_marks:
        print("No marks have been entered for this course yet.")


def main_menu():
    print("--- Student Mark Management System ---")
    while True:
        print("\n==========================")
        print("         MAIN MENU")
        print("==========================")
        print("1. Add Students")
        print("2. Add Courses")
        print("3. Input Marks for a Course")
        print("4. View List of Students")
        print("5. View List of Courses")
        print("6. View Student Marks by Course")
        print("0. Exit Program")
        
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks_for_course()
        elif choice == '0':
            print("Bybye")
            sys.exit(0)
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main_menu()