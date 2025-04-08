class Rectangle():
    def __init__(self, name, width, length, height = 0):
        self.name = name
        self.width = width
        self.length = length
        self.height = height

    def get_name(self):
        return self.name

    def print_area(self):
        baseArea = self.width * self.length
        side1Area = self.width * self.height
        side2Area = self.length * self.height
        surfaceArea = round((2 * baseArea) + (2 * side1Area) + (2 * side2Area), 2)
        print(f"The {self.name}'s Surface Area is {surfaceArea} meters squared")
    
    def print_perimeter(self):
        perimeter = round((2 * self.width) + (2 * self.length), 2)
        print(f"The {self.name}'s Perimeter is equal to {perimeter} meters")

    def print_volume(self):
        volume = round(self.height * self.width * self.length, 2)
        if self.height == 0:
            print(f"The {self.name} is not a rectangular prism. Volume cannot be computed")
        else:
            print(f"The {self.name} is a rectangular prism. It has a volume of {volume} cubic meters")
    pass