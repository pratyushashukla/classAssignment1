class Person:
    # Parameterized Constructor for initializing class variables
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age  # Declared private class property
        self.gender = gender

    # A class method printing greetings from the Person
    def say_hello(self):
        print(f"Hello, My name is",self.name,"Hope you are doing fine!!!")

    # A class method used for calculating whether the person is an adult or not
    def is_adult(self):
        if self.__age >=18:
            return True
        else:
            return False
    def accessAge(self):
        return self.__age
class Student(Person):
    def __init__(self,name, age, gender,studentId, courseName):
        Person.__init__(self,name,age,gender)
        self.student_id = studentId
        self.course = courseName
    def say_hello(self):
        print("Hello from the Student class")
        print(" My name is",self.name,"Hope you are doing fine!!!")
    def displayStudentInfo(self):
        print(f"Student with name",self.name,"and student ID:",self.student_id,"has enrolled for", self.course, "course")

class Teacher(Student):
    def __init__(self,name, age, gender,teacherId, subject):
        Person.__init__(self,name,age,gender)
        self.teacher_id = teacherId
        self.subject = subject

    def say_hello(self):
        print("Hello from Teacher class, Hope you are doing fine!!!")

    def displayTeacherInfo(self):
        print(f"Teacher with name",self.name,"and teacher ID:",self.teacher_id,"teaches", self.subject, "subject to the Lambton students")

''' Task 1 '''
personObj = Person("Pratyusha",23,"Female")
personObj.say_hello()
personObj.is_adult()

print("Accessing the private variable age through method:",personObj.accessAge())

''' Task 2 '''
studObj = Student("Pratyusha",23,"Female","c0865904","Full Stack Software Development")
studObj.say_hello()
studObj.is_adult()
studObj.displayStudentInfo()

''' Task 3 '''

teacherObj = Teacher("Ishant Gupta",35,"Male","t0865804","Python Programming")
teacherObj.say_hello()
teacherObj.displayTeacherInfo()


