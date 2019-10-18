from items import *

rooms = {}

"""

"""



def add_room(id, name, description, connected_places, items, scenario_branch):
    items[id] = {"name":name, "description":description, "connected_places":connected_places, "items":items}

add_room("coach",

        name="Coach outside cardiff uni",

        description = """You are in a run-down, dusty bus that looks like it could break down
        at any moment. The drive is staring down at you with beady eyes awaiting you ticket. You're estatic to arrive at London to meet
        our childhood friend, Alex.""",

        connected_places = {victoria_coach_station:120},

        items = ["wagon wheels", "tape"],

        scenario_branch = []

        )



add_room("victoria_coach_station",

         name="London Victoria coach station"

         description = """You've arrived at London Victoria Coach Station and it's a gloomy 8am.
         As you step out of the coach, and grab your luggage, you push through the cluster of people
         in the coach station and head outside. You have agreed to meet Kirill at the top floor of the Shard.""",

         connected_places = {wetherspoons:30, taxi:10, tube:20},

         items = ["coffee", "luggage", "molotov", "crayons"],

         scenario_branch = []

         )

add_room("wetherspoons",

         name = "Wetherspoons"

         description = """You enter the pub famed for its affordable food and drinks. The pub provides
         a classic English interior that makes you feel right at home. There are plenty of people around,
         causing a ruckus for the staff in this busy day.""",

         connected_places = {victoria_coach_station:30}

         items = ["beer", "whiskey", "coffee", "egg", "pork"],

         scenario_branch = []

         )

add_room("taxi",

         name = "taxi"

         description = """You call for a Taxi, a cab driver stops for you.""",

         connected_places = {},

         items = []

         scenario_branch = []

         }
