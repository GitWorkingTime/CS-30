import random
import copy

value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]
suite = ['♥', '♠', '♦', '♣']
set = []

# Helper Functions:
def binary_search(arr, target):
    """
    Performs an iterative binary search on a SORTED list
    
    Args:
        arr (list): a sorted list of values
        target (int or float): the value we're looking for
    
    Example:
        binary_search([1,2,3,4,5,6,7,8,9], 6)
        >>> 5
        
        binary_search([1,3,5,7,9], 4)
        >>> -1 (-1 for false)
    """
    low = 0 #start
    high = len(arr) - 1 #"-1" accounts for the way the index is counted
    mid = 0
    
    while low <= high:
        mid = (low + high) // 2 #Take the average between low and high
        
        #If the target is the same as the middle index value, return it
        if target == arr[mid]:
            return mid
        
        #If the target is. greater than the middle index value, ignore the left half
        elif target > arr[mid]:
            low = mid + 1
        
        #If the target is less than the middle index value, ignore the right half
        else:
            high = mid - 1
    #If the target is not found in the array, return "-1" to say it is false
    return -1

def selection_sort(arr):
    """
    Performs a selection_sort algorithm on an UNSORTED list
    
    Args:
        arr (list): the list we want to sort
    
    Examples:
        selection_sort([1,5,7,3])
        >>> [1,3,5,7]

        selection_sort(['b','d','f','e','t'])
        >>> ['b', 'd', 'e', 'f', 't']
    """ 
    
    n = len(arr) #Get the array's length
    
    if n <= 1:
        return arr
    
    for i in range(0, n - 1): #Go through each item in the list. "-1" to skip the last item because there is no need to sort that one.
        curMinInd = i #The current minimum index is set to the current item
        
        for j in range(i + 1, n):#Start the for loop one item ahead of the current item and go through the rest of the list
        
            if arr[j] < arr[curMinInd]: #If an item ahead has a smaller value, make it the current minimum index. Repeat until the loop is done
                curMinInd = j
        
        arr[i], arr[curMinInd] = arr[curMinInd], arr[i] #Swap the two items
    return arr

def duplicate_check(hand):
    """
    Checks to see if there is a duplicate card in the hand

    Args:
        hand (list): the hand to double check

    Example:
        hand = ['♠ 7', '♠ 7']
        hand = duplicate_check(hand)
        >>> ['♠ 7', '♠ K']
    """

    length = len(hand) #Find the number of items in the hand

    #Go through each item in the hand
    for i in range(length):

        #Go through each item behind what we are looking at
        for j in range(i):

            #If any of the cards behind the current is the same, change it
            if hand[i] == hand[j]:

                #In case there after the first change it is the same, keep changing it
                while hand[j] == hand[i]:
                    hand[i] = set_value()
    return hand

def convert_face_to_value(hand):
    """
    Changes the face cards (i.e: Ace, Jack, King, and Queen) into its integer values (i.e: 1, 11, 12, 13)
    Pre-requisite: the suits infront of the cards must be removed

    Args:
        hand (list): the hand to convert the face cards into integer values
    
    Example:   
        arr = ['♥ 4', '♠ J']
        
        #To remove the suits in front of the cards
        for i in range(len(arr)):
            arr[i] = arr[i][2:] #Removes the first 2 characters

        convert_face_to_value(arr)
        >>> [4, 11]
    """
    handCopy = copy.copy(hand) #Copy the hand so that the original does not mutate
    n = len(handCopy) #Find the number of items in the hand

    for i in range(n): #Go through each item in the hand

        #Check if the value is a face card. If so, convert it into the corresponding int values:
        if handCopy[i] == 'A': 
            handCopy[i] = 1

        elif handCopy[i] == 'J':
            handCopy[i] = 11

        elif handCopy[i] == 'Q':
            handCopy[i] = 12

        elif handCopy[i] == 'K':
            handCopy[i] = 13
        
        #Convert the value into an int if it is not a face card because the values list uses strings
        handCopy[i] = int(handCopy[i])
    
    return handCopy #Return the hand converted into int

