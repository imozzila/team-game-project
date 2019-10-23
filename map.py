from items import *

locations = {}
"""

"""

def add_location(id, name, description, connected_places, items, entry_requirements):
    locations[id] = {"name":name, "description":description, "connected_places":connected_places, "items":items, "entry_requirements":entry_requirements}

add_location("coach",

    name="Coach",

    description = """You are in a run-down, dusty bus that looks like it could break down at any moment.
The driver is staring down at you with beady eyes awaiting your ticket.
You're estatic to arrive at London to meet your childhood friend, Kirill.


You must give the ticket to the bus driver to board the coach to London""",

    connected_places = {"victoria_coach_station":120},

    items = ["wagon wheels", "tape"],

    entry_requirements = []
)



add_location("victoria_coach_station",

     name="coach station",

    description = """You've arrived at London Victoria Coach Station and it's a gloomy 8am.
    As you step out of the coach, and grab your luggage, you push through the cluster of people
    in the coach station and head outside. You have agreed to meet Kirill at the top floor of the Shard.
    There is a huge Wetherspoons in the distance, no doubt full of responsible parents letting their
    children drink Dark Fruits. A homeless person is dancing a little ways down the road beneath
    the sign indicating Victoria Tube Station, and there is a line of taxis outside the coach station
    with very...reasonable rates. """,

    connected_places = {"wetherspoons":30, "taxi":5, "victoria_tube":20},

    items = ["coffee", "luggage", "molotov", "crayons"],

    entry_requirements = ["bus driver","ticket"]
)

add_location("wetherspoons",

         name = "Wetherspoons",

         description = """You enter the pub famed for its affordable food and drinks. The pub provides
a classic English interior that makes you feel right at home. There are plenty of people around,
causing a ruckus for the staff in this busy day. The menu has some great offers and there are a few
tables around that are available. You probably shouldn't eat before lunch with Kirill, but they
serve alcohol at any time of day here. """,

         connected_places = {"victoria_coach_station":30},


         items = ["beer", "whiskey", "coffee", "egg", "lamb"],

         entry_requirements = []

         )

add_location("taxi",

         name = "Taxi",

         description = """You call for a Taxi, a cab driver stops for you.

                        £5 for the fare, that's the best deal you'll get.""",

         connected_places = {"victoria_coach_station":5},

         items = [],

        entry_requirements = [])

add_location("victoria_tube",

             name = "Victoria Tube Station",

             description = """You enter a humid, busy tube station and descend down the escalator,
                            you see a sign showing different lines for the tube. There is a guy
                            playing saxophone, giving the tube station a jazzy vibe. You check the
                            map and it says Monument Station is the closest stop to the Shard.
                            Besides getting the train its just a waiting game until some dodgy
                            person tries to mug you here. """,

             connected_places = {"monument_indoors":10},

             items = ["beer", "skateboard", "cornetto", "tin foil", "milk"],

             entry_requirements = [])


add_location("monument_indoors",

        name = "Monument Underground",

        description="""You enter a grimy, loud and crowded station. As you hop off your carriage
                    and look around, you get harassed by a man in a Pikachu suit. He grips you
                    with the strength of a boulder. You struggle to escape but he won't let you go.""",

        connected_places={"monument_outdoors":5, "victoria_tube":10},

        items=["money", "keys"],

        entry_requirements = [])

add_location("monument_outdoors",

        name="Monument",

        description="""You walk outside of the station to find the iconic monument which commemorates
                    the Great Fire of London. The area is riddled with offices and buildings, with a
                    Boots store conveniently nearby. A stampede of Chinese tourists walk by with a tour guide.
                    You could go and get some painkillers after the fight with that Pikachu guy, or head
                    straight for the Shard.""",

        connected_places={"boots":5, "first_floor_shard":10},

        items=["steel ball", "pen", "gift card", "laces"],

        entry_requirements = [])

add_location("boots",

            name = "Boots",

            description = """You walk into the shop and instantly recognise the array of fragrances.
                            Paracetamol are only 40p, what a bargain! Not much to do here otherwise...""",

            connected_places = {"monument_outdoors":5},

            items = [],

            entry_requirements = [])

add_location("first_floor_shard",

        name = "First Floor of the Shard",

        description="""You look up at the towering building in amazement. You feel like you're
                    almost at the end and are excited to meet your friend. You enter the building
                    to find yourself completely out of place. You're surrounded by businessmen in
                    well-attired clothing. There is a secretary you can talk to, a security guard
                    looking unhappy, and a busy elevator that can take you to the next floor.""",

        connected_places={"casino_floor_shard":10},

        items=["pen", "paper", "coffee", "lego yoda", "tissue box", "fan"],

        entry_requirements = [])

