import math

class Circle():
    """
    a circle class that takes in three constructor variables:
        name (str) - Name of the instance
        radius (int/float) - The radius of the circle
        height (int/float) - The height of the circle

    4 methods:
        get_name() -> returns name
        print_area() -> prints the surface area area and returns it
        print_circumference() -> prints the circumference and returns it
        print_volume() -> prints the volume and returns it
    """

    def __init__(self, name, radius, height = 0):
        #Initialize instance variables
        self.name = name

        #Take the absolute value of the numbers to account for negative numbers
        self.radius = abs(radius)
        self.height = abs(height)

    def get_name(self):
        #Returns the instance's name
        return self.name
    
    def print_area(self):
        #Uses the formula 'πr^2' to find the area of the circles
        circleArea = math.pi * (self.radius**2)

        #Uses the formula '2πrh' to find the area of the sides of the cylinder (if height != 0)
        rectangleArea = (2 * math.pi * self.radius) * self.height

        #Add the circleArea and rectangleArea and round it to 2 decimal places
        surface = round((2 * circleArea) + rectangleArea, 2)

        #Print the surface area
        print(f"The {self.name}'s Area is equal to {surface} meters squared")

        #Return the surface area
        return surface

    def print_circumference(self):
        #Uses the formulae '2πr' to find the circumference and rounded to 2 decimal places
        circumerference = round(2 * math.pi * self.radius, 2)

        #Prints the circumference
        print(f"The {self.name}'s Circumeference is equal to {circumerference} meters")

        #Returns the circumference
        return circumerference
    
    def print_volume(self):
        #Uses the formulae 'πhr^2' to find the volume of the instance
        area = math.pi * (self.radius**2)

        #Rounded to 2 decimal places
        volume = round(area * self.height, 2)

        #Double checks to see if the instance is an instance or a cylinder
        if self.height == 0:
            print(f"The {self.name} is not a cylinder. Volume cannot be computed")
        else:
            print(f"The {self.name} is a cylinder. It has a volume of {volume} cubic meters")

        #Return the volume
        return volume