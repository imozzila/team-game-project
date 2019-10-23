import random

def high_lower():
    print("Welcome to higher and lower!")
    print("Guess the number between 1 and 10")
    count = 0
    win = False
    final_num = random.randint(1, 10)
    while not win and count < 5:
        valid_input = False

        while not valid_input:
            try:
                player_guess = int(input("Guess the number\n"))
                valid_input = True
            except:
                print("Please enter a number")


        if player_guess > final_num:
            print("Too high!")
        elif player_guess < final_num:
            print("Too low!")
        elif player_guess == final_num:
            print("You win a sense of pride and accomplishment!")
            win = True
        count += 1
    if not win:
        print("You took more than 5 turns...")
        print("You lost. Thousands of kids gather around in a circle around you can point their fingers at you laughing. You pathetic loser.")
        print("Due to the embarrassment of your loss. You just go back home to Cardiff, drinking away with some VKs. You were never the same again.")
    return win
