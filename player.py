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
    name = "Bus Driver",
    status = {"mood":"good","hit":0, "alive":True, "killable":False, "hittable":False},
    inventory = [],
    current_location = locations["coach"]
    )

add_character("taxi_driver",
    name="Taxi Driver",
    status = {"hit":0, "alive":True, type:"killable"},
    inventory = [],
    current_location=locations["victoria_coach_station"]
    )

add_character("piers_morgan",
    name = "Piers Morgan",
    status = {"hit":0, "alive":True,"killable":False, "hittable":False},
    inventory =[],
    current_location = locations["piers_floor_shard"]
    )

add_character("waiter",
    name="Waiter",
    status = {"hit":0, "alive":True,"killable":False, "hittable":True},
    inventory = [],
    current_location = locations["wetherspoons"]
)

add_character("policeman",
    name="Policeman",
    status = {"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory = [],
    current_location = locations["wetherspoons"]
)

add_character("pikachu",
    name="Pikachu",
    status={"hit":0, "alive":True, "killable":False, "hittable":True},
    inventory = [],
    current_location=locations["monument_indoors"])

add_character("secretary",
    name="Secretary",
    status={"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory = [],
    current_location=locations['first_floor_shard'])

add_character("bodyguard",
    name="Bodyguard",
    status={"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory = [],
    current_location=locations['first_floor_shard'])

add_character("tourist",
    name="Tourist",
    status={"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory=[],
    current_location=locations['monument_outdoors'])

add_character("businessman",
    name="Businessman",
    status={"hit":0, "alive":True, "killable":False, "hittable":True},
    inventory=[],
    current_location= locations['first_floor_shard'])

add_character("chef",
    name="J. Wu",
    status={"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory=[],
    current_location= locations['cooking_floor_shard'])

add_character("dealer",
    name="Dealer",
    status={"hit":0, "alive":True, "killable":True, "hittable":False},
    inventory=[],
    current_location=locations['casino_floor_shard'])

add_character("pirate",
    name="Pirate",
    status={"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory=[],
    current_location=locations['cannon_floor_shard'])

add_character("cashier",
    name="Cashier",
    status={"hit":0, "alive":True, "killable":False, "hittable":False},
    inventory=[],
    current_location=locations['boots'])

add_character("padlock",
    name="padlock",
    status={"hit":0, "alive":True},
    inventory=[],
    current_location="")


"""Maybe change it so that you can pick a name"""

"""Due to the way we've changed how we represent the player, in order to call current_location we use characters["player"][current_location]"""
