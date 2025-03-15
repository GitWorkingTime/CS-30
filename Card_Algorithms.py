import random
import copy

value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]
suite = ['♥', '♠', '♦', '♣']
set = []

def set_value():
    valueInd = random.randint(0, 11)
    suiteInd = random.randint(0, 3)
    #print(f"Value ind: {valueInd} and Suite Ind: {suiteInd}.")
    card = f"{suite[suiteInd]} {value[valueInd]}"
    return card

def duplicate_check(hand):
    length = len(hand)
    for i in range(length):
        for j in range(i):
            if hand[i] == hand[j]:
                while hand[j] == hand[i]:
                    hand[i] = set_value()
    return hand

def convert_face_to_value(hand):
    handCopy = copy.copy(hand)
    for i in range(len(handCopy)):
        if handCopy[i] == 'A':
            handCopy[i] = 1
        elif handCopy[i] == 'J':
            handCopy[i] = 11
        elif handCopy[i] == 'Q':
            handCopy[i] = 12
        elif handCopy[i] == 'K':
            handCopy[i] = 13
    return handCopy

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

def check_equal(hand):
    length = len(hand)
    handCopy = copy.copy(hand)
    
    if length < 1 and length > 4:
        return False
    elif length == 1:
        return True
    
    
    for i in range(length):
        handCopy[i] = handCopy[i][2:]
        handCopy = convert_face_to_value(handCopy)
        handCopy[i] = int(handCopy[i])
    
    if handCopy[1:] == handCopy[:-1]:
        return True
    else:
        return False

def shuffle(hand):
    length = len(hand)
    print(hand)
    for i in range(length):
        switchInd = random.randint(1, length) - 1
        hand[i], hand[switchInd] = hand[switchInd], hand[i]
    print(hand)
    return hand

def three_of_a_kind(hand):
    handCopy = copy.copy(hand)
    print(handCopy)
    valueRepeats = list(range(13))
    valueInt = copy.copy(value)
    valueInt = convert_face_to_value(valueInt)
    for i in range(13):
        valueRepeats[i] = 0
    
    length = len(handCopy)
    
    if length < 3:
        return False
    
    for i in range(length):
        handCopy[i] = handCopy[i][2:]
    handCopy = convert_face_to_value(handCopy)
    
    for i in range(length):
        for j in range(13):
            if handCopy[i] == valueInt[j]:
                valueRepeats[j] += 1
    
    # for i in range(13):
    #     print(f"{value[i]}: {valueRepeats[i]}")
    
    for i in range(13):
        if valueRepeats[i] == 3:
            return True
    return False

def num_of_pairs():
    pairRepeats = 0
    handCopy = copy.copy(hand)
    print(handCopy)
    valueRepeats = list(range(13))
    valueInt = copy.copy(value)
    valueInt = convert_face_to_value(valueInt)
    for i in range(13):
        valueRepeats[i] = 0
    
    length = len(handCopy)
    
    for i in range(length):
        handCopy[i] = handCopy[i][2:]
    handCopy = convert_face_to_value(handCopy)
    
    for i in range(length):
        for j in range(13):
            if handCopy[i] == valueInt[j]:
                valueRepeats[j] += 1
    
    for i in range(13):
        print(f"{value[i]}: {valueRepeats[i]}")
    pass

def highest_pair():
    pass

print(three_of_a_kind(create_hand()))


