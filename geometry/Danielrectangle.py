class Rectangle():
    """
    a rectangle class that takes in three constructor variables:
        name (str) - Name of the instance
        width (int/float) - The width of the rectangle
        height (int/float) - The height of the rectangle
        length (int/float) - The length of the rectangle

    4 methods:
        get_name() -> returns name
        print_area() -> prints the surface area area and returns it
        print_perimeter() -> prints the perimeter and returns it
        print_volume() -> prints the volume and returns it
    """
    
    def __init__(self, name, width, length, height = 0):
        #Initialize the instance's variables
        self.name = name

        #Take the absolute to account for negative numbers
        self.width = abs(width)
        self.length = abs(length)
        self.height = abs(height)

    def get_name(self):
        #Return the instance's name
        return self.name

    def print_area(self):
        #Uses the formula 'wl', 'wh', 'lh' to find the area of each side
        baseArea = self.width * self.length
        side1Area = self.width * self.height
        side2Area = self.length * self.height

        #Add them all up and round to 2
        surfaceArea = round((2 * baseArea) + (2 * side1Area) + (2 * side2Area), 2)

        #Print the surface area
        print(f"The {self.name}'s Surface Area is {surfaceArea} meters squared")

        #Return the surface area
        return surfaceArea
    
    def print_perimeter(self):
        #Uses the formula 'wl' of the base rectangle to find the perimeter. Rounded to 2 decimal places
        perimeter = round((2 * self.width) + (2 * self.length), 2)

        #Print the perimeter
        print(f"The {self.name}'s Perimeter is equal to {perimeter} meters")

        #Return the perimeter
        return perimeter

    def print_volume(self):
        #Uses the formula 'wlh' to find the volume. Rounded to 2 decimal places
        volume = round(self.height * self.width * self.length, 2)

        #Double check if the instance is a rectangle or a rectangular prism
        if self.height == 0:
            print(f"The {self.name} is not a rectangular prism. Volume cannot be computed")
        else:
            print(f"The {self.name} is a rectangular prism. It has a volume of {volume} cubic meters")
        
        #Return volume
        return volume