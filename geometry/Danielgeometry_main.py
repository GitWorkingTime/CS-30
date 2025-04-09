from DanielCircle import *
from Danielrectangle import *

# ---- Asserts/Testing ----#
circle1 = Circle("Circle1", 5)
circle2 = Circle("Circle2", 10, 2)
circle3 = Circle("Circle3", 3, -3)
rect1 = Rectangle("Rect1", 10, 2)
rect2 = Rectangle("Rect2", -10, -10)
rect3 = Rectangle("Rect3", 2, 3, 5)
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

    assert(rect1.get_name()) == "Rect1"
    assert(rect1.print_area()) == 40
    assert(rect1.print_perimeter()) == 24
    assert(rect1.print_volume()) == 0

    assert(rect2.get_name()) == "Rect2"
    assert(rect2.print_area()) == 200
    assert(rect2.print_perimeter()) == 40
    assert(rect2.print_volume()) == 0
    
    assert(rect3.get_name()) == "Rect3"
    assert(rect3.print_area()) == 62
    assert(rect3.print_perimeter()) == 10
    assert(rect3.print_volume()) == 30
    
    print("finished\n")


class Main():
    """
    Contains the main functionality
    """
    #---- Call tests ----#
    tests()

    #---- Create the two lists and run through each methods ----#
    manHole = Circle("Man Hole", 0.5)
    towerOfPisa = Circle("Tower Of Pisa", 20, 80)
    circles = [manHole, towerOfPisa]

    #Go through each item in the lists
    for i in range(len(circles)):
        #Print the name
        print(f"The {circles[i].get_name()} has the following properties")

        #Call each method
        circles[i].print_area()
        circles[i].print_circumference()
        circles[i].print_volume()

        #Create a new line for organization
        print("")

    paper = Rectangle("Paper", 0.126, 0.28)
    printer = Rectangle("Printer", 0.36, 0.32, 0.24)
    rectangles = [paper, printer]

    #Go through each item in the lists
    for i in range(len(rectangles)):
        #Print the name
        print(f"The {rectangles[i].get_name()} has the following properties")

        #Call each method        
        rectangles[i].print_area()
        rectangles[i].print_perimeter()
        rectangles[i].print_volume()

        #Create a new line for organization
        print("")
    
    #---- For Searching ----#
    while True:
        #Ask the user
        print("What circle do you what to search for?")

        #Get user Input
        circleInput = input()
        circleInput = circleInput.strip()
        
        #Flag variable for certain print messages
        found = False
        
        #Go through each item in the list
        for i in range(len(circles)): 

            #Check if the input matches the name
            if circleInput == circles[i].get_name():
                #Print the name
                print(f"The {circles[i].get_name()} has the following properties")

                #Call each method
                circles[i].print_area()
                circles[i].print_circumference()
                circles[i].print_volume()

                #Create a new line for organization
                print("")
                
                #Change flag variable
                found = True

                #Leave the loop
                break
        
        #If not found, say not found
        if found == False:
            print("Not Found!")
        else:
            found = False
        
        #Ask the user
        print("What rectangle do you what to search for?")

        #Get user Input        
        rectangleInput = input()
        rectangleInput = rectangleInput.strip()

        #Go through each item in the list
        for i in range(len(rectangles)):
            #Check if the input matches the name
            if rectangleInput == rectangles[i].get_name():
                #Print the name
                print(f"The {rectangles[i].get_name()} has the following properties")

                #Call each method                
                rectangles[i].print_area()
                rectangles[i].print_perimeter()
                rectangles[i].print_volume()

                #Create a new line for organization
                print("")

                #Change flag variable
                found = True
                
                #Leave the loop
                break
        
        #If not found, say it's not found
        if found == False:
            print("Not Found!")
        else:
            found = False