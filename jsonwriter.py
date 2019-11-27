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
            {"name": "Example B-1",
             "coordinates": (300, 300),
             "info": "Example Text B-1"},
            {"name": "Example B-2",
             "coordinates": (400, 400),
             "info": "Example Text B-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "1 East":{
        "file":'floorplans/east1.png',
        "deck_text":"Deck 1 East",
        "resize":[381, 600],
        "icons": [
            {"name": "Example E1-1",
             "coordinates": (300, 300),
             "info": "Example Text E1-1"},
            {"name": "Example E1-2",
             "coordinates": (100, 400),
             "info": "Example Text E1-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "2 East":{
        "file":'floorplans/east2.png',
        "deck_text":"Deck 2 East",
        "resize":[510, 600],
        "icons": [
            {"name": "Example E2-1",
             "coordinates": (300, 300),
             "info": "Example Text E2-1"},
            {"name": "Example E2-2",
             "coordinates": (400, 400),
             "info": "Example Text E2-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "2 West":{
        "file":'floorplans/west2.png',
        "deck_text":"Deck 2 West",
        "resize":[463, 300],
        "icons": [
            {"name": "Example W2-1",
             "coordinates": (300, 300),
             "info": "Example Text W2-1"},
            {"name": "Example W2-2",
             "coordinates": (400, 400),
             "info": "Example Text W2-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "3 East":{
        "file":'floorplans/east3.png',
        "deck_text":"Deck 3 East",
        "resize":[379, 600],
        "icons": [
            {"name": "Example E3-1",
             "coordinates": (300, 300),
             "info": "Example Text E3-1"},
            {"name": "Example E3-2",
             "coordinates": (400, 400),
             "info": "Example Text E3-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "3.5 West":{
        "file":'floorplans/west3-5.png',
        "deck_text":"Deck 3.5 West",
        "resize":[472, 300],
        "icons": [
            {"name": "Example W3.5-1",
             "coordinates": (300, 300),
             "info": "Example Text W3.5-1"},
            {"name": "Example W3.5-2",
             "coordinates": (400, 400),
             "info": "Example Text W3.5-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "4 East":{
        "file":'floorplans/east4.png',
        "deck_text":"Deck 4 East",
        "resize":[505, 600],
        "icons": [
            {"name": "Example E4-1",
             "coordinates": (300, 300),
             "info": "Example Text E4-1"},
            {"name": "Example E4-2",
             "coordinates": (400, 400),
             "info": "Example Text E4-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "5 East":{
        "file":'floorplans/east5.png',
        "deck_text":"Deck 5 East",
        "resize":[348, 600],
        "icons": [
            {"name": "Example E5-1",
             "coordinates": (300, 300),
             "info": "Example Text E5-1"},
            {"name": "Example E5-2",
             "coordinates": (400, 400),
             "info": "Example Text E5-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "5 West":{
        "file":'floorplans/west5.png',
        "deck_text":"Deck 5 West",
        "resize":[472, 300],
        "icons": [
            {"name": "Example W5-1",
             "coordinates": (300, 300),
             "info": "Example Text W5-1"},
            {"name": "Example W5-2",
             "coordinates": (400, 400),
             "info": "Example Text W5-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "6 East":{
        "file":'floorplans/east6.png',
        "deck_text":"Deck 6 East",
        "resize":[406, 600],
        "icons": [
            {"name": "Example E6-1",
             "coordinates": (300, 300),
             "info": "Example Text E6-1"},
            {"name": "Example E6-2",
             "coordinates": (400, 400),
             "info": "Example Text E6-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "7 East":{
        "file":'floorplans/east7.png',
        "deck_text":"Deck 7 East",
        "resize":[402, 600],
        "icons": [
            {"name": "Example E7-1",
             "coordinates": (300, 300),
             "info": "Example Text E7-1"},
            {"name": "Example E7-2",
             "coordinates": (400, 400),
             "info": "Example Text E7-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "8 East":{
        "file":'floorplans/east8.png',
        "deck_text":"Deck 8 East",
        "resize":[402, 600],
        "icons": [
            {"name": "Example E8-1",
             "coordinates": (300, 300),
             "info": "Example Text E8-1"},
            {"name": "Example E8-2",
             "coordinates": (400, 400),
             "info": "Example Text E8-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "9 East":{
        "file":'floorplans/east9.png',
        "deck_text":"Deck 9 East",
        "resize":[404, 600],
        "icons": [
            {"name": "Example E9-1",
             "coordinates": (300, 300),
             "info": "Example Text E9-1"},
            {"name": "Example E9-2",
             "coordinates": (400, 400),
             "info": "Example Text E9-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]
        },
    "9.5 West":{
        "file":'floorplans/west9-5.png',
        "deck_text":"Deck 9.5 West",
        "resize":[464, 300],
        "icons": [
            {"name": "Example W9.5-1",
             "coordinates": (300, 300),
             "info": "Example Text W9.5-1"},
            {"name": "Example W9.5-2",
             "coordinates": (400, 400),
             "info": "Example Text W9.5-2"}
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
            {"coordinates": (450, 450),
             "target": "1 East"}
            ]}
        }
}

import json

with open("deckinfo.json", "w") as outfile:
    json.dump(body, outfile)
