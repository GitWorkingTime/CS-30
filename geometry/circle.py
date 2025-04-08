import math

class Circle():
    def __init__(self, name, radius, height = 0):
        self.name = name
        self.radius = radius
        self.height = height
        pass

    def get_name(self):
        return f"The name is {self.name}"
    
    def print_area(self):
        circleArea = math.pi * (self.radius**2)
        rectangleArea = (2 * math.pi * self.radius) * self.height
        surface = (2 * circleArea) + rectangleArea
        print(f"The area is {surface}")

    def print_circumference(self):
        circumerference = 2 * math.pi * self.radius
        print(f"The circumeference is {circumerference}")
    
    def print_volume(self):
        area = math.pi * (self.radius**2)
        volume = area * self.height
        print(f"The volume is {volume}")