def count_repeats(hand):
    """
    Goes through the hand and counts the number of items a value appears in a hand

    Args:
        hand (list): the hand we want to go through

    Example:
        count_repeats(['♦ J', '♣ K', '♥ 5', '♣ Q', '♣ A', '♦ 6', '♥ 6', '♣ 2'])
        >>> [1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1]
    """
    copiedHand = copy.copy(hand) #Copy the hand to use
    length = len(copiedHand) #Find the number of items in the hand

    #To remove the suits in front of the cards
    for i in range(length): 
        copiedHand[i] = copiedHand[i][2:] #Removes the first 2 characters
    copiedHand = convert_face_to_value(copiedHand) #Convert the face cards into its corresponding int values
    copiedHand = selection_sort(copiedHand) #Sort the hand for binary search

    #Initialize repeat count
    repeats = list(range(13)) #Create a list with 13 items for each value
    for i in range(13): #Go through the entire list
        repeats[i] = 0 #Set each to 0
    
    #Initialize card values in int:
    cardValues = copy.copy(value) #Copy the value's list
    cardValues = convert_face_to_value(cardValues) #Convert the face cards into its corresponding int values
 
    for i in range(length): #Go through the entire hand
        valueInd = binary_search(cardValues, copiedHand[i]) #For the current item, find the corresponding index in the values list
        if valueInd == -1: #If not found
            continue #Skip to the next item in the list
        repeats[valueInd] += 1 #If found, increment by one on the card found 
    
    return repeats #Return the repeats list

# --------------------------------- #
#For creating the hands:
def set_value():
    """
    Creates the card

    Example:
        set_value()
        >>> '♠ A'
    """

    #Choose a random value
    valueInd = random.randint(0, 12)

    #Choose a random suit
    suitInd = random.randint(0, 3)

    #Combine the two together using f strings
    card = f"{suite[suitInd]} {value[valueInd]}"

    return card #Return the card value

def create_hand():
    """
    Creates a hand with 1 to 13 cards

    Example:
        create_hand()
        >>> ['♦ 3', '♥ 5', '♥ A', '♣ K', '♦ 6', '♥ 4', '♦ 4', '♠ J', '♣ 10', '♥ 7', '♣ 5']
    """

    length = random.randint(1, 13) #Determine the amount of cards in the hand

    hand = list(range(length)) #Create a list with the specified amount of cards

    for i in range(length): #Go through each item
        value = set_value() #Create the card
        hand[i] = value #Set the item to the card
    
    duplicate_check(hand) #Go through the hand once more to make sure there is no duplicates
    return hand #Return the hand

def create_set():
    for i in range(4): #Create 4 hands
        set.append(create_hand()) #Add each hand to a set
    return set #Return the set

# --------------------------------- #
#The operation functions:
def check_equal(hand):
    """
    Goes through the hand and sees if all of the cards are equal

    Args:
        hand (list): the hand we want to check

    Example:
        check_equal(['♠ 10', '♠ 8'])
        >>> False

        check_equal(['♠ 10', '♠ 10'])
        >>> True
    """

    length = len(hand) #Find the number of items in the hand
    handCopy = copy.copy(hand) #Create a copy so that we don't mutate the original

    if length == 1: #If there is only one card, return true
        return True
    elif length < 1:
        return False
    
    for i in range(length): #Go through each item in the hand
        handCopy[i] = handCopy[i][2:] #Removes the first 2 characters
    handCopy = convert_face_to_value(handCopy) #Convert the face cards into its corresponding int values
    
    if handCopy[1:] == handCopy[:-1]: #Check if all of the elements are the same using list splicing
        return True #Return true if all elements are the same
    else:
        return False #Returns false if all the elements are not the same

def shuffle(hand):
    """
    Shuffle the cards

    Example:
        shuffle(['♥ 9', '♦ J', '♥ Q', '♠ 8', '♣ Q', '♦ 5', '♥ 2'])
        >>> "Original: ['♥ 9', '♦ J', '♥ Q', '♠ 8', '♣ Q', '♦ 5', '♥ 2']"
        >>> "Shuffled: ['♦ J', '♥ Q', '♦ 5', '♥ 9', '♠ 8', '♣ Q', '♥ 2']"
    """
    old = copy.copy(hand) #To compare with the previous version
    length = len(hand) #Find the number of items in the hand
    if length <= 1: #If there is only one card, return it
        print(f"\nOriginal: {hand}")
        print(f"Shuffled: {hand}\n")
        return hand

    print(f"\nOriginal: {hand}")
    while old == hand: #While the old and new is the same. This ensures that only a new shuffled deck is returned
        for i in range(length): #Go through the hand
            switchInd = random.randint(0, length - 1) #Choose randomly which other item to switch with
            hand[i], hand[switchInd] = hand[switchInd], hand[i] #Swap (We do want to mutate this one)
    
    print(f"Shuffled: {hand}\n")
    return hand #Return the shuffled hand

