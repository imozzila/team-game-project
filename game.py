#!/usr/bin/python3

from map import locations
from player import characters
from items import items
from gameparser import *



def list_of_items(item_list):
    """An empty list is created, and all the item names are added to it
    A string of all the item names are returned

    >>> list_of_items(["dog", "man", "food"])
    "dog, man, food"

    """
    new_item_list =  []
    for item in item_list:
        new_item_list.append(item)
    return ", ".join(new_item_list)

def print_location_items(location, items):
    """This takes in a location and the items dictionary.
       It then adds all the items from the location and obtains the names using the items dictionary and prints them out"""
    item_list = []
    for item in location["items"]:
        item_list.append(items[item]["name"])

    if item_list:
        items = list_of_items(item_list) # locations["items"] = ["wagon wheels", "tape"]
    else:
        pass

def print_location_characters(characters, location):
    """This takes in a character and the locations dictionary.
       It then checks through all the characters and checks if they're in the current location.
       If they're in the current location, then they're printed out.
    """
    character_list =  []

    for character in characters:
        if characters[character]["current_location"] == location:
            character_list.append(characters[character]["name"])

    print("The " + ", ".join(character_list) + " are here")

def print_location_details(characters, location, items):
    """This combines the print functions to print all the details about a room"""
    print_location_items(location, items)
    print_location_characters(characters, location)

def print_inventory_items(player_inv, items): #items = ["wallet, luggage, ticket"]
    """
    This takes in a player inventory and the items dictionary.
    It iterates through the player's inventory and obtians the name of the item.
    The names of the items are then printed out.
    """
    item_list=[]
    for item in player_inv:
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
    print(location["name"].upper())
    print()
    print(location["description"])
    print()
    print_location_details(characters, location, items)

def print_menu(connected_places, player_status, player_inventory, time):
    """
    NOT FINISHED WE'RE GOING TO ADD REST OF ACTIONS LATER
    """
    print("You can:")
    #GO TAKE DROP GIVE RIDE BUY FIGHT TALK
    for place in connected_places:
        time_taken = calculate_time(player_status, player_inventory,connected_places, place)
        print("You can GO to %s (%s MINS)" %(place, time_taken))

    #for loc_item in loc_items:
        #print("TAKE %s to take %s." %(room_item['id'].upper(),room_item['name']))
    #for inv_item in inv_items:
        #print("DROP %s to drop your %s." %(inv_item['id'].upper(),inv_item['name']))


    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """
    NOT DONE
    """
    return chosen_exit in exits


def execute_go(direction, current_location, player_properties, inventory, time):
    """NOT DONE
    """
    try:
        new_room = move(current_location['exits'],direction)
        new_time = time + calculate_time(player_properties, inventory, current_location['exits'])
        #This moves the player, it also calculates how long the movement is going to take and adds it to the current time
        return new_room, new_time
    except KeyError:
        print("There is nothing %s of here." % direction)



def execute_give(item_id, inventory, npc_inventory):
    """Gives an item from your inventory to an npc's inventory"""


def execute_take(item_id, current_location, inventory):
    """
    NOT DONE
    """
    item_picked_up = False

    for item in current_location['items']:
        if item['id'] == item_id:
            if calculate_mass(inventory, item):
                item_picked_up = True
                inventory.append(item)
                current_location['items'].remove(item)
        else:
            pass
    if not item_picked_up:
        print("You cannot take that.")
    return current_location, inventory


def execute_drop(item_id, current_location, inventory):
    """
    NOT DONE
    """
    item_exists = False
    for item in inventory:
        if item['id'] == item_id:
            item_exists = True
            current_location['items'].append(item)
            inventory.remove(item)
        else:
            pass
    if not item_exists:
        print("You cannot drop that.")
    return current_location, inventory

def remove_item_from_player(item, inventory):
    """This remove the selected item from the players inventory"""

def check_requirements(item_needed, inventory):
    """This checks if the player has all the items needed in their inventory"""

def calculate_time(player_properties, inventory,connected_places, place):
    """This calculates how long it'll take for the player to perform an action"""
    time = connected_places[place] #simply a quick fix, we still need to worry about modifiers
    return time

def execute_command(command, current_location, inventory, time):
    """
    NOT DONE
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            current_location, time = execute_go(command[1], current_location, player_properties, inventory, time)
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            current_location, inventory = execute_take(command[1], current_location, inventory)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            current_location, inventory = execute_drop(command[1], current_location, inventory)
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")
    return current_location, inventory

def menu(exits, room_items, player, time, key_nouns, key_verbs):
    """
    NOT DONE

    """

    # Display menu
    player_status = player["status"]
    player_inventory = player["inventory"]
    print_menu(exits, player_status, room_items, time)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input, key_nouns, key_verbs)

    return normalised_user_input


def move(exits, direction):
    """

    """

    # Next room to go to
    return rooms[exits[direction]]

# This is the entry point of our program
def main(characters, items, key_nouns, key_verbs):
    # Main game loop
    Victorious = False
    time = 0
    while not Victorious:
        player = characters["player"]
        current_location = player["current_location"]
        print_location(characters, current_location, items)

        print_inventory_items(player["inventory"], items)
        command = menu(current_location["connected_places"], current_location["items"], player, time, key_nouns, key_verbs) #NOT WORKING YET
        execute_command(command, current_location, player["inventory"], time)
        #current_location, inventory = execute_command(command, current_location, inventory)
        #Victorious = check_victory(current_location, Victorious)
        Victorious = True



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main(characters, items, key_nouns, key_verbs)
