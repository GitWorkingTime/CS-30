import math

# ---- Math class ----#
class Mathings:
    """
    Class 'Mathings' contains operations that include:
        Addition
        Subtraction
        Multiplication
        Division
        Using Pythagorean Theorem
        Taking the power of a number
        Getting the Kth digit of a number
        Three short answers
    """

    @staticmethod
    def addition(x, y):
        #Add the two numbers
        return x + y

    @staticmethod
    def subtraction(x, y):
        #Subtract the two numbers
        return x - y
    
    @staticmethod
    def multiplication(x, y):
        #Multiply the numbers
        return x * y

    @staticmethod
    def division(x, y):
        #Can't divide by 0
        if y == 0:
            return None

        #Divide the two numbers. The result is rounded to 5 decimal places
        return round(x / y, 5)
    
    @staticmethod
    def pythagoras(x, y):
        #Take the square of the first side
        a = x**2

        #Take the square of the second side
        b = y**2

        #Take the square root of the sum of the first and second sides
        c = math.sqrt(a + b)

        #Returns the results rounded to 5 decimal places
        return round(c, 5)

    @staticmethod
    def pow(x, y):
        #Returns the first number to the power of the second number
        return round(x**y, 5)

    @staticmethod
    def getKthDigit(n, k):
        """
        Operates on a number to find the digit of a number given a specific place value

        Args:
            n (int) -> the number we are looking at
            k (int) -> the place value we are looking for
        """

        #Take the absolute value of the number. Negatives make this wonky
        n = abs(n)

        #Determining the place value
        placeValue = 10**k

        #Get rid of the numbers to the right of the digit we are looking for
        leftover = n // placeValue

        #Get rid of the numbers to the right of the digit we are looking for
        remainder = leftover % 10

        #Return the result
        return remainder
    
    @staticmethod
    def short1():
        #Answer to: 'Do a bit of a deeper dive and In your own words a static method is why it might be used'
        ans = '''
                A static method is a method that is independent from an instance. This means that it can be called
                directly from a class without the need of an instance or object. This means that the function cannot use 
                the keyword, self, and is applicable to anywhere in the code. 
                '''
        return ans
    
    @staticmethod
    def short2():
        #Answer to: 'What is the purpose of the @staticmethod decorator'
        ans = '''
                The @staticmethod decorator is placed on the line directly above a method to turn it into a static
                method.
                '''
        return ans
    
    @staticmethod
    def short3():
        #Answer to: 'Explain the difference between a static method and an instance method'
        ans = '''
                The difference between a static and an instance method is that a static method does not need an object
                or instance to be called whereas the instance method does.
                '''
        return ans

# ---- Helper Functions (Global) ----#
def cleanUpInput(user):
    """
    Takes the user input and trims it for use

    Args:
        user (str) -> the user's input
    """

    #Get rid of the whitespace
    user = user.strip()

    #Turn all of the letters to lowercase
    user = user.lower()

    #Remove the whitespace in between the letters
    user = user.replace(" ", "")

    #Return the results
    return user

def validate_input(text):
    """
    Used to double check if the user input is purely just numbers or not. The operation 'isnumeric()' doesn't account for signs (+/-) so this is created instead

    Args:
        text (str) -> the user's input
    """

    #Go through the entire string
    for i in range(len(text)):
        #Rationale: '2-' breaks the code when converting into an int

        #Check to see if the signs are anywhere in the string besides the very first character
        if (text[i] == '+' or text[i] == '-') and i != 0:
            #Return false if this is the case
            return False

    #The allowed characters (i.e: numbers and signs) to check for in text
    allowed_chars = set("0123456789+-")

    #Check through all of the characters in the text if it matches with the allowed_chars list. The all() makes sure every character is found within the allowed_chars
    #before returning True. Otherwise, it will return a false
    return all(char in allowed_chars for char in text)

def choosingNumbers():
    """
    Used for user inputs. Goes through the process of getting the first and second numbers
    """

    print("Choose first number:")
    num1 = input()

    #Cleans up the first number
    num1 = cleanUpInput(num1)

    #Double check if the user input is actually a number
    if validate_input(num1) == False:
        #While loop so that the user actually puts in a number before continuing
        while validate_input(num1) == False:
            print("Try again!")
            num1 = input()
            num1 = cleanUpInput(num1)
    
    #Convert into an int
    num1 = int(num1)   

    print("Choose second number:")
    num2 = input()
    
    #Cleans up the second number
    num2 = cleanUpInput(num2)

    #Double check if the user input is actually a number
    if validate_input(num2) == False:
        #While loop so that the user actually puts in a number before continuing
        while validate_input(num2) == False:
            print("Try again!")
            num2 = input()
            num2 = cleanUpInput(num2)
    
    #Convert into an int
    num2 = int(num2)

    #Return the two numbers in the form of a list
    return num1, num2