def three_of_a_kind(hand):
    """
    Goes through a hand to see if there are three of a kind

    Args:
        hand(list): the hand we want to go through
    
    Example:
        three_of_a_kind(['♦ 2', '♦ 8', '♣ 6', '♥ Q', '♦ 3'])
        >>> False

        three_of_a_kind(['♦ 2', '♣ 3', '♣ 6', '♥ 3', '♦ 3'])
        >>> True
    """
    n = len(hand) #Find the number of items in the hand
    if n < 3: #If there is less than 3 cards, return false
        return False

    repeats = count_repeats(hand) #Count the number of repeats in the hand

    for i in range(13): #Go through the repeats list
        if repeats[i] == 3: #If there is an element which values is 3, return True
            return True
    return False #Otherwise, return false to say there is no three of a kind


def num_of_pairs(hand):
    """
    Print the any quadruplets, triplets, and pairs found in the hand

    Args:
        hand (list): The hand we want to go through
    
    Example:
        num_of_pairs(['♠ 8', '♥ A', '♣ 8', '♠ 7', '♣ 5', '♠ 2', '♦ 9', '♦ 3', '♠ 3', '♠ K', '♣ A', '♠ J'])
        >>> "Pair: ♥ A ♣ A"
        >>> "Pair: ♦ 3 ♠ 3"
        >>> "Pair: ♠ 8 ♣ 8"
    """
    valueArr = copy.copy(hand) #Copy the hand so that the original doesn't mutate
    length = len(hand) #Find the number of items in the hand
    pairList = []
    tripletsList = []
    quadrupleList = []

    #Go through the entire value hand
    for i in range(length): 
        valueArr[i] = valueArr[i][2:] #Remove the first 2 characters

    repeats = count_repeats(hand) #Find the number of repeats in the hand
    
    if length <= 1:
        return -1
    
    if (2 in repeats) == False and (3 in repeats) == False and (4 in repeats) == False: #Checks to see if there are any repeats at all
        return -1 #Return '-1' if none are found

    #For quadruplets:
    for i in range(13): #13 to go through each repeats item
        if repeats[i] != 4: #If the repeat value isn't 4, move on to the next item
            continue
        
        targetInd = i #Set the target index to the current iteration
        quadrupleInd = [] #Initialize the list for cards with the same value

        for j in range(length): #Go through the number of items in the hand
            if valueArr[j] == value[targetInd]: #If the value is the same as the target
                quadrupleInd.append(j) #Add on the index
                continue #Move on to the next item
        quadrupleList.append(quadrupleInd)

        #Print all of the Quadruples:
        print(f"Quadruples: {hand[quadrupleInd[0]]} {hand[quadrupleInd[1]]} {hand[quadrupleInd[2]]} {hand[quadrupleInd[2]]}\n")

    #For triplets:
    for i in range(13): #13 to go through each repeats item
        if repeats[i] != 3: #If the repeat value isn't 3, move on to the next item
            continue 

        targetInd = i #Set the target index to the current iteration
        tripletsInd = [] #Initialize the list for cards with the same value
        for j in range(length): #Go through the number of items in the hand
            if valueArr[j] == value[targetInd]: #If the value is the same as the target
                tripletsInd.append(j) #Add on the index
                continue #Move on to the next item
        tripletsList.append(tripletsInd)
        #Print all of the Triplets:
        print(f"Triples: {hand[tripletsInd[0]]} {hand[tripletsInd[1]]} {hand[tripletsInd[2]]}\n")

    #For pairs:
    for i in range(13): #13 to go through each repeats item
        if repeats[i] != 2: #If the repeat value isn't 2, move on to the next item
            continue

        targetInd = i #Set the target index to the current iteration
        pairInd = [] #Initialize the list for cards with the same value
        for j in range(length): #Go through the number of items in the hand
            if valueArr[j] == value[targetInd]: #If the value is the same as the target
                pairInd.append(j) #Add on the index
                continue #Move on to the next item
        
        pairList.append(pairInd)
        #Print all of the Pairs:
        print(f"Pair: {hand[pairInd[0]]} {hand[pairInd[1]]}\n")
    return quadrupleList, tripletsList, pairList


