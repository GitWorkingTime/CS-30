from DanielCircle import *
from Danielrectangle import *

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

circle1 = Circle("Circle1", 5)
circle2 = Circle("Circle2", 10, 2)
circle3 = Circle("Circle3", 3, -3)
def tests():
    print("testing...")
    assert(circle1.get_name()) == "Circle1"
    assert(circle1.print_area()) == 157.08
    assert(circle1.print_circumference()) == 31.42
    assert(circle1.print_volume()) == 0.0

    assert(circle2.get_name()) == "Circle2"
    assert(circle2.print_area()) == 753.98
    assert(circle2.print_circumference()) == 62.83
    assert(circle2.print_volume()) == 628.32

    assert(circle3.get_name()) == "Circle3"
    assert(circle3.print_area()) == 113.1
    assert(circle3.print_circumference()) == 18.85
    assert(circle3.print_volume()) == 84.82
    print("finished\n")

    pass

tests()

class Main():
    while True:
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