add_location("casino_floor_shard",

             name = "Casino Floor",

             description="""You enter the casino floor and are immediately greeted by the smell
                         of places where dreams come to die. There is a Honda Civic rotating on a
                         plate as a grand prize. The sound of slot machines giving people false hope
                         is impossible to ignore. A lady carrying champagne and food on a tray walks
                         past in the direction of some peculiar looking stairs. You could go and give
                         the slots a run for their money, join a roulette table, or follow the lady
                         up the weird looking staircase.""",

             connected_places = {"cannon_floor_shard":10, "first_floor_shard":10},

             items = ["Honda Civic", "whiskey", "beer", "phone", "cigarettes"],

             entry_requirements = [])

add_location("cannon_floor_shard",

             name = "Weird Floor",

             description = """This floor definitely has a weird feeling to it. You look around
                            for any signs of movement. The floor has six great pillars supporting the ceiling.
                            As you notice all the food remains scattered acorss the floor, a man holding a giant
                            ship's cannon steps out from behind one of the pillars aiming right at you.

                            "YO-HO AND FIDDLY-DEE, IT'S A PIRATE'S LIFE FOR MEEE"

                            He lights the cannon fuse and laughs maniacally...""",
                            #Don't know what sort of encounter we want here
             connected_places = {"casino_floor_shard":10, "cooking_floor_shard":10},

             items = ["salmon", "steel ball", "weetabix", "cornflakes", "milk", "teapot", "tissue box", "racket"],

             entry_requirements = [])

add_location("cooking_floor_shard",

             name = "Sizzling Floor",

             description = """You survived the cannon man and beeline it for the stairs again, going up
                            another floor. You can smell the source of some fine dining and follow the scent into
                            a huge, advanced kitchen. A woman appears in front of you before you can blink and
                            waves her spatula in front of you menacingly. Her nametag says "J. Wu", and her
                            hat is almost 60cm tall, indicating some serious cooking prestige.

                            "ARE YOU THE IDIOT WHO COOKED THIS SQUID?! IT'S SO RAW I CAN STILL HEAR IT
                            TELLING SPONGEBOB TO F*** OFF! GET OUT OF MY KITCHEN!"

                            The staircase is only a few meters away, you could get to it without being
                            stabbed with a cooking utensil if you're fast... """,

            connected_places = {"cannon_floor_shard":10, "piers_floor_shard":10},

             items = ["tin foil", "salmon", "pan", "egg", "lamb", "butter", "jar", "lime"],

             entry_requirements = [])

add_location("piers_floor_shard",

             name = "Spooky Floor",


             description = """Stained with eggs, meat juices, flour and other assorted foods, you make it to the
                            staircase once again. Clambering up the carpeted steps, you feel a cold chill down your
                            spine. There is an ominous wind around you and a single wooden door covered in claw-marks
                            in front of you. The door does not appear to be locked, so you turn the handle and enter.
                            The room has bookshelves across both walls, a great mahogany desk in the middle, and a
                            tall, leather chair facing away from you out the window. The air you exhale curls up in
                            front of you from the cold, and the chair begins to slowly rotate...

                            Piers Morgan now faces you, staring straight through you with a vacant gaze.

                            "Do you eat cereal with or without water?" """,

            connected_places = {"cooking_floor_shard":10, "top_floor_shard":10},

             items = [],

             entry_requirements = [])

add_location("good_top_floor_shard",

            name = "Top Floor",

            description = """You have chosen..... wisely.
                        Kirill greets you with a smile and welcomes you to the table you have reserved.
                        He was waiting for you to arrive and has ordered your favourite bottle of vintage
                        Dom Perignon 1985 for your table, and a bowl of cereal with water, on him! You
                        have a great catch-up with your best friend and drink and chat till the early
                        hours of the evening. You end the meeting with a fist-bump and grab your jacket
                        to leave. It's 7:30pm, now you just have to get home...
                        The End. :)
                        """,

            connected_places = {"piers_floor_shard":10},

            items = [],

            entry_requirements = [])

add_location("bad_top_floor_shard",

            name = "Top Floor",

            description = """You have chosen..... poorly.
                        You took too long to get here and Kirill is long gone. He ordered your favourite meal,
                        kale juice and pasta with hot dogs cut up into little pieces in it, but it has been cold
                        for a while. He left your half of the bill with a sad face drawn on it.
                        The End. :(
                        """,

            connected_places = {"piers_floor_shard":10},

            items = [],

            entry_requirements = [])
