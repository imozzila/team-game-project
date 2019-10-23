import random

def high_lower(inventory):
    print("Welcome to higher and lower!")

    count = 0
    win = False
    final_num = random.randint(0, 500)
    while not win:
        player_guess = input("Guess the number")
        if player_guess > final_num:
            print("Too high!")
            count+=1
        elif player_guess < final_num:
            print("Too low!")
            count+=1
        elif count > 5:
            print("You took more than 5 turns...")
            print("You win a think python 2e book!")
        else:
            print("You Win!")
            print("You lost. Thousands of kids gather around in a circle around you can point their fingers at you laughing. You pathetic loser.")
            win = True
    if count > 5:
        money = money /2
    else:
        money
