import math

class Circle():
    def __init__(self, name, radius, height = 0):
        self.name = name
        self.radius = abs(radius)
        self.height = abs(height)
        pass

    def get_name(self):
        return self.name
    
    def print_area(self):
        circleArea = math.pi * (self.radius**2)
        rectangleArea = (2 * math.pi * self.radius) * self.height
        surface = round((2 * circleArea) + rectangleArea, 2)
        print(f"The {self.name}'s Area is equal to {surface} meters squared")
        return surface

    def print_circumference(self):
        circumerference = round(2 * math.pi * self.radius, 2)
        print(f"The {self.name}'s Circumeference is equal to {circumerference} meters")
        return circumerference
    
    def print_volume(self):
        area = math.pi * (self.radius**2)
        volume = round(area * self.height, 2)
        if self.height == 0:
            print(f"The {self.name} is not a cylinder. Volume cannot be computed")
        else:
            print(f"The {self.name} is a cylinder. It has a volume of {volume} cubic meters")
        return volume