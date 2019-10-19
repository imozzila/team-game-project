from items import *
from map import rooms

def add_character(id, name, status, inventory, current_room):
    items[id] = {"name":name, "status":status, "inventory":inventory, "current_room":current_room}

characters = {}

add_character("player",
    name = "player",
    status = [],
    inventory = ["wallet", "luggage", "ticket"],
    current_room = rooms["Reception"]
    )


"""Maybe change it so that you can pick a name"""

"""Due to the way we've changed how we represent the player, in order to call current_room we use characters["player"][current_room]"""
    
