#!/usr/bin/python3
import winsound
from map import locations
from player import characters
from items import items
from gameparser import *
from figlet import f
from fileparser import dialogues
from events import *

def list_of_items(item_list):
    """An empty list is created, and all the item names are added to it
    A string of all the item names are returned

    >>> list_of_items(["dog", "man", "food"])
    "dog, man, food"

    """
    return ", ".join(item_list)

def print_location_items(location, items):
    """This takes in a location and the items dictionary.
       It then adds all the items from the location and obtains the names using the items dictionary and prints them out"""
    item_list = []
    for item in location["items"][:-1]:
        #Iterate through every item except the last one
        item_list.append(items[item]["name"])

    #TODO Fixing grammar
    if len(item_list) >= 1:
        print("The following items are here:\n%s and %s\n" %(list_of_items(item_list), location["items"][-1])) #There is a fish, a dog and a cat here.
    else:
        print("There's nothing on the floor to pick up.")

def print_location_characters(characters, location):
    """This takes in a character and the locations dictionary.
       It then checks through all the characters and checks if they're in the current location.
       If they're in the current location, then they're printed out.
    """
    character_list =  []

    for character in characters:
        if characters[character]["current_location"] == location and characters[character]["name"] != "player":
            character_list.append(characters[character]["name"])

    print("The following characters are here:\n%s\n" %(list_of_items(character_list)))

def print_location_details(characters, location, items):
    """This combines the print functions to print all the details about a room"""
    print_location_items(location, items)
    print_location_characters(characters, location)

def print_inventory_items(player_inventory, items): #items = ["wallet, luggage, ticket"]
    """
    This takes in a player inventory and the items dictionary.
    It iterates through the player's inventory and obtians the name of the item.
    The names of the items are then printed out.
    """
    item_list=[]
    for item in player_inventory:
        item_list.append(items[item]["name"])

    if item_list:
        print("You have " + list_of_items(item_list)  + ".")
    else:
        print("You have nothing in your inventory")

def print_location(characters, location, items):
    """
    WE NEED TO PRINT THE TIME AND THE WEATHER ASSOCIATED WITH THE TIME
    """
    print()
    print(f.renderText(location["name"].upper()))
    print()
    print(location["description"])
    print()
    print_location_details(characters, location, items)

def print_menu(connected_places, player_status, player_inventory, player_location, time):
    """
    NOT FINISHED WE'RE GOING TO ADD REST OF ACTIONS LATER
    """
    print("You can:")
    #GO TAKE DROP GIVE RIDE BUY FIGHT TALK

    for place in connected_places:
        time_taken = calculate_time(player_status, player_inventory,connected_places, place)
        print("GO to %s (%s Minutes)" %(locations[place]["name"], time_taken))
    #This shows the player a list of places they can go

    for item in player_location["items"]:
        print("TAKE %s" %(items[item]["name"]))
    #This shows the player a list of items they can take

    for item in player_inventory:
        print("DROP %s" %(items[item]["name"]))
    #This shows the player a list of items they can drop
    for item in player_location["items"]:
        if "purchasable" in items[item]["properties"]:
            print("BUY %s" %(items[item]["name"]))
    #ride, fight, talk
    for character in characters:
        if (characters[character]["current_location"] == player_location) and (characters[character]["name"] != "player"):
            if "aggressive" in characters[character]["status"]:
                print("Fight %s" %(characters[character]["name"]))
    #This shows the player a list of characters they can fight

    for character in characters:
        if (characters[character]["current_location"] == player_location) and (characters[character]["name"] != "player"):
            if "interactable" in characters[character]["status"]:
                print("Talk to %s" %(characters[character]["name"]))
    #This shows the player a list of characters they can talk to

def is_valid_player(npc, current_location):
    valid = False
    if npc['current_location'] == current_location:
        valid = True
    else:
        pass
    return valid

def is_valid_item(item_chosen, inventory):
    valid = False
    for item in inventory:
        if item_chosen == item:
            valid = True
        else:
            pass

    return valid

def convert_command(command, current_location):
    character_id = get_id(command[1],characters)
    if character_id:
        temp_command = command[2]
        command[2] = command[1]
        command[1] = temp_command
    else:
        pass
    return command

def is_valid_exit(connected_places, locations, chosen_location):

    """
    NOT DONE
    """

    valid = False
    for connected_place in connected_places:
        if chosen_location == locations[connected_place]['name'].lower():
            valid = True
    return valid

