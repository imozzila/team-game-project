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

def listenForEvents(events_occurred):
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
    else:
        pass
    return events_occurred

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
    winsound.PlaySound(scream.wav, winsound.SND_FILENAME)
    print("""Since the pikachu man is immobilized, you can now move on""")
