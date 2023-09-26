class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def displayInfo(self):
        print(f"Student: {self.name}, ID: {self.id}")

class Skill(Student):
    def __init__(self, id, name, skill):
        Student.__init__(self, id, name)
        self.skill = skill


    def displaySkill(self):
        print(f"Student's skill is:",self.skill)

class Subject(Student):
    def __init__(self,  id, name, subjectName):
        Student.__init__(self, id, name)
        self.subjectName = subjectName
    def displayInformation(self):
        super().displayInfo()

testObj = Subject(20,'Pratyusha','Python')
testObj.displayInformation()
