class Student():
    def __init__(self, name, module1Grade, module2Grade, module3Grade, average, remainingCourse):
        self.name = name
        self.module1Grade = module1Grade
        self.module2Grade = module2Grade
        self.module3Grade = module3Grade
        average = (module1Grade + module2Grade + module3Grade) / 3
        self.average = average
        self.remainingCourse = remainingCourse
        pass

    def print(self):
        print(f"Name: {self.name}")


        pass

student = Student("Mark", 90, 65, 80, 0, "English")
print(student.name)
print(student.module1Grade)
print(student.module2Grade)
print(student.module3Grade)
print(student.average)
print(student.remainingCourse)
student.print()

class Teacher():
    def __init__(self, name, subject, apple, suitColour):
        self.name = name
        self.subject = subject
        self.apple = apple
        self.suitColour = suitColour
        pass


teacher = Teacher("Mr. L", "Math", "Granny Smith apple", "Black")

