import math

class Mathings:
    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        return x - y
    
    @staticmethod
    def multiplication(x, y):
        return x * y

    @staticmethod
    def division(x, y):
        return round(x / y, 5)
    
    @staticmethod
    def pythagoras(x, y):
        a = x**2
        b = y**2
        c = math.sqrt(a + b)
        return round(c, 5)

    @staticmethod
    def pow(x, y):
        return x**y

    @staticmethod
    def getKthDigit(n, k):
        n = abs(n)
        placeValue = 10**k
        leftover = n // placeValue
        remainder = leftover % 10
        return remainder
    
    @staticmethod
    def short1():
        ans = '''
                A static method is a method that is independent from an instance. This means that it can be called
                directly from a class without the need of an instance or object. This means that the function cannot use 
                the keyword, self, and is applicable to anywhere in the code. 
                '''
        return ans
    
    @staticmethod
    def short2():
        ans = '''
                The @staticmethod decorator is placed on the line directly above a method to turn it into a static
                method.
                '''
        return ans
    
    @staticmethod
    def short3():
        ans = '''
                The difference between a static and an instance method is that a static method does not need an object
                or instance to be called whereas the instance method does.
                '''
        return ans
    
    @staticmethod
    def exit():
        return None

def cleanUpInput(user):
    user = user.strip()
    user = user.lower()
    user = user.replace(" ", "")
    return user

def validate_input(text):
    for i in range(len(text)):
        if (text[i] == '+' or text[i] == '-') and i != 0:
            return False

    allowed_chars = set("0123456789+-")
    return all(char in allowed_chars for char in text)

def choosingNumbers():
    print("Choose first number:")
    num1 = input()
    num1 = cleanUpInput(num1)
    if validate_input(num1) == False:
        while validate_input(num1) == False:
            print("Try again!")
            num1 = input()
            num1 = cleanUpInput(num1)
        
    num1 = int(num1)

    print("Choose second number:")
    num2 = input()
    num2 = cleanUpInput(num2)
    if validate_input(num2) == False:
        while validate_input(num2) == False:
            print("Try again!")
            num2 = input()
            num2 = cleanUpInput(num2)
    
    num2 = int(num2)
    return num1, num2

class Main():
    while True:
        print('''Hello! Please choose one operation to use:
            Addition (0)
            Subtraction(1)
            Multiplication(2)
            Division(3)
            Pythagoras(4)
            Power(5)
            GetKthdigit(6)
            Short1(7)
            Short2(8)
            Short3(9)
        ''')
        operation = input()
        if operation == '0':
            num = choosingNumbers()
            result = Mathings.addition(num[0], num[1])
            print(f"The sum is: {result}\n")

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break
            
        elif operation == '1':
            num = choosingNumbers()
            result = Mathings.subtraction(num[0], num[1])
            print(f"The difference is: {result}")

        elif operation == '2':
            num = choosingNumbers()
            result = Mathings.multiplication(num[0], num[1])
            print(f"The product is: {result}")

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '3':
            num = choosingNumbers()
            result = Mathings.division(num[0], num[1])
            print(f"The quotient is: {result}")

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '4':
            num = choosingNumbers()

            result = Mathings.pythagoras(num[0], num[1])
            print(f"The hypotenuse is: {result}")

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '5':
            num = choosingNumbers()
            result = Mathings.pow(num[0], num[1])
            print(f"The result is: {result}")

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '6':
            num = choosingNumbers()
            result = Mathings.getKthDigit(num[0], num[1] - 1)
            print(f"The '{num[1]}' digit from the right is: {result}")

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '7':
            print(Mathings.short1())

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '8':
            print(Mathings.short2())

            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break

        elif operation == '9':
            print(Mathings.short3())
            
            print("Do you wish to continue? Type 'yes' to continue or type anything else to exit")
            user = input() 
            user = cleanUpInput(user)
            
            if user == "yes":
                print("")
                continue
            else:
                break
            
        else:
            print("Try Again!")
        