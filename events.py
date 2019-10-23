import winsound
from player import characters
from map import locations
from items import items
from fileparser import dialogues
from game import *
from QTE import *
from casino import *

def is_valid_event(event, events_occurred):
    valid = False
    if event in events_occurred:
        pass
    else:
        valid = True
    return valid

def listenForEvents(victorious, events_occurred, time):
    player = characters['player']
    current_location = player['current_location']
    location_name = current_location['name'].lower()

    if location_name == "monument underground" and is_valid_event("pikachu", events_occurred):
        events_occurred.append("pikachu")
        handle_pikachu_event(current_location)
    elif location_name == "taxi":
        handle_taxi_event(current_location)
    elif 'ticket' in characters['bus_driver']['inventory'] and is_valid_event("ticket", events_occurred):
        events_occurred.append("ticket")
        handle_bus_event(current_location)
    elif is_unconscious("pikachu") and is_valid_event("pikachu_unconscious", events_occurred):
        events_occurred.append("pikachu_unconscious")
        handle_pikachu_unconscious_event(current_location)
    elif location_name == "shard" and is_valid_event("shard", events_occurred):
        events_occurred.append("shard")
        handle_first_floor_event(current_location)
    elif is_unconscious("businessman") and is_valid_event("businessman_unconscious", events_occurred):
        events_occurred.append("businessman_unconscious")
        handle_businessman_unconscious_event(current_location)
    elif location_name == "casino floor" and is_valid_event("casino_floor", events_occurred):
        events_occurred.append("casino_floor")
        victorious = handle_casino_event(current_location)
    elif location_name == "sizzling floor" and is_valid_event("sizzling_floor", events_occurred):
        events_occurred.append("sizzling_floor")
        victorious = handle_cooking_event(current_location)
    elif location_name=="top floor" and time > 300:
        victorious = handle_bad_ending_event(current_location)
    elif location_name=="top floor" and time <= 300:
        victorious = handle_good_ending_event(current_location)
    elif location_name == "spooky floor" and is_valid_event("spooky_floor", events_occurred):
        events_occurred.append("spooky_floor")
        time += handle_piers_event(current_location)
    elif location_name == "weird floor" and is_valid_event("weird_floor", events_occurred):
        events_occurred.append("weird_floor")
        victorious = handle_weird_event(current_location)
    else:
        pass
    return victorious, events_occurred, time

def handle_pikachu_event(current_location):
    scenario = "struggle"
    location_id = get_id(current_location['name'], locations)
    dialogue = get_dialogue("pikachu", location_id, dialogues, scenario)
    lock_in_player(current_location)
    print()
    print("'%s'" %(dialogue))
    print()
    print("The pikachu man is persistent in you giving him money.")

def handle_bus_event(current_location):
    scenario="ticket"
    location_id=get_id(current_location['name'], locations)
    dialogue = get_dialogue("bus_driver", location_id, dialogues, scenario)
    print()
    print("'%s'" %(dialogue))
    print()
    print("""

It seems as though you might be able to get to the coach station now.

    """)

def handle_taxi_event(current_location):
    print()

def handle_pikachu_unconscious_event(current_location):
    unlock_in_player(current_location)
    print("""Since the pikachu man is immobilized, you can now move on""")
    #play_music("scream.wav")

def handle_businessman_unconscious_event(current_location):
    current_location_id = get_id(current_location['name'], locations)
    locations[current_location_id]['connected_places']["casino_floor_shard"]= 10

def handle_first_floor_event(current_location):
    current_location_id = get_id(current_location['name'], locations)
    locations[current_location_id]['connected_places']["casino_floor_shard"]= 30

def handle_piers_event(current_location):
    time = 0
    print("A: I'll go with water.")
    print("B: Milk all the way!")
    print("C: I prefer the cereal on its own.")
    playerInput = input("Pick A B or C to try and convince piers to let you up.\n")
    valid = False
    while not valid:
        if (playerInput == "A" or playerInput == "a"):
            print("Good choice. He gets up off of his chair. 'Congratulations' A circle of people come out of the shadow and start applauding.")
            time = 0
            valid = True
        elif (playerInput == "B" or playerInput == "b"):
            print("What. Get out. You walk away in shame.")
            time = 20
            valid = True
        elif (playerInput == "C" or playerInput == "c"):
            print("Hmmmm. I'll let you pass. But you have wait 5 minutes.")
            time = 5
            valid = True
        else:
            print("Please enter a valid input")

    return time

def handle_casino_event(current_location):
    victorious = high_lower()
    return not victorious

def handle_good_ending_event(current_location):
    print("""You have chosen..... wisely.
    Kirill greets you with a smile and welcomes you to the table you have reserved.
    He was waiting for you to arrive and has ordered your favourite bottle of vintage
    Dom Perignon 1985 for your table, and a bowl of cereal with water, on him! You
    have a great catch-up with your best friend and drink and chat till the early
    hours of the evening. You end the meeting with a fist-bump and grab your jacket
    to leave. It's 7:30pm, now you just have to make it back home...
    The End. :)
    """)
    return True

def handle_bad_ending_event(current_location):
    print("""You have chosen..... poorly.
You took too long to get here and Kirill is long gone. He ordered your favourite meal,
kale juice and pasta with hot dogs cut up into little pieces in it, but it has been cold
for a while. He left your half of the bill with a sad face drawn on it.
The End."""
)

def handle_cooking_event(current_location):
    victorious = egg_flip()
    return not victorious

def handle_weird_event(current_location):
    victorious = cannon()
    return not victorious
