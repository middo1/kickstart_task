import random

colours = ["Blue" , "Green" , "Red" , "Yellow" , "Orange" , "White" , "Black"]


while True:
    try:
        if question == "yes":
            while True:
                colour = random.choice(colours)
                guess = input("Guess a colour: ")
                if guess == colour:
                    print("You're right" , guess , "is correct")
                    break
                else:
                    print("Uuuhh your guess is wrong the colour is" , colour)
                    question = input("Do wanna keep playing, pls choose yes or no: ")
                    break
        elif question == "no":
            break
        else:
            print("Wrong command")
            question = input("Do wanna keep playing, pls choose yes or no: ")
    except:
        question = None    
    while question == None:
        colour = random.choice(colours)
        guess = input("Guess a colour: ")
        if guess == colour:
            print("You're right" , guess , "is correct")
            break
        else:
            print("Uuuhh your guess is wrong the colour is" , colour)
            question = input("Do wanna keep playing, pls choose yes or no: ")
            break