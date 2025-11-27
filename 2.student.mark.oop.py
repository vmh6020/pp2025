class Student:
    def __init__(self, i, n, a):
        self.__id = i
        self.__name = n
        self.__age = a
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    
class Course:
    def __init__(self, i, n):
        self.__id = i
        self.__name = n
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id
    
class StudentMark:
    def __init__(self, student, course_name, course_mark):
        self.student = student
        self.course_name = course_name
        self.course_mark = course_mark
    def get_student(self):
        return self.__name
    def set_student(self, new_name):
        self.__name = new_name
    def get_course_name(self):
        return self.__id
    def set_course_name(self, new_id):
        self.__id = new_id
    def get_course_mark(self):
        return self.__age
    def set_course_mark(self, new_age):
        self.__age = new_age