def highest_pair(hand):
    """
    Prints the highest pair found in a hand (only 2 cards)

    Args:
        hand(list): the hand we want to go through
    
    Example:
        highest_pair(['♦ 4', '♦ 9', '♠ J', '♦ K', '♥ K'])
        >>> "Pair: ♦ K ♥ K"
    """

    copiedHand = copy.copy(hand) #Copy the list so that the original doesn't mutate
    valueArr = copy.copy(hand) #Copy the list so that the original doesn't mutate
    length = len(hand) #Find the number of items in the hand
    for i in range(length): #Go through the items in the hand
        valueArr[i] = valueArr[i][2:] #Remove the first 2 characters

    repeats = count_repeats(hand) #Find the number of repeats in the hand

    #Initialize the highest index variable
    highestInd = 0
    for i in range(13): #Go through the repeats list
        if repeats[i] == 2: #If the repeats value is 2, set the highest index to the iteration
            highestInd = i

    if highestInd == 0: #If no pair is found
        return -1 #'-1' for no pair found
    
    pairInd = [] #Initialize the pair list 
    for i in range(length): #Go through the entire hand
        if valueArr[i] == value[highestInd]: #If the value is the same as the highest index, add that index to the list
            pairInd.append(i)
            continue
    
    #Print the pair
    print(f"Pair: {copiedHand[pairInd[0]]} {copiedHand[pairInd[1]]}\n")
    return pairInd

# --------------------------------- #
#Main functionality:

#For asserts
def tests():
    #For 'Check Equal':
    assert(check_equal(['♦ 4', '♦ K', '♠ 10'])) == False
    assert(check_equal(['♦ 4'])) == True
    assert(check_equal(['♠ 8', '♦ 6'])) == False
    assert(check_equal(['♠ 10', '♥ Q', '♣ 4', '♣ 9', '♦ Q', '♦ 8', '♥ J', '♥ 9', '♠ K', '♥ 6', '♠ 3'])) == False
    assert(check_equal([])) == False

    #For 'Shuffles': 
    assert(shuffle(['♥ J', '♠ 5']) == ['♥ J', '♠ 5']) == False
    assert(shuffle(['♠ 7', '♥ 5', '♣ 2']) == ['♠ 7', '♥ 5', '♣ 2']) == False
    assert(shuffle(['♠ 10', '♦ 7', '♦ 10', '♥ 7', '♥ 6', '♦ 5', '♥ J', '♥ 8', '♦ 4']) == ['♠ 10', '♦ 7', '♦ 10', '♥ 7', '♥ 6', '♦ 5', '♥ J', '♥ 8', '♦ 4']) == False
    
    #For 'Three of a kind':
    assert(three_of_a_kind(['♦ 6', '♠ 9', '♣ 2', '♠ K', '♥ 6', '♥ 5', '♦ 3', '♣ 9', '♠ 5', '♥ 3'])) == False
    assert(three_of_a_kind(['♦ Q', '♠ 8', '♣ J', '♦ 2', '♦ 8', '♠ J'])) == False
    assert(three_of_a_kind(['♥ 10', '♣ 2', '♥ 2', '♦ 2'])) == True
    assert(three_of_a_kind(['♣ A'])) == False
    assert(three_of_a_kind([])) == False
    
    #For 'Count pairs':
    assert(num_of_pairs(['♠ 3', '♠ 6', '♠ J', '♥ A', '♠ 9'])) == -1
    assert(num_of_pairs(['♠ 2', '♥ 7', '♥ 4', '♦ J', '♥ 8'])) == -1
    assert(num_of_pairs(['♦ 4', '♥ 5', '♥ 4', '♠ 3', '♦ A', '♥ K', '♦ 9', '♥ 8', '♦ J', '♥ 7', '♣ 7', '♠ 9', '♥ Q'])) == ([], [], [[0, 2], [9, 10], [6, 11]])
    assert(num_of_pairs(['♥ A', '♠ J', '♣ 4', '♣ Q', '♦ 7', '♥ 8', '♠ Q'])) == ([], [], [[3, 6]])
    assert(num_of_pairs(['♣ 9', '♥ 3', '♠ 7', '♣ 10', '♠ 9', '♥ J', '♦ 2', '♥ 9', '♦ K', '♣ 6', '♠ 2', '♠ J', '♥ 8'])) == ([], [[0, 4, 7]], [[6, 10], [5, 11]])
    assert(num_of_pairs(['♥ J', '♣ J', '♠ J', '♦ J'])) == ([[0, 1, 2, 3]], [], [])
    
    #For 'Highest Pair':
    assert(highest_pair(['♥ Q', '♦ 10', '♦ 3', '♠ Q', '♣ K', '♦ 8', '♠ 5', '♣ 5', '♣ 4', '♦ 2', '♥ K', '♣ 7'])) == [4, 10]
    assert(highest_pair(['♣ 3', '♦ 2', '♠ 7', '♣ K', '♥ Q', '♦ 4', '♦ 6', '♦ 5', '♣ 9'])) == -1
    assert(highest_pair(['♦ 5', '♥ 10', '♠ 3', '♦ 7'])) == -1
    assert(highest_pair(['♦ 9', '♠ Q', '♥ 7', '♦ A', '♣ 6', '♠ A', '♠ 2', '♣ K', '♦ 9'])) == [0, 8]

