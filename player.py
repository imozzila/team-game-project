from items import *
from map import locations

def add_character(id, name, status, inventory, current_location):
    characters[id] = {"name":name, "status":status, "inventory":inventory, "current_location":current_location}

characters = {}

add_character("player",
    name = "player",
    status = [],
    inventory = ["wallet", "luggage", "ticket"],
<<<<<<< HEAD
    current_room = rooms["Reception"])
=======
    current_location = locations["coach"]
    )
>>>>>>> 02418b4419b7781add67b544eabbddf02c96b816

add_character("bus_driver",
              name = "bus driver",
              status = [],
              inventory = [],
              current_location = locations["coach"]
              )


"""Maybe change it so that you can pick a name"""

"""Due to the way we've changed how we represent the player, in order to call current_location we use characters["player"][current_location]"""

for character in characters:
    characters[character]['name']
