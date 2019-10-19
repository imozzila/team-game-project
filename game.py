#!/usr/bin/python3

from map import locations
from player import characters
from items import *
from gameparser import *



def list_of_items(items):
    """An empty list is created, and all the item names are added to it
    A string of all the item names are returned"""
    item_list =  []
    for item in items:
        item_list.append(item["name"])
    return ", ".join(item_list)

def print_location_items(location):
    if location['items']:
    #if the list is empty this line returns false
        items = list_of_items(location['items']['name'])
        print("There is %s here.\n" % items)
    else:
        pass

def print_location_characters(characters, location):
    character_list =  []
    for character in characters:
        if character["current_location"] == location:
            character_list.append(character)

    print(", ".join(character_list))

def print_location_details(characters, location):
    """ This combines the print functions to print all the details about a room"""
    print_location_items(location)
    print_location_characters(characters, location)




def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if items:
        items = list_of_items(items)
        print("You have %s.\n" % items)
    else:
        pass

def print_location(characters, location):
    """
    WE NEED TO PRINT THE TIME AND THE WEATHER ASSOCIATED WITH THE TIME
    """
    # Display room name

    print()
    print(location["name"].upper())
    print()
    # Display room description
    print(location["description"])
    print()
    print_location_details(characters, location)

    #
    # COMPLETE ME!
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(connected_places, characters, time):
    """

    """
    print("You can:")
    # Iterate over available exits
    #GO TAKE DROP GIVE RIDE BUY FIGHT TALK 
    for place in connected_places:
        time_taken = calculate_time(characters["player"]["status"], characters["player"]["inventory"], time)
        print("You can GO to %s (%s MINS)" %(place, time_taken))

    for loc_item in loc_items:
        print("TAKE %s to take %s." %(room_item['id'].upper(),room_item['name']))
    for inv_item in inv_items:
        print("DROP %s to drop your %s." %(inv_item['id'].upper(),inv_item['name']))
    # COMPLETE ME!
    #

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """
    """
    return chosen_exit in exits


def execute_go(direction, current_location, player_properties, inventory, time,):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is)
    """
    try:
        new_room = move(current_location['exits'],direction)
        new_time = time + calculate_time(player_properties, inventory, time)
        return new_room, new_time
    except KeyError:
        print("There is nothing %s of here." % direction)
    #calculate time


def execute_give(item_id, inventory, npc_inventory):
    """Gives an item from your inventory to an npc's inventory"""


def execute_take(item_id, current_location, inventory):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
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
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
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

def calculate_time(player_properties, inventory, time):
    """This calculates how long it'll take for the player to perform an action"""

def execute_command(command, current_location, inventory):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            current_location, time = execute_go(command[1],current_location)
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

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

# This is the entry point of our program
def main(characters):
    # Main game loop
    Victorious = False
    time = 0
    while not Victorious:

        print_location(characters, characters["player"]["current_location"])

        print_inventory_items(characters["player"]["inventory"])

        # Show the menu with possible actions and ask the player
        command = menu(current_location["exits"], current_location["items"], inventory)

        # Execute the player's command
        current_location, inventory = execute_command(command, current_location, inventory)
        Victorious = check_victory(current_location, Victorious)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main(characters)