def is_unconscious(npc_name):
    npc_id = get_id(npc_name, characters)
    npc = characters[npc_id]
    valid = True
    if npc['status']['alive']:
        valid = False
    else:
        pass
    return valid


def update_status(npc):
    npc['status']['alive'] = False

def get_dialogue(npc, current_location_id, dialogues, scenario="default", mood="default"):
    dialogue = dialogues[current_location_id][npc][scenario][mood]
    return dialogue

def get_id(object, objects):
    for object_id in objects:
        if objects[object_id]['name'].lower() == object.lower():
            return object_id
        else:
            pass
def lock_in_player(location):
    for connected_place in location['connected_places']:
        for i in range(2):
            locations[connected_place]['entry_requirements'].append('padlock')

def unlock_in_player(location):
    for connected_place in location['connected_places']:
        for i in range(2):
            locations[connected_place]['entry_requirements'].remove('padlock')
def play_music(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)

def extract_music(location_name):
    location_id = get_id(location_name, locations)
    sound_file = locations[location_id]['music']
    return sound_file

def play_location_sound(location_name):
    sound_file = extract_music(location_name)
    play_music(sound_file)

def execute_go(new_location, current_location, locations, player_properties, inventory, time):
    """
    Almost done, just need to add the timer.
    """

    try:

        if is_valid_exit(current_location['connected_places'], locations, new_location):
            time += calculate_time(player_properties, inventory, current_location["connected_places"], new_location)
            current_location_id = get_id(new_location, locations)
            current_location = locations[current_location_id]

            play_location_sound(current_location['name'])
        #This moves the player, it also calculates how long the movement is going to take and adds it to the current time
    except KeyError:
        print(KeyError)
        print("You can't go to", new_location)
    return current_location, time

def execute_buy():
    pass


def execute_fight(player, npc_name):
    if is_killable(npc_name):
        npc_id = get_id(npc_name, characters)
        current_location = player['current_location']
        if is_valid_player(characters[npc_id], current_location):

            current_location_id = get_id(current_location['name'], locations)
            dialogue = get_dialogue(npc_id, current_location_id, dialogues, "hit")
            scenario = characters[npc_id]['status']['hit']

            print(dialogue[scenario])

            if dialogue[scenario] == "...":
                print("%s has died. You're a murderer." % npc_name)
                update_status(characters[npc_id])
            else:
                characters[npc_id]['status']['hit'] += 1


def execute_talk(npc_id, current_location_id, dialogues):

    dialogue = get_dialogue(npc_id, current_location_id, dialogues, "talk")
    print("\n'"+dialogue+"'\n")


def execute_give(item_name, player_inventory, npc_inventory):
    """Gives an item from your inventory to an npc's inventory"""

    player_inventory.remove(item_name)
    npc_inventory.append(item_name)


    return player_inventory, npc_inventory




def execute_take(item_id, current_location, player_inventory):
    """
    SOMEWHAT DONE
    """
    item_id = get_id(item_id,items)
    item_picked_up = False

    for item in current_location['items']:
        if item == item_id:
            #if calculate_mass(inventory, item):
            item_picked_up = True
            player_inventory.append(item)
            current_location['items'].remove(item)
        else:
            pass
    if not item_picked_up:
        print("You cannot take that.")
    return current_location, player_inventory


def execute_drop(item_id, current_location, player_inventory):
    """
    This takes in an item, the player's current_location and the player's inventory.
    It first checks whether the item is inside the player's inventory.
    If it is, then the item is removed from the player's inventory and is placed inside the current location's item list.
    """

    item_exists = False
    for item in player_inventory:
        if item == item_id:
            item_exists = True
            remove_item_from_player(item, player_inventory)
            current_location['items'].append(item)
        else:
            pass
    if not item_exists:
        print("You cannot drop that.")
    return current_location, player_inventory

def remove_item_from_player(item, player_inventory):
    """This remove the selected item from the players inventory"""
    player_inventory.remove(item)

def print_requirements(name, items):
    items = list_of_items(items)
    if 'padlock' in items:
        print("You cannot escape.")
    else:
        print("%s does not have %s." % (name, items))

