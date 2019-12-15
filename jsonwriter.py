'''
This file is just a quick utility I wrote to create json files from a python
dictionary. Not directly used in the map's operation, just here for convenience
'''

body = {"decks":{
    "Basement West":{
        "file":'floorplans/westb.png',
        "deck_text":"Basement West",
        "resize":[472, 300],
        "icons": [
            {"name": "Microfiche Room",
             "coordinates": (261, 285),
             "info": "Not visible on this map, the East side of the basement level contains the school's microfiche collection."}
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (236, 285),
             "info": "Emergency exit, also leads to microfiche room."}
            ]
        },
    "1 East":{
        "file":'floorplans/east1.png',
        "deck_text":"Deck 1 East",
        "resize":[381, 600],
        "icons": [
            {"name": "Old Carrel Rules",
             "coordinates": (15, 225),
             "info": "An old sheet of rules for using research carrels, in the remains of a decomissioned carrel space. Suggests that carrels used to be much more popular, used by 2-4 people at a time."},
            {"name": "Dumbwaiter",
             "coordinates": (175, 550),
             "info": "Remains of the main stacks dumbwaiter system."}
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "2 East":{
        "file":'floorplans/east2.png',
        "deck_text":"Deck 2 East",
        "resize":[510, 600],
        "icons": [
            {"name": "Dumbwaiter",
             "coordinates": (305, 550),
             "info": "Remains of the main stacks dumbwaiter system."}
             ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ],
        "eastwest": [
            {"coordinates": (315, 15),
             "target": "2 West"}
            ]
        },
    "2 West":{
        "file":'floorplans/west2.png',
        "deck_text":"Deck 2 West",
        "resize":[463, 300],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ],
        "eastwest": [
            {"coordinates": (232, 280),
             "target": "2 East"}
            ]
        },
    "3 East":{
        "file":'floorplans/east3.png',
        "deck_text":"Deck 3 East",
        "resize":[379, 600],
        "icons": [
            {"name": "Dumbwaiter",
             "coordinates": (168, 545),
             "info": "Remains of the main stacks dumbwaiter system."}
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "3.5 West":{
        "file":'floorplans/west3-5.png',
        "deck_text":"Deck 3.5 West",
        "resize":[472, 300],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "4 East":{
        "file":'floorplans/east4.png',
        "deck_text":"Deck 4 East",
        "resize":[505, 600],
        "icons": [
            {"name": "Pneumatic Tubes",
             "coordinates": (300, 335),
             "info": "The main library once used an intricate system of pneumatic tubes to transfer documents and allow communication between units. The system is no longer used, but part of its infrastructure remains here."},
            {"name": "Dumbwaiter",
             "coordinates": (295, 540),
             "info": "Remains of the main stacks dumbwaiter system."},
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "5 East":{
        "file":'floorplans/east5.png',
        "deck_text":"Deck 5 East",
        "resize":[348, 600],
        "icons": [
            {"name": "Bookstacks Office",
             "coordinates": (45, 60),
             "info": "This is the office which directly maintains the organization of the main stacks collection."},
            {"name": "Body Outline",
             "coordinates": (174, 535),
             "info": "A faint outline left behind by some grisly halloween decorations. As it turns out, tape damages fresh floor wax."},
            {"name": "Reference Collection",
             "coordinates": (247, 400),
             "info": "The lower right quadrant of 5 East contains the main stacks' reference collection, maintained by RIS."},
            {"name": "Dumbwaiter",
             "coordinates": (157, 500),
             "info": "Remains of the main stacks dumbwaiter system."},
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ],
        "eastwest": [
            {"coordinates": (179, 15),
             "target": "5 West"}
            ]
        },
    "5 West":{
        "file":'floorplans/west5.png',
        "deck_text":"Deck 5 West",
        "resize":[472, 300],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ],
        "eastwest": [
            {"coordinates": (236, 285),
             "target": "5 East"}
            ]
        },
    "6 East":{
        "file":'floorplans/east6.png',
        "deck_text":"Deck 6 East",
        "resize":[406, 600],
        "icons": [
            {"name": "Dumbwaiter",
             "coordinates": (180, 580),
             "info": "Remains of the main stacks dumbwaiter system."}
             ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "7 East":{
        "file":'floorplans/east7.png',
        "deck_text":"Deck 7 East",
        "resize":[402, 600],
        "icons": [
            {"name": "Sealed Doorway",
             "coordinates": (30, 18),
             "info": "When the western section of the stacks was built, the old outer wall of the east stacks had to be converted to an inner wall. Here is one artifact of that conversion, a bricked-up doorway never painted over."},
            {"name": "Dumbwaiter",
             "coordinates": (175, 577),
             "info": "Remains of the main stacks dumbwaiter system."},
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "8 East":{
        "file":'floorplans/east8.png',
        "deck_text":"Deck 8 East",
        "resize":[402, 600],
        "icons": [
            {"name": "Dumbwaiter",
             "coordinates": (175, 577),
             "info": "Remains of the main stacks dumbwaiter system."}
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "9 East":{
        "file":'floorplans/east9.png',
        "deck_text":"Deck 9 East",
        "resize":[404, 600],
        "icons": [
            {"name": "Dumbwaiter",
             "coordinates": (175, 577),
             "info": "Remains of the main stacks dumbwaiter system."}
            ],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]
        },
    "9.5 West":{
        "file":'floorplans/west9-5.png',
        "deck_text":"Deck 9.5 West",
        "resize":[464, 300],
        "exits": [
            {"name": "Emergency Exit",
             "coordinates": (150, 150),
             "info": "Emergency Exit 1"},
            {"name": "Emergency Exit",
             "coordinates": (100, 100),
             "info": "Emergency Exit 2"}
            ]}
        }
}

import json

with open("deckinfo.json", "w") as outfile:
    json.dump(body, outfile)
