import winsound
from player import characters
from map import locations
from items import items
from fileparser import dialogues
from game import *

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
    elif location_name == "shard":
        handle_first_floor_event(current_location)
    elif is_unconscious("bodyguard") and is_valid_event("bodyguard_unconscious", events_occurred):
        handle_bodyguard_unconscious_event(current_location)
    elif location_name == "sizzling floor":
        handle_cooking_event(current_location)
    elif location_name == "spooky_floor":
        handle_piers_event(current_location)
    elif time > 230:
        handle_bad_ending_event
    else:
        pass
    return victorious, events_occurred

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
    play_music("scream.wav")

def handle_first_floor_event(current_location):
    current_location_id = get_id(current_location['name'], locations)
    locations[current_location_id]['connected_places']["casino_floor_shard"]= 30

def handle_piers_event(current_location):
    time = 0
    print("A: I'll go with water.")
    print("B: Milk all the way!")
    print("C: I prefer the cereal on its own.")

    player_input = input("Pick A B or C to try and convince piers to let you up.")

    if (playerInput == "A" or "a"):
        print("Good choice. He gets up off of his chair. 'Congratulations' A circle of people come out of the shadow and start applauding.")
        time = 0
    if (playerInput == "B" or "a"):
        print("What. Get out. You walk away in shame.")
        time = 20
    if (playerInput == "C" or "c"):
        print("Hmmmm. I'll let you pass. But you have wait 5 minutes.")
        time = 5

    return time



def handle_good_ending_event(current_location):
    return True

def handle_bad_ending_event(current_location):
    return True

def handle_arrest_ending_event(current_location):
    return True

def handle_cooking_event(current_location):
    return True