def check_requirements(location):
    """This checks if the player has all the items needed in their inventory"""
    location_id = get_id(location, locations)
    valid = False
    requirements = locations[location_id]['entry_requirements']
    if requirements:
        npc_id = get_id(requirements[0], characters)
        npc = characters[npc_id]


        valid_items = 0
        items = 0


        for item in requirements[1:]:
            items += 1
            if item in npc['inventory']:
                valid_items += 1
            else:
                pass

        if items == valid_items:

            valid = True
        else:
            print_requirements(npc['name'],requirements[1:])
            pass
    else:
        valid = True
    return valid

def has_modifiers(inventory):
    valid = False
    for item in inventory:
        item_id = get_id(item,items)
        if 'fast' in items[item_id]['properties']:
            valid = True
        else:
            pass
    return valid

def calculate_time(player_properties, inventory, connected_places, chosen_location):
    """This calculates how long it'll take for the player to perform an action
        NOT FINSIHED YET
    """
    location_id = get_id(chosen_location, locations)
    time = connected_places[location_id]
    if has_modifiers(inventory):
        time = time * 0.5

    return time

def execute_command(command, locations, characters, time, dialogues):
    """
    This takes in a list. The list contains 2 parts. The verb and the noun.
    The verb is checked for what action it performs and the corresponding function is executed on the second part of the list (the noun).
    """

    player = characters['player']
    player_status = player["status"]
    player_inventory = player["inventory"]
    current_location = player["current_location"]



    if len(command) == 0:
        print("This is not a valid command type in help for a lits of valid commands")

    elif command[0] == "go":
        if len(command) > 1:

            if check_requirements(command[1]):
                current_location, time = execute_go(command[1], current_location, locations,  player_status, player_inventory, time)
                print(time)
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
                current_location, player_inventory = execute_take(command[1], current_location, player_inventory)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            current_location, player_inventory = execute_drop(command[1], current_location, player_inventory)
        else:
            print("Drop what?")

    elif command[0] == "give":
        if len(command) > 2:
            command = convert_command(command, current_location)
            item_id = get_id(command[1], items)
            npc_id = get_id(command[2], characters)
            npc_inventory = characters[npc_id]['inventory']
            if is_valid_item(items[item_id]['name'], player_inventory) and is_valid_player(characters[npc_id], current_location):
                player_inventory, npc_inventory = execute_give(items[item_id]['name'], player_inventory, npc_inventory)
                print("You have given %s your %s" %(characters[npc_id]["name"],command[1]))
            else:
                print("You cannot give that.")
        else:
            print("Give what?")

    elif command[0] == "ride":
        if len(command) > 1:
            current_location = execute_ride()
        else:
            print("Ride what?")

    elif command[0] == "buy":
        if len(command) > 1:
            player["money"], inventory = execute_buy()
        else:
            print("Buy what?")

    elif command[0] == "talk":
        if len(command) > 1:
            try:
                npc_id = get_id(command[1],characters)
                current_location_id = get_id(current_location['name'], locations)
                if is_valid_player(characters[npc_id], current_location):
                    execute_talk(npc_id, current_location_id, dialogues)
                else:
                    print("%s is not here." % npc_id)
            except KeyError:
                print("You cannot talk to that person")

    elif command[0] == "fight":
        if len(command) > 1:
            execute_fight(player, command[1])
        else:
            print("fight who?")

    elif command[0] == "help":
        print_menu(current_location["connected_places"], player_status, player_inventory, current_location, time)

    return current_location, player_inventory



def menu(exits, room_items, player, time):
    """
    NOT DONE

    """

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input, key_nouns, key_verbs)

    return normalised_user_input


# This is the entry point of our program
def main(characters, locations, items, dialogues):
    # Main game loop
    Victorious = False
    time = 0
    announced = False
    occurred_events = []
    while not Victorious:
        player = characters["player"]
        current_location = player["current_location"]
        inventory = player["inventory"]

        if not announced:
            print_location(characters, current_location, items)
            announced = True

        Victorious, occurred_events = listenForEvents(Victorious, occurred_events, time)
        if not Victorious:
            print_inventory_items(player["inventory"], items)
            print("What will you do?\n")

            command = menu(current_location["connected_places"], current_location["items"], player, time) #NOT WORKING YET
            player["current_location"], player["inventory"] = execute_command(command, locations, characters, time, dialogues)
            if player["current_location"] != current_location:
                announced = False





# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main(characters, locations, items, dialogues)
