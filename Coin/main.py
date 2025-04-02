#Import the coin class and functions
from coin import * 

if __name__ == "__main__":
    """
    Runs the code
    """

    #Initialize all types of coins present in Canada
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
        