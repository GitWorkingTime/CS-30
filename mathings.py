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
    def dividision(x, y):
        return x / y
    
    @staticmethod
    def pythagoras(x, y):
        a = x**2
        b = y**2
        c = math.sqrt(a + b)
        return c

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
        return None
    
    @staticmethod
    def short2():
        return None
    
    @staticmethod
    def short3():
        return None
    
    @staticmethod
    def exit():
        return None

class Main():
    def cleanUpInput(user):
        user = user.strip()
        user = user.replace(" ", "")
        return user
    
    def validate_input(text):
        allowed_chars = set("0123456789+-")
        return all(char in allowed_chars for char in text)

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
    match operation:
        case '0':
            print("Choose first number:")
            num1 = input()
            if checkForLetters(num1) == True:
                while checkForLetters(num1) == True:
                    print("Try again!")
                    num1 = input()
                
            num1 = int(num1)
            print("Choose second number:")
            num2 = input()
            if checkForLetters(num2) == True:
                while checkForLetters(num2) == True:
                    print("Try again!")
                    num2 = input()
            
            num2 = int(num2)
            sum = Mathings.addition(num1, num2)
            print(f"The sum is: {sum}")
        case '1':
            print("subtracting")
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            pass
        case '9':
            pass
        case _:
            print("Try again!")

    pass

# if types(ans) != int:
#try: expt: