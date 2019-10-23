import time


def egg_flip():
    startTime = time.time()
    playerInput = input("Type 'flip egg' to flip the egg.")

    if playerInput == "flip egg":
        endTime = round(time.time() - startTime, 0)
        if endTime > 5:
            print("Too slow!!")
            print(endTime)
            return False
        elif endTime < 5:
            print("Well done!")
            print(endTime)
            return True
    else:
        print("What are you typing?")
        return False

def cannon():
    print("The cannon is launching in 3 (Press enter as quickly as possible on go to lanuch the cannon)")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!!!")
    startTime = time.time()
    playerInput = input("PRESS ENTER!!!!")
    endTime = round(time.time() - startTime, 0)
    if endTime < 2:
        print("Well done, a flying pirate soars across the room smashing the wall.")
    else:
        print("You were too slow, the cannon malfunctions with a big bang glass flies across the room leaving you cowering in fear.")
