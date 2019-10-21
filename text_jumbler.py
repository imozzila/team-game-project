import random


Player['DrunkenState'] = "Sober"
NoOfDrinks = 0

def JumbleText(Message):
    word = ""
    Words = []
    for character in Message:
        if character == " ":
            Words.append(word)
            word = ""
        elif character.isalpha():
            word += character
    Words.append(word)
    print(Words)
    for word in Words:
        LengthOfWord = len(word)
        word = list(word)
        middle = word[1:LengthOfWord-1]
        random.shuffle(middle)
        word[1:LengthOfWord-1] = middle
        word = ''.join(word)
        print(word)

def drink(Player):
    NoOfDrinks += 1
    if NoOfDrinks >= 2:
        Player['DrunkenState'] = "Tipsy"
    elif NoOfDrinks >= 6:
        Player['DrunkenState'] = "Drunk"
    elif NoOfDrinks >= 10:
        Player['DrunkenState'] = "Wasted"
    else:
        Player['DrunkenState'] = "Sober"

JumbleText("Wouldnt I be sweet")
