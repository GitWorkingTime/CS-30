import random

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
        hand[i] = set_value()
    return hand

def create_set():
    for i in range(4):
        set.append(create_hand())
    return set

create_set()
print(f"\nHands to Choose from:\nFirst Hand: {set[0]}\nSecond Hand: {set[1]}\nThird Hand: {set[2]}\n Fourth Hand: {set[3]}\n")

def check_equal():
    pass

def shuffle():
    pass

def three_of_a_kind():
    pass

def num_of_pairs():
    pass

def highest_pair():
    pass