# ---- Test Cases ----#
def test():
    #Addition
    assert(Mathings.addition(1, 2)) == 3
    assert(Mathings.addition(123, 234)) == 357
    assert(Mathings.addition(-10, 20)) == 10
    assert(Mathings.addition(-10, -20)) == -30

    #Subtraction
    assert(Mathings.subtraction(1,2)) == -1
    assert(Mathings.subtraction(234, 123)) == 111
    assert(Mathings.subtraction(-10, 20)) == -30
    assert(Mathings.subtraction(20, -10)) == 30

    #Multiplication
    assert(Mathings.multiplication(1, 1)) == 1
    assert(Mathings.multiplication(4, 5)) == 20
    assert(Mathings.multiplication(-20, 5)) == -100
    assert(Mathings.multiplication(-2, -2)) == 4

    #Division
    assert(Mathings.division(1,1)) == 1
    assert(Mathings.division(0, 5)) == 0
    assert(Mathings.division(5, 0)) == None
    assert(Mathings.division(1, 3)) == 0.33333
    assert(Mathings.division(1, 5)) == 0.2

    #Pythagoras
    assert(Mathings.pythagoras(5, 12)) == 13.0
    assert(Mathings.pythagoras(3, 4)) == 5.0
    assert(Mathings.pythagoras(1, 1)) == 1.41421
    assert(Mathings.pythagoras(10, -3)) == 10.44031

    #Power
    assert(Mathings.pow(5, 0)) == 1
    assert(Mathings.pow(2, 4)) == 16
    assert(Mathings.pow(5, 3)) == 125
    assert(Mathings.pow(2, -1)) == 0.5
    assert(Mathings.pow(3, -1.5)) == 0.19245

    #GetKthDigit asserts (From CMU CS)
    assert(Mathings.getKthDigit(809, 0) == 9)
    assert(Mathings.getKthDigit(809, 1) == 0)
    assert(Mathings.getKthDigit(809, 2) == 8)
    assert(Mathings.getKthDigit(809, 3) == 0)
    assert(Mathings.getKthDigit(0, 3) == 0)
    assert(Mathings.getKthDigit(1, 0) == 1)
    assert(Mathings.getKthDigit(1, 1) == 0)
    assert(Mathings.getKthDigit(-1, 0) == 1)
    assert(Mathings.getKthDigit(-1, 1) == 0)
    assert(Mathings.getKthDigit(-809, 0) == 9)

# ---- Main Functionality ----#
class Main():
    """
    This class will handle user interaction and menu navigation. It will include a loop that presents the user with a menu of calculation options and prompts for user input.  
    if input == 1 then Add, else if input == 2 then Divide etc
    Based on the user's choice, it will call the corresponding method from the mathings class and display the result.
    """

    #Do Asserts:
    test()

    #While loop so that the user can repeat different operations
    while True:
        print('''Hello! Please choose one operation to use:
            Addition (0)
            Subtraction(1)
            Multiplication(2)
            Division(3)
            Pythagoras(4)
            Power(5)
            GetKthDigit(6)
            Short1(7)
            Short2(8)
            Short3(9)
        ''')

        #Get the user input
        operation = input()
        if operation == 'name':
            #Print my name
            print("Daniel Lee\n")

            #Go to the next iteration of the loop
            continue
        elif operation == '0':
            #Go through choosing the numbers
            num = choosingNumbers()

            #Perform the operation
            result = Mathings.addition(num[0], num[1])

            #Print the result
            print(f"The sum is: {result}\n")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break
            
        elif operation == '1':
            #Go through choosing the numbers
            num = choosingNumbers()
            
            #Perform the operation
            result = Mathings.subtraction(num[0], num[1])

            #Print the result
            print(f"The difference is: {result}")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '2':
            #Go through choosing the numbers            
            num = choosingNumbers()

            #Perform the operation
            result = Mathings.multiplication(num[0], num[1])

            #Print the result
            print(f"The product is: {result}")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '3':
            #Go through choosing the numbers            
            num = choosingNumbers()

            #Perform the operation
            result = Mathings.division(num[0], num[1])

            #Print the result
            print(f"The quotient is: {result}")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '4':
            #Go through choosing the numbers            
            num = choosingNumbers()

            #Perform the operation
            result = Mathings.pythagoras(num[0], num[1])

            #Print the result
            print(f"The hypotenuse is: {result}")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '5':
            #Go through choosing the numbers            
            num = choosingNumbers()

            #Perform the operation
            result = Mathings.pow(num[0], num[1])

            #Print the result
            print(f"The result is: {result}")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '6':
            #Go through choosing the numbers            
            num = choosingNumbers()

            #Perform the operation. The 'num[1] - 1' is due to the way the index is counted from 0.
            result = Mathings.getKthDigit(num[0], num[1] - 1)

            #Print the result
            print(f"The '{num[1]}' digit from the right is: {result}")

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '7':
            #Print the short answer
            print(Mathings.short1())

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '8':
            #Print the short answer
            print(Mathings.short2())

            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        elif operation == '9':
            #Print the short answer
            print(Mathings.short3())
            
            #Provide the user a choice to continue or exit
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue

            #'else' keyword so that if the user types anything besides a yes, the program will stop
            else:
                break

        else:
            print("Try Again!")
        