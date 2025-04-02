#Import the coin class and functions
from CoinDaniel import * 

if __name__ == "__main__":
    """
    Runs the code
    """
    #Initialize all types of coins most often used in Canada
    penny = Coin("penny", 9.53, "94% Steel, 1.5% Nickel, and 4.5% Copper plating", 1)
    nickel = Coin("nickel", 10.6, "94.5% Steel, 3.5% Copper, and 2% nickel plating", 5)
    dime = Coin("dime", 9.02, "92% Steel, 5.5% Copper, and 2.5% Nickel plating", 10)
    quarter = Coin("quarter", 11.94, "94% Steel, 3.8% Copper, and 2.2% Nickel plating", 25)
    loonie = Coin("loonie", 13.25, "91.5% Nickel, 8.5% Bronze plating which has 88% Copper and 12% Tin", 100)
    toonie = Coin("toonie", 14, "Ring: 99% Nickel, Centre: 92% Coppper, 6% Aluminium, and 2% Nickel", 200)

    #Create a list that has all types of coins present in Canada
    all_coins = [penny, nickel, dime, quarter, loonie, toonie]

    def totalValue(all_coins):
        """
        Calculates the total sum of the coins of a list containing coins

        Args:
            all_coins (list) - contains coins

        Examples:
            totalValue([penny, nickel, dime]) #Each items in the list are instances
            >>> 16
        """

        #Find the length of the list
        n = len(all_coins)

        #Initialize sum variable and start at zero
        sum = 0
        
        #Go through each item in the list
        for i in range(n):
            #Add up all of the coin's values
            sum += all_coins[i].value
        
        #Return the total sum
        return sum 
    
    # ---- Asserts ----#
    def tests():
        # ---- Area ---- #
        assert(penny.get_area()) == "The surface area of one side of a penny is 285.32 mm^2.\nA penny is made up of 94% Steel, 1.5% Nickel, and 4.5% Copper plating and has a value of 1 cents"
        assert(dime.get_area()) == "The surface area of one side of a dime is 255.6 mm^2.\nA dime is made up of 92% Steel, 5.5% Copper, and 2.5% Nickel plating and has a value of 10 cents"
        assert(nickel.get_area()) == "The surface area of one side of a nickel is 352.99 mm^2.\nA nickel is made up of 94.5% Steel, 3.5% Copper, and 2% nickel plating and has a value of 5 cents"
        assert(quarter.get_area()) == "The surface area of one side of a quarter is 447.88 mm^2.\nA quarter is made up of 94% Steel, 3.8% Copper, and 2.2% Nickel plating and has a value of 25 cents"
        assert(loonie.get_area()) == "The surface area of one side of a loonie is 551.55 mm^2.\nA loonie is made up of 91.5% Nickel, 8.5% Bronze plating which has 88% Copper and 12% Tin and has a value of 100 cents"
        assert(toonie.get_area()) == "The surface area of one side of a toonie is 615.75 mm^2.\nA toonie is made up of Ring: 99% Nickel, Centre: 92% Coppper, 6% Aluminium, and 2% Nickel and has a value of 200 cents"

        # ---- Circumference ---- #
        assert(penny.get_circumference()) == "The penny's circumferance is 59.88 mm.\nA penny is made up of 94% Steel, 1.5% Nickel, and 4.5% Copper plating and has a value of 1 cents"
        assert(dime.get_circumference()) == "The dime's circumferance is 56.67 mm.\nA dime is made up of 92% Steel, 5.5% Copper, and 2.5% Nickel plating and has a value of 10 cents"
        assert(nickel.get_circumference()) == "The nickel's circumferance is 66.6 mm.\nA nickel is made up of 94.5% Steel, 3.5% Copper, and 2% nickel plating and has a value of 5 cents"
        assert(quarter.get_circumference()) == "The quarter's circumferance is 75.02 mm.\nA quarter is made up of 94% Steel, 3.8% Copper, and 2.2% Nickel plating and has a value of 25 cents"
        assert(loonie.get_circumference()) == "The loonie's circumferance is 83.25 mm.\nA loonie is made up of 91.5% Nickel, 8.5% Bronze plating which has 88% Copper and 12% Tin and has a value of 100 cents"
        assert(toonie.get_circumference()) == "The toonie's circumferance is 87.96 mm.\nA toonie is made up of Ring: 99% Nickel, Centre: 92% Coppper, 6% Aluminium, and 2% Nickel and has a value of 200 cents"

        # ---- Total Values ---- #
        test_all_coins1 = [penny, dime, quarter]
        assert(totalValue(test_all_coins1)) == 36

        test_all_coins2 = [dime, quarter, toonie]
        assert(totalValue(test_all_coins2)) == 235
        
        test_all_coins3 = [nickel, dime]
        assert(totalValue(test_all_coins3)) == 15
    
    tests()

    while True:
        """
        Asks for user input and then tries to find it an a list by using linear search
        """
        #---- User Input ----#
        print("Choose a coin: Penny, Nickel, Dime, Quarter, Loonie, or a Toonie")

        #Get the user input
        name = input() 

        #Remove whitespace in between characters
        name = name.replace(" ", "")

        #Make all of the characters lowercase
        name = name.lower()

        #Remove whitespace outside of the characters
        name = name.strip()

        #---- List ----#
        #Get the length of the list
        n = len(all_coins) 
        found = False

        #Apply linear search to find the coin
        for i in range(n):

            #If we have found the coin
            if name == all_coins[i].name:
                #Return all of the instance variables through the '__repr__' method
                print(f"{all_coins[i]}\n")
                found = True
        #If not found, say we haven't found it
        if found == False:
            print("Coin not found! Try again.\n")

        #Make this false again to reset the loop
        found = False