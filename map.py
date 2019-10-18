from items import *

rooms = {}

def add_room(id, name, description, connected_places, items):
    items[id] = {"name":name, "description":description, "connected_places":connected_places, "items":items}

add_room("coach",

        name="Coach outside cardiff uni"

        description = """You are in a run-down, dusty bus that looks like it could break down
        at any moment. The drive is staring down at you with beady eyes awaiting you ticket. You're estatic to arrive at London to meet
        our childhood friend, Alex.""",

        connected_places = {victoria_coach_station:120},

        items = ["wagon wheels", "tape"]

        )
