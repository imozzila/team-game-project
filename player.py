from items import *
from map import locations

def add_character(id, name, status, inventory, current_location):
    characters[id] = {"name":name, "status":status, "inventory":inventory, "current_location":current_location}

characters = {}

add_character("player",
    name = "player",
    status = {},
    inventory = ["wallet", "luggage", "ticket"],
    current_location = locations["coach"]
    )

add_character("bus_driver",
    name = "bus driver",
    status = {"mood":"good"},
    inventory = [],
    current_location = locations["coach"]
    )

add_character("taxi_driver",
    name="taxi driver",
    status = {},
    inventory = [],
    current_location=locations["victoria_coach_station"]
    )

add_character("piers_morgan",
    name = "Piers Morgan",
    status = {},
    inventory =[],
    current_location = locations["piers_floor_shard"]
    )

add_character("waiter",
    name="Waiter",
    status = {},
    inventory = [],
    current_location = locations["wetherspoons"]
    )

add_character("policeman",
    name="Policeman",
    status = {},
    inventory = [],
    current_location = locations["wetherspoons"]
)

add_character("pikachu",
    name="Pikachu",
    status={"hit":0, "alive":True},
    inventory = [],
    current_location=locations["monument_indoors"])

add_character("padlock",
    name="padlock",
    status={},
    inventory=[],
    current_location="")
"""Maybe change it so that you can pick a name"""

"""Due to the way we've changed how we represent the player, in order to call current_location we use characters["player"][current_location]"""
