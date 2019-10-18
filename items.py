items = {}
def add_item(id, name, mass, properties, description):
    items[id] = {"name":name, "mass":mass, "properties":properties, "description":description}

add_item("wallet",
    name = "a wallet",
    mass = 0.3,
    properties = ["container", "droppable", "light"],
    description="")


add_item("luggage",
    name= "luggage",
    mass =  2,
    properties = [],
    description = "")


add_item("money",
    name= "money",
    mass = 0.5,
    properties = [],
    description ="")

add_item("ticket",
    name = "a coach ticket",
    mass = 0.1,
    properties = [],
    description ="")

add_item("phone",
    name= "a smartphone",
    mass= 0.2,
    properties = [],
    description="")

add_item("tape",
    name= "duck tape",
    mass= 1,
    properties = [],
    description = "You never know when this might come in handy.")

add_item("salmon",
    name="a fillet of salmon",
    mass= 0.5,
    properties = [],
    description ="Sometimes, you just gotta treat yourself with some fish.")

add_item("molotov",
    name ="a molotov",
    mass =0.7,
    properties = [],
    description ="The solution to every problem is to create another problem.")

add_item("steel ball",
    name = "a steel ball",
    mass = 5,
    properties = [],
    description= "")

add_item("plank",
    name="a wooden plank",
    mass=2.5,
    properties = [],
    description= "")

add_item("pen",
    name="a pen",
    mass= 0.1,
    properties = [],
    description = "")

add_item("paper",
    name="paper",
    mass=0.1,
    properties = [],
    description= "")

add_item("helmet",
    name="a helmet",
    mass= 0.5,
    properties = [],
    description= "")

add_item("crayons",
    name = "a box of crayons",
    mass = 0.2,
    properties = [],
    description = "")

add_item("matches",
    name="a box of matches",
    mass=0.3,
    properties =[],
    description= "")

add_item("beer",
    name="beer",
    mass=0.2,
    properties = [],
    description= "")

add_item("cereal",
    name="cereal",
    mass=0.4,
    properties=[],
    description= "")

add_item("gear",
    name="protective gear",
    mass=2,
    properties = [],
    description="")

add_item("pan",
    name="a frying pan",
    mass=1,
    properties = [],
    description= "")

add_item("egg",
    name="an egg",
    mass=0.1,
    properties = [],
    description= "")

add_item("pork",
    name="porkchops",
    mass=0.2,
    properties = [],
    description= "")

add_item("skateboard",
    name="skateboard",
    mass=0.3,
    properties=[],
    description="")

add_item("whiskey",
    name="whiskey",
    mass=0.2,
    properties=[],
    description="")

add_item("coffee",
    name="coffee",
    mass=0.2,
    properties=[],
    description="")

add_item("wagon wheels",
    name="wagon wheels",
    mass=0.1,
    properties=[],
    description="The best biscuits ever made")

add_item("sock",
    name="a sock",
    mass=0.1,
    properties=[],
    description="Can't find the other one.")

add_item("butter",
    name="a block of butter",
    mass=0.1,
    properties=[],
    description="")

add_item("steering wheel",
    name="a steering wheel",
    mass=0.1,
    properties=[],
    description="")

add_item("trainers",
    name="light-up trainers",
    mass=0.1,
    properties=[],
    description="Used to distract your opponents")

add_item("laces",
    name="shoe laces",
    mass=0.1,
    properties=[],
    description="Can you tie your shoe laces, though?")

add_item("ring",
    name="gold ring",
    mass=0.1,
    properties=[],
    description="Someone took it off, but it won't make it that much easier")

add_item("gondola",
    name="a Venetian gondola",
    mass = 10,
    properties =[],
    description="How did this even get to London?")

add_item("cornetto",
    name="a cornetto",
    mass=0.1,
    properties=[],
    description="How's that for a slice of fried gold?")

add_item("hdmi",
    name="an HDMI cable",
    mass=0.1,
    properties=[],
    description="")

add_item("jar",
    name="a jar",
    mass=0.1,
    properties=[],
    description="")

add_item("racket",
    name="a tennis racket",
    mass=0.3,
    properties=[],
    description="")

add_item("lego yoda",
    name="a lego yoda",
    mass=0.2,
    properties=[],
    description="Rumour has it that he got banned for running people over with a 2001 Honda Civic")

add_item("keys",
    name="keys to a 2001 Honda Civic",
    mass=0.1,
    properties=[],
    description="It's got blood all over it.")

add_item("Honda Civic",
    name="a Honda Civic",
    mass = 30,
    properties=[],
    description="It's missing a steering wheel. I wonder where that went?")

add_item("Helicopter",
    name="a helicopter",
    mass = 100,
    properties=[],
    description="")

add_item("rubiks cube",
    name="a Rubik's cube",
    mass=0.1,
    properties=[],
    description="")

add_item("tissue box",
    name="an empty tissue box",
    mass=0.1,
    properties=[],
    description="")

add_item("tin foil",
    name="tin foil",
    mass=0.2,
    properties=[],
    description="")

add_item("gift card",
    name="a $10 roblox gift card",
    mass=0.1,
    properties=[],
    description="")

add_item("teapot",
    name="a teapot",
    mass=0.5,
    properties=[],
    description="")

add_item("lime",
    name="a lime",
    mass=0.1,
    properties=[],
    description="IT'S A LIME!")

add_item("fan",
    name="a broken fan",
    mass=0.5,
    properties=[],
    description="The cat broke it.")

add_item("weetabix",
    name="Weetabix",
    mass=0.2,
    properties=[],
    description="")

add_item("cornflakes",
    name="Corn Flakes",
    mass=0.2,
    properties=[],
    description="")

add_item("milk",
    name="expired milk",
    mass=0.1,
    properties=[],
    description="")
print(len(items))
