import sys
from datetime import datetime
import math
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @property
    def dob(self):
        return self.__dob

    def __str__(self):
        return f"{self.__id} \t| {self.__name:20} \t| {self.__dob}"


class Course:
    def __init__(self, c_id, name):
        self.__id = c_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__id} \t| {self.__name}"


class StudentMark:
    # Relation: Student (Object) - Course (Object) - Mark 
    def __init__(self, student_obj, course_obj, mark_val):
        self.__student = student_obj 
        self.__course = course_obj  
        self.__value = mark_val

    @property
    def student(self):
        return self.__student

    @property
    def course(self):
        return self.__course

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f"{self.__student.name} - {self.__course.name}: {self.__value}"
    



class SchoolSystem:
    def __init__(self):
        # Dictionary easy to find by ID: {id: Object}
        self.__students = {} 
        self.__courses = {}
        
        # Dictionary with key as Tuple (student_id, course_id) để map điểm
        # Structure: { ('SV01', 'PY1'): object_StudentMark }
        self.__marks_map = {} 

    # Helkper function
    def check_data(self):
        if not self.__students:
            print("No students data.")
            return False
        if not self.__courses:
            print(" No courses data.")
            return False
        return True

    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    # Feature functions
    def add_students(self):
        try:
            num = int(input("\nNumber of students to add: "))
            for i in range(num):
                print(f"\nStudent {i+1}:")
                s_id = input("  ID: ").strip().upper()
                if s_id in self.__students:
                    print(" ID exists. Skipping.")
                    continue
                
                name = input("  Name: ").strip()
                
                dob = ""
                while True:
                    dob = input("  DOB (DD-MM-YYYY): ").strip()
                    if self.validate_date(dob): break
                    print("  Invalid format.")

                # Tạo Object và lưu vào Dict
                new_student = Student(s_id, name, dob)
                self.__students[s_id] = new_student
                print(f"   Added {name}")

        except ValueError:
            print("  Please enter a number.")

    def add_courses(self):
        try:
            num = int(input("\nNumber of courses to add: "))
            for i in range(num):
                print(f"\nCourse {i+1}:")
                c_id = input("  ID: ").strip().upper()
                if c_id in self.__courses:
                    print("   ID exists. Skipping.")
                    continue
                
                name = input("  Name: ").strip()
                
                new_course = Course(c_id, name)
                self.__courses[c_id] = new_course
                print(f" Added {name}")
        except ValueError:
            print("  Please enter a number.")

    def input_marks(self):
        if not self.check_data(): return

        self.list_courses()
        course_id = input("\nEnter Course ID to grade: ").strip().upper()
        
        # Lấy object Course từ Dict (O(1))
        selected_course = self.__courses.get(course_id)
        if not selected_course:
            print(" Course not found.")
            return

        print(f"\n--- Grading: {selected_course.name} ---")
        
        # Duyệt qua các object sinh viên trong Dict
        for s_id, student_obj in self.__students.items():
            try:
                val = input(f"  Mark for {student_obj.name} ({s_id}): ").strip()
                if not val: continue
                
                mark_val = math.floor(float(val), )
                if 0 <= mark_val <= 20:
                    # Tạo Mark Object kết nối 2 Object kia
                    mark_obj = StudentMark(student_obj, selected_course, mark_val)
                    
                    # Lưu vào map với key là bộ đôi ID (Optimized)
                    key = (s_id, course_id)
                    self.__marks_map[key] = mark_obj
                else:
                    print("   Mark must be 0-20.")
            except ValueError:
                print("   Invalid mark.")

    def list_students(self):
        print("\n--- Student List ---")
        print("ID \t| Name \t\t\t| DOB")
        print("-" * 50)
        for s in self.__students.values():
            print(s)

    def list_courses(self):
        print("\n--- Course List ---")
        print("ID \t| Name")
        print("-" * 30)
        for c in self.__courses.values():
            print(c)

    def show_marks(self):
        if not self.check_data(): return

        self.list_courses()
        course_id = input("\nView marks for Course ID: ").strip().upper()
        
        if course_id not in self.__courses:
            print(" Course not found.")
            return

        print(f"\n--- Mark Sheet: {self.__courses[course_id].name} ---")
        print("ID \t| Student Name \t\t| Mark")
        print("-" * 45)

        found = False
        # Duyệt qua danh sách sinh viên để hiển thị
        for s_id, s_obj in self.__students.items():
            # O(1) nhờ Tuple Key
            key = (s_id, course_id)
            mark_obj = self.__marks_map.get(key)
            
            # Lấy điểm nếu có, không thì gạch ngang
            display = mark_obj.value if mark_obj else "--"
            
            print(f"{s_id} \t| {s_obj.name:20} \t| {display}")
            if mark_obj: found = True
        
        if not found:
            print("\n(No marks yet)")
    def avg_gpa(self):
        total_gpa = 0
        count = 0
        for m in self.__marks_map.values():
            total_gpa += m
            count += 1
        return total_gpa / count
    

if __name__ == "__main__":
    system = SchoolSystem()
    
    while True:
        print("\n=== ULTIMATE STUDENT MANAGER ===")
        print("1. Add Students")
        print("2. Add Courses")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks")
        print("0. Exit")
        
        choice = input("Select: ").strip()
        
        if choice == '1': system.add_students()
        elif choice == '2': system.add_courses()
        elif choice == '3': system.input_marks()
        elif choice == '4': system.list_students()
        elif choice == '5': system.list_courses()
        elif choice == '6': system.show_marks()
        elif choice == '0':
            print("Bye bye")
            sys.exit(0)
        else:
            print("Invalid selection.")