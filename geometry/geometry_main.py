from circle import *
from rectangle import *

manHole = Circle("Man Hole", 0.5)
towerOfPisa = Circle("Tower Of Pisa", 20, 80)
circles = [manHole, towerOfPisa]

for i in range(len(circles)):
    print(f"The {circles[i].get_name()} has the following properties")
    circles[i].print_area()
    circles[i].print_circumference()
    circles[i].print_volume()
    print("")

paper = Rectangle("Paper", 0.126, 0.28)
printer = Rectangle("Printer", 0.36, 0.32, 0.24)
rectangles = [paper, printer]

for i in range(len(rectangles)):
    print(f"The {rectangles[i].get_name()} has the following properties")
    rectangles[i].print_area()
    rectangles[i].print_perimeter()
    rectangles[i].print_volume()
    print("")

print("What circle do you what to search for?")
circleInput = input()
circleInput = circleInput.strip()
found = False

for i in range(len(circles)):
    if circleInput == circles[i].get_name():
        print(f"The {circles[i].get_name()} has the following properties")
        circles[i].print_area()
        circles[i].print_circumference()
        circles[i].print_volume()
        print("")
        found = True
        break
if found == False:
    print("Not Found!")
else:
    found = False

print("What rectangle do you what to search for?")
rectangleInput = input()
rectangleInput = rectangleInput.strip()

for i in range(len(rectangles)):
    if rectangleInput == rectangles[i].get_name():
        print(f"The {rectangles[i].get_name()} has the following properties")
        rectangles[i].print_area()
        rectangles[i].print_perimeter()
        rectangles[i].print_volume()
        print("")
        found = True
        break
if found == False:
    print("Not Found!")
else:
    found = False