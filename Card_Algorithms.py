import random
import copy

value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suite = ['♥', '♠', '♦', '♣' ]
set = [] 

def set_value():
    valueInd = random.randint(1, 13) - 1
    suiteInd = random.randint(1, 4) - 1
    card = f"{suite[suiteInd]} {value[valueInd]}"
    return card

def create_hand():
    length = random.randint(1, 13)
    hand = list(range(length))
    for i in range(length):
        value = set_value()
        hand[i] = value
    duplicate_check(hand)
    return hand

def create_set():
    for i in range(4):
        set.append(create_hand())
    return set

def duplicate_check(hand):
    for i in range(len(hand)):
        for j in range(i):
            if hand[i] == hand[j]:
                while hand[j] == hand[i]:
                    hand[i] = set_value()
    return hand

# create_set()
# print(f"\nHands to Choose from:\nFirst Hand:{set[0]}\nSecond Hand:{set[1]}\nThird Hand:{set[2]}\nFourth Hand:{set[3]}\n")

def check_equal(hand):
    length = len(hand)
    handCopy = copy.copy(hand)
    if length < 1: #If there is no card
        return False 
    if length == 1: #If there is only one card
        return True
    if length > 4: #If there is more than 4 cards
        return False
    
    for i in range(length):
        handCopy[i] = hand[i][2:]

        if handCopy[i] == 'A':
            handCopy[i] = 1
        elif handCopy[i] == 'J':
            handCopy[i] = 11
        elif handCopy[i] == 'Q':
            handCopy[i] = 12
        elif handCopy[i] == 'K':
            handCopy[i] = 13
    
    for i in range(length):
        handCopy[i] = int(handCopy[i])
    result = handCopy[1:] == handCopy[:-1]
    return result

def shuffle(hand):
    length = len(hand)
    print(hand)
    for i in range(length):
        switchInd = random.randint(1, length) - 1
        hand[i], hand[switchInd] = hand[switchInd], hand[i]
    print(hand)
    return hand

def three_of_a_kind():
    pass

def num_of_pairs():
    pass

def highest_pair():
    pass
