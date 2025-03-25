class Student():
    """
    Creates a class with attributes intialized in the '__init__' constructor
    """

    def __init__(self, name, module1Grade, module2Grade, module3Grade, average, remainingCourse):
        """
        Creates attributes to use when creating an instance/object of this class.

        Attributes:
            self -> this class
            name -> the name of the student
            module1Grade -> the grade for the first module
            module2Grade -> the grade for the second module
            module3Grade -> the grade for the third module
            average -> the average among all of the modules
            remaininingCourse -> the course the student has left before graduating
        """

        #Initialize attributes
        self.name = name 
        self.module1Grade = module1Grade
        self.module2Grade = module2Grade
        self.module3Grade = module3Grade

        #Calculate the average by adding all of the module grades and dividing by 3
        average = (module1Grade + module2Grade + module3Grade) / 3

        #use '//' operator to round down
        self.average = average // 1 
        self.remainingCourse = remainingCourse

    def printAttributes(self):
        """
        Function/method to print out the instance's attributes
        """
        print(f"Name: {self.name}\nModule 1 Grade: {self.module1Grade}\nModule 2 Grade: {self.module2Grade}\nModule 3 Grade: {self.module3Grade}\nAverage: {self.average}\nRemaining Course: {self.remainingCourse}")

#Creates instances
student1 = Student("Mark", 90, 65, 80, 0, "English")
student2 = Student("Ethan", 100, 100, 100, 0, "Math")
student3 = Student("Imaad", 90, 87, 95, 0, "Music")

#Puts all of the instances into a list
students = [student1, student2, student3]

class Teacher():
    """
    Creates a class with attributes intialized in the '__init__' constructor
    """
    def __init__(self, name, subject, apple, suitColour, classAvg, diplomaAvg):
        """
        Creates attributes to use when creating an instance/object of this class.

        Attributes:
            self -> this class
            name -> the name of the teacher
            subject -> the subject the teacher teaches
            apple -> the teacher's favourite type of apple
            suitColour -> the teacher's favourite suit colour
            classAvg -> the teacher's overall class average
            diplomaAvg -> the teacher's class diploma average
        """
        
        #Initialize the attributes
        self.name = name
        self.subject = subject
        self.apple = apple
        self.suitColour = suitColour
        self.classAvg = classAvg
        self.diplomaAvg = diplomaAvg

    def printAttributes(self):
        """
        Prints out all of the attributes of this one specific instance
        """
        print(f"Name: {self.name}\nSubject: {self.subject}\nFavourite type of apple: {self.apple}\nFavourite suit colour: {self.suitColour}\nClass average: {self.classAvg}\nDiploma average: {self.diplomaAvg}")

#Creates the instances
teacher1 = Teacher("Mr. L", "Math", "Granny Smith apple", "Black", 66, 90)
teacher2 = Teacher("Mr. Seuss", "English", "Honeycrisps", "Purple", 80, 100)
teacher3 = Teacher("Mr. Him", "Drama", "Jazz apples", "Blue", 76, 85)

#Put all of the instances into a list
teachers = [teacher1, teacher2, teacher3]

