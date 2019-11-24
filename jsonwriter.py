'''
This file is just a quick utility I wrote to create json files from a python
dictionary. Not directly used in the map's operation, just here for convenience
'''

body = {"decks":{
    1.0:{
        "file":'floorplans/EAST_01.png',
        "deck_text":"Deck 1",
        "resize":[359, 800],
        "icons": [
            {"name": "Example 1-1",
             "coordinates": (300, 300),
             "info": "Example Text 1-1"},
            {"name": "Example 1-2",
             "coordinates": (400, 400),
             "info": "Example Text 1-2"}
            ]
        },
    2.0:{
        "file":'floorplans/EAST_02_WEST_02.png',
        "deck_text":"Deck 2",
        "resize":[481, 800],
        "icons": [
            {"name": "Example 2-1",
             "coordinates": (300, 300),
             "info": "Example Text 2-1"},
            {"name": "Example 2-2",
             "coordinates": (400, 400),
             "info": "Example Text 2-2"}
            ]
        },
    3.0:{
        "file":'floorplans/EAST_03.png',
        "deck_text":"Deck 3",
        "resize":[361, 800],
        "icons": [
            {"name": "Example 3-1",
             "coordinates": (300, 300),
             "info": "Example Text 3-1"},
            {"name": "Example 3-2",
             "coordinates": (400, 400),
             "info": "Example Text 3-2"}
            ]
        },
    3.5:{
        "file":'floorplans/WEST_3.5.png',
        "deck_text":"Deck 3.5",
        "resize":[364, 800],
        "icons": [
            {"name": "Example 3.5-1",
             "coordinates": (300, 300),
             "info": "Example Text 3.5-1"},
            {"name": "Example 3.5-2",
             "coordinates": (400, 400),
             "info": "Example Text 3.5-2"}
            ]
        },
    4.0:{
        "file":'floorplans/EAST_04.png',
        "deck_text":"Deck 4",
        "resize":[481, 800],
        "icons": [
            {"name": "Example 4-1",
             "coordinates": (300, 300),
             "info": "Example Text 4-1"},
            {"name": "Example 4-2",
             "coordinates": (400, 400),
             "info": "Example Text 4-2"}
            ]
        },
    5.0:{
        "file":'floorplans/EAST_05_West_05.png',
        "deck_text":"Deck 5",
        "resize":[338, 800],
        "icons": [
            {"name": "Example 5-1",
             "coordinates": (300, 300),
             "info": "Example Text 5-1"},
            {"name": "Example 5-2",
             "coordinates": (400, 400),
             "info": "Example Text 5-2"}
            ]
        },
    6.0:{
        "file":'floorplans/EAST_06.png',
        "deck_text":"Deck 6",
        "resize":[379, 800],
        "icons": [
            {"name": "Example 6-1",
             "coordinates": (300, 300),
             "info": "Example Text 6-1"},
            {"name": "Example 6-2",
             "coordinates": (400, 400),
             "info": "Example Text 6-2"}
            ]
        },
    7.0:{
        "file":'floorplans/EAST_07.png',
        "deck_text":"Deck 7",
        "resize":[376, 800],
        "icons": [
            {"name": "Example 7-1",
             "coordinates": (300, 300),
             "info": "Example Text 7-1"},
            {"name": "Example 7-2",
             "coordinates": (400, 400),
             "info": "Example Text 7-2"}
            ]
        },
    8.0:{
        "file":'floorplans/EAST_08.png',
        "deck_text":"Deck 8",
        "resize":[375, 800],
        "icons": [
            {"name": "Example 8-1",
             "coordinates": (300, 300),
             "info": "Example Text 8-1"},
            {"name": "Example 8-2",
             "coordinates": (400, 400),
             "info": "Example Text 8-2"}
            ]
        },
    9.0:{
        "file":'floorplans/EAST_09.png',
        "deck_text":"Deck 9",
        "resize":[378, 800],
        "icons": [
            {"name": "Example 9-1",
             "coordinates": (300, 300),
             "info": "Example Text 9-1"},
            {"name": "Example 9-2",
             "coordinates": (400, 400),
             "info": "Example Text 9-2"}
            ]
        },
    9.5:{
        "file":'floorplans/WEST_9.5.png',
        "deck_text":"Deck 9.5",
        "resize":[365, 800],
        "icons": [
            {"name": "Example 9.5-1",
             "coordinates": (300, 300),
             "info": "Example Text 9.5-1"},
            {"name": "Example 9.5-2",
             "coordinates": (400, 400),
             "info": "Example Text 9.5-2"}
            ]
        },
    -1.0:{
        "file":'floorplans/WEST_basement.png',
        "deck_text":"Basement",
        "resize":[364, 800],
        "icons": [
            {"name": "Example B-1",
             "coordinates": (300, 300),
             "info": "Example Text B-1"},
            {"name": "Example B-2",
             "coordinates": (400, 400),
             "info": "Example Text B-2"}
            ]}
        }
}

import json

with open("deckinfo.json", "w") as outfile:
    json.dump(body, outfile)
