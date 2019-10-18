from items import *

location_bus = {
    "name": "An idle bus outside the student union",

    "description":
    """ """,

    "connected_places": {"Victoria_Coach_Station": 120},

    "items": [item_tape],

    ""
}

location_coach_station = {
    "name": "Victoria Coach Station",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"north": "Reception"},

    "items": []
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": []
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": []
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "items": [item_pen]
}

room_lecture = {
    "name": "the lecture hall",

    "description":
    """You are now at the lecture hall, Kirill Sidorov is having a chat
    with the technician to fix the audio issues. You grab a seat and listen
    to the lecture.""",

    "exits":{"south":"Reception"},

    "items": []

 }


rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office,
    "Lecture Hall": room_lecture
}
