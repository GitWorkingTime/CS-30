import math

class Coin():
    def __init__(self, coin_name, radius, material, value):
        #Initialize instance variables:
        self.name = coin_name
        self.radius = radius
        self.material = material
        self.value = value
        pass

    def __repr__(self):
        return f"The coin is {self.name} and has a radius of {self.radius} mm.\nIt's composition is {self.material} and is worth {self.value} cents."

    def get_circumference(self):
        """
        Calculates the circumference of the instance
        """
        #Uses the formula '2πr' to calculate circumference
        circumference = 2 * math.pi * self.radius

        #Rounds the circumference value to 2 decimal places
        circumference = round(circumference, 2)
        
        #Returns the circumeference through an f string
        return f"The {self.name}'s circumferance is {circumference} mm.\nA {self.name} is made up of {self.material} and has a value of {self.value} cents"
        
    
    def get_area(self):
        """
        Calculates the area of a face of the instance
        """
        #Uses the formula 'π(r^2)' to find the surface area of a face on the coin
        area = math.pi * (self.radius**2)

        #Rounds the area value to 2 decimal places
        area = round(area, 2)

        #Returns the area value through an f string
        return f"The surface area of one side of a {self.name} is {area} mm^2.\nA {self.name} is made up of {self.material} and has a value of {self.value} cents"