def main_loop():
    """
    Creates a hand and asks user input for which hand to use and what operations they want to do
    """

    set = create_set() #Create the hands
    tests()
    for i in range(14): #Create white space between the main functionality and the asserts because some of them prints onto the console
        print("\n")


    while True: #While loop so that actions can be repeated
        print(f"Hands Available:\n#1: {set[0]}\n#2: {set[1]}\n#3: {set[2]}\n#4: {set[3]}") #Show the hands
        print("\nWhich hand would you like? (1, 2, 3, 4) OR type 'exit' to leave") #Ask the users what hand they would like to use

        handInput = input() #Get user input
        handInput = handInput.lower() #Convert into lowercase
        handInput = handInput.strip() #Remove any white space outside of the string
        handInput = handInput.replace(" ", "") #Remove any white space in between the characters
        
        if handInput == "exit": #If they want to leave
            break #Leave the loop

        if handInput.isnumeric() == False: #Double checks if the input is an int value
            print("\nPlease input an integer value. Try again\n")
            continue #Return to the top of this loop
        handInput = int(handInput) - 1 #Converts into integer. '-1' to account for the way index is counted

        if handInput > 3: #If the hand chosen is more than what we have, make them choose the correct hand
            print("Please choose a hand\n")
            continue #Return to the top of this loop

        print(f"\nYour chosen hand is {set[handInput]}\n") #Announce what hand they have chosen
        while(True): #Another while loop so that the operations can be repeated without changing the hand chosen
            print('''Which operation would you like to do?
            Check If all are equal(type 'equal')
            Shuffle the cards(type 'shuffle')
            See if there is any three of a kind(type 'three')
            Find any pairs in the hand(type 'pair')
            Find the highest pair in the hand(type 'highest')
            Try another hand(type 'exit')''')

            operationInput = input() #Get user input
            operationInput = operationInput.lower() #Convert into lowercase
            operationInput = operationInput.strip() #Remove any white space outside of the string
            operationInput = operationInput.replace(" ", "") #Remove any white space in between the characters
            
            #Go through the operations
            if operationInput == "equal": 
                isEqual = check_equal(set[handInput])
                if isEqual == False:
                    print("\nNo cards in this hand is the same\n")
                else:
                    print("\nAll cards in this hand is the same\n")
                
            elif operationInput == "shuffle":
                set[handInput] = shuffle(set[handInput])

            elif operationInput == "three":
                if three_of_a_kind(set[handInput]) == True:
                    print("\nThere is a three of a kind!\n")
                else:
                    print("\nThere is no three of a kind\n")

            elif operationInput == "pair":
                if num_of_pairs(set[handInput]) == -1: #If none were found
                    print("\nNo pair was found\n")

            elif operationInput == "highest":
                if highest_pair(set[handInput]) == -1: #If none were found
                    print("\nNo pair was found\n")

            elif operationInput == "exit":
                break #Leave this loop
            else:
                print("\nPlease choose an appropriate operation!\n")
                continue #Return to the top of this loop
        
main_loop() #Run the program