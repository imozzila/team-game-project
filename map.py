from items import *

locations = {}
"""

"""

def add_location(id, name, description, connected_places, items, scenario_branch):
    locations[id] = {"name":name, "description":description, "connected_places":connected_places, "items":items}

add_location("coach",

    name="Coach to London",

    description = """You are in a run-down, dusty bus that looks like it could break down at any moment.
The driver is staring down at you with beady eyes awaiting your ticket.
You're estatic to arrive at London to meet your childhood friend, Kirill.""",

    connected_places = {"victoria_coach_station":120},

    items = ["wagon wheels", "tape"],

    scenario_branch = []
)



add_location("victoria_coach_station",

     name="coach station",

    description = """You've arrived at London Victoria Coach Station and it's a gloomy 8am.
    As you step out of the coach, and grab your luggage, you push through the cluster of people
    in the coach station and head outside. You have agreed to meet Kirill at the top floor of the Shard.""",

    connected_places = {"wetherspoons":30, "taxi":5, "tube":20},

    items = ["coffee", "luggage", "molotov", "crayons"],

    scenario_branch = []
)

add_location("wetherspoons",

         name = "Wetherspoons",

         description = """You enter the pub famed for its affordable food and drinks. The pub provides
         a classic English interior that makes you feel right at home. There are plenty of people around,
         causing a ruckus for the staff in this busy day.""",

         connected_places = {"victoria_coach_station":30},


         items = ["beer", "whiskey", "coffee", "egg", "pork"],

         scenario_branch = []

         )

add_location("taxi",

         name = "Taxi",

         description = """You call for a Taxi, a cab driver stops for you.

                        £5 for the fare, that's the best deal you'll get.""",

         connected_places = {"victoria_coach_station":5},

         items = [],

         scenario_branch = [])

add_location("victoria_tube",

             name = "Victoria Tube Station",

             description = """You enter a humid, busy tube station and descend down the escalator,
                            you see a sign showing different lines for the tube. There is a guy
                            playing saxophone, giving the tube station a jazzy vibe."""

             connected_places = {"monument_indoors":10},

             items = ["beer", "skateboard", "cornetto", "tin foil", "milk"],

             scenario_branch = [])


add_location("monument_indoors",

        name = "Monument Underground",

        description="""You enter a grimy, loud and crowded station. As you hop off your carriage
                    you get harassed by a man in a Pikachu suit. He grips you with the strength
                    of a boulder. You struggle to escape but he won't let yo go.""",

        connected_places={},

        items=["money, keys"],

        scenario_branch=[])

add_location("monument_outdoors",

        name="Monument",

        description="""You walk outside of the station to find the iconic monument which commemorates
                    the Great Fire of London. The area is riddles with offices and buildings, with a
                    Boots store conveniently nearby. A stampede of Chinese tourists walk by with a tour guide.""",

        connected_places={"boots":5, "first_floor_shard":10"},

        items=["steel ball", "pen", "gift card", "laces"],

        scenario_branch=[])

add_location("first_floor_shard",

        name = "First Floor of the Shard",

        description="""You look up at the towering building in amazement. You feel like you're
                    almost at the end and are excited to meet your friend. You enter the building
                    to find yourself completely out of place. You're surrounded by businessmen in
                    well-attired clothing. You're completely lost in the ground floor and have no
                    idea where the elevator or stairs are.""",

        connected_places={"casino_floor_shard":10},

        items=["pen", "paper", "coffee", "lego yoda", "tissue box", "fan"],

        scenario_branch=[])

<<<<<<< HEAD
=======
add_location("casino_floor_shard",

             name = "Casino Floor",

             description="""You enter the casino floor and are immediately greeted by the smell
                         of places where dreams come to die. There is a Honda Civic rotating on a
                         plate as a grand prize. The sound of slot machines giving people false hope
                         is impossible to ignore. A lady carrying champagne and food on a tray walks
                         past in the direction of some peculiar looking stairs.""",

             connected_places = {"cannon_floor_shard":10, "first_floor_shard":10},

             items = ["Honda Civic", "whiskey", "beer", "phone", "cigarettes"],

             scenario_branch = [])

add_location("cannon_floor_shard",

             name = "Weird Floor",

             description = """This floor definitely has a weird feeling to it. You look around
                            for any signs of movement. The floor has six great pillars supporting the ceiling.
                            As you notice all the food remains scattered acorss the floor, a man holding a giant
                            ship's cannon steps out from behind one of the pillars aiming right at you.

                            "YO-HO AND FIDDLY-DEE, IT'S A PIRATE'S LIFE FOR MEEE"

                            He lights the cannon fuse and laughs maniacally...""",

             connected_places = {"casino_floor_shard":10, "cooking_floor_shard":10}

             items = ["salmon", "steel ball", "weetabix", "corn flakes", "milk", "teapot", "tissue box", "racket", "frying pan"],

             scenario_branch = [])

add_location("cooking_floor_shard",

             name = "Sizzling Floor",

             description = """You survive the cannon man and beeline it for the stairs again, going up
                            another floor. You can smell the source of some fine dining and follow the scent into
                            a huge, advanced kitchen. A man wearing a 60cm tall chef's hat approaches you
                            brandishing a spatula, and roars at you

                            "THIS IS KIRILL'S KITCHEN, WEAR YOUR APRON OR YOUR LUNCH WILL BE A KNUCKLE SANDWICH!" """
             items = [],
             scenario_branch = [])

add_location("piers_floor_shard",
             name = "Spooky Floor",
             description = "",
             items = [],
             scenario_branch = [])
>>>>>>> 94aaa9a2bb7422324b0137e95b0d94ed9a1285fe

add_location("top_floor_shard",
        name="Top Floor",
        description="",
        connected_places={},
        items = [],
        scenario_branch = [])
