import math

class Coin():
    def __init__(self, coin_name, radius, material, value):
        self.name = coin_name
        self.radius = radius
        self.material = material
        self.value = value
        pass

    def __repr__(self):
        return f"The coin is {self.name} and has a radius of {self.radius} mm.\nIt's composition is {self.material} and is worth {self.value} cents."

    def get_circumference(self):
        circumference = 2 * math.pi * self.radius
        circumference = round(circumference, 2)
        return f"The {self.name}'s circumferance is {circumference} mm.\nA {self.name} is made up of {self.material} and has a value of {self.value} cents"
        
    
    def get_area(self):
        area = math.pi * (self.radius**2)
        area = round(area, 2)
        return f"The surface area of one side of a {self.name} is {area} mm^2.\nA {self.name} is made up of {self.material} and has a value of {self.value} cents"