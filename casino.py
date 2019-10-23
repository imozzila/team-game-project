import random

def high_lower(inventory):
    print("Welcome to higher and lower!")
    print("Guess the number between 1 and 10")
    count = 0
    win = False
    final_num = random.randint(0, 10)
    while not win and count < 5:
        player_guess = int(input("Guess the number\n"))
        if player_guess > final_num:
            print("Too high!")
        elif player_guess < final_num:
            print("Too low!")
        elif player_guess == final_num:
            print("You win a think python 2e book!")
            win = True
        count += 1
    if not win:
        print("You took more than 5 turns...")
        print("You lost. Thousands of kids gather around in a circle around you can point their fingers at you laughing. You pathetic loser.")
    return win
    
