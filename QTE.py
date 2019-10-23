import time


def egg_flip():
    win = False
    startTime = time.time()
    playerInput = input("Type 'flip egg' to flip the egg. BE QUICK!")

    if str(playerInput) == "flip egg":
        endTime = round(time.time() - startTime, 0)
        if endTime > 5:
            print("Too slow!!")
        elif endTime < 5:
            print("Well done!")
            win = True
    else:
        print("'What are you doing??' said J. Wu 'HOW COULD YOU NOT EVEN FRY AN EGG, IT'S BASICALLY HATCHING'")
        print("Chef Wu had scared you away from the Shard. You ended up curled up outside of the shard crying, forcing you to miss your train back to Cardiff.")
    return win

def cannon():
    win = False
    print("The cannon is launching in 3 (Press enter as quickly as possible on go to lanuch the cannon)")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!!!")
    startTime = time.time()
    input("PRESS ENTER!!!!")
    endTime = round(time.time() - startTime, 0)
    if endTime < 2:
        print("Well done, a flying pirate soars across the room smashing the wall.")
        win = True
    else:
        print("You were too slow, the cannon malfunctions with a big bang glass flies across the room leaving you cowering in fear.")
        print("You leave the Shard, wondering why there was even a cannon in there.")
    return win
