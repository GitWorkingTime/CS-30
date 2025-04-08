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
        surfaceArea = (2 * baseArea) + (2 * side1Area) + (2 * side2Area)
        print(f"The surface area is {surfaceArea}")
    
    def print_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.length)
        print(f"The perimeter is {perimeter}")

    def print_volume(self):
        volume = self.height * self.width * self.length
        print(f"The volume is {volume}")

    pass