intersections = {
    "INT1":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 1 Northbound - Left turn and striaght ahead
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 2 Northbound - Straight Ahead
            
            "SB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 1 Southbound - Left turn and striaght ahead
            "SB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 2 Southbound - Straight Ahead

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 1 Eastbound - Left turn and striaght ahead            
            "EB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 2 Eastbound - Striaght ahead     
            
            "WB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 1 Westbound - Left turn and striaght ahead
            "WB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 2 Westbound - Striaght ahead            
            
            "CURRENT PHASE":"MAIN ROAD"
            },
    "INT2":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 1 Northbound - Left turn and striaght ahead
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 2 Northbound - Straight Ahead
            
            "SB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 1 Southbound - Left turn and striaght ahead
            "SB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 2 Southbound - Straight Ahead

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25}, # Lane 1 Eastbound - Left turn and striaght ahead   
            "WB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25}, # Lane 1 Westbound - Left turn and striaght ahead         
            
            "CURRENT PHASE":"MAIN ROAD"
            },  
    "INT3":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 1 Northbound - Left turn and striaght ahead
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 2 Northbound - Straight Ahead
            
            "SB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 1 Southbound - Left turn and striaght ahead
            "SB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 2 Southbound - Straight Ahead

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25}, # Lane 1 Eastbound - Left turn and striaght ahead   
            "WB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25}, # Lane 1 Westbound - Left turn and striaght ahead       
            
            "CURRENT PHASE":"MAIN ROAD"
            },  
    "INT4":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 1 Northbound - Left turn
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150}, # Lane 2 Northbound - Right turn

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 1 Eastbound - Striaght ahead            
            "EB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 2 Eastbound - Right turn
            
            "WB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50}, # Lane 1 Westbound - Left turn
            "WB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50}, # Lane 2 Westbound - Straight ahead
            
            "CURRENT PHASE":"MAIN ROAD"
            }    
    }

traffic_demand = {
    "INT1":{"NB_LANE_1":{"ARRIVAL_WEIGHT": 0.15}, # Lane 1 Northbound - Left turn and striaght ahead
            "NB_LANE_2":{"ARRIVAL_WEIGHT": 0.5}, # Lane 2 Northbound - Straight Ahead
            
            "SB_LANE_1":{"ARRIVAL_WEIGHT": 0}, # Lane 1 Southbound - Left turn and striaght ahead
            "SB_LANE_2":{"ARRIVAL_WEIGHT": 0}, # Lane 2 Southbound - Straight Ahead

            "EB_LANE_1":{"ARRIVAL_WEIGHT": 0.125}, # Lane 1 Eastbound - Left turn and striaght ahead            
            "EB_LANE_2":{"ARRIVAL_WEIGHT": 0.0125}, # Lane 2 Eastbound - Striaght ahead     
            
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.0125}, # Lane 1 Westbound - Left turn and striaght ahead
            "WB_LANE_2":{"ARRIVAL_WEIGHT": 0.025}, # Lane 2 Westbound - Striaght ahead       
            },
    
    "INT2":{"NB_LANE_1":{"ARRIVAL_WEIGHT": 0}, # Lane 1 Northbound - Left turn and striaght ahead
            "NB_LANE_2":{"ARRIVAL_WEIGHT": 0}, # Lane 2 Northbound - Straight Ahead
            
            "SB_LANE_1":{"ARRIVAL_WEIGHT": 0}, # Lane 1 Southbound - Left turn and striaght ahead
            "SB_LANE_2":{"ARRIVAL_WEIGHT": 0}, # Lane 2 Southbound - Straight Ahead

            "EB_LANE_1":{"ARRIVAL_WEIGHT": 0.0125}, # Lane 1 Eastbound - Left turn and striaght ahead   
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.025}, # Lane 1 Westbound - Left turn and striaght ahead     
            }, 
    
    "INT3":{"NB_LANE_1":{"ARRIVAL_WEIGHT": 0}, # Lane 1 Northbound - Left turn and striaght ahead
            "NB_LANE_2":{"ARRIVAL_WEIGHT": 0}, # Lane 2 Northbound - Straight Ahead
            
            "SB_LANE_1":{"ARRIVAL_WEIGHT": 0}, # Lane 1 Southbound - Left turn and striaght ahead
            "SB_LANE_2":{"ARRIVAL_WEIGHT": 0}, # Lane 2 Southbound - Straight Ahead

            "EB_LANE_1":{"ARRIVAL_WEIGHT": 0.025}, # Lane 1 Eastbound - Left turn and striaght ahead   
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.0125}, # Lane 1 Westbound - Left turn and striaght ahead       
            }, 
    
    "INT4":{"NB_LANE_1":{"ARRIVAL_WEIGHT": 0}, # Lane 1 Northbound - Left turn
            "NB_LANE_2":{"ARRIVAL_WEIGHT": 0}, # Lane 2 Northbound - Right turn

            "EB_LANE_1":{"ARRIVAL_WEIGHT": 0.025}, # Lane 1 Eastbound - Striaght ahead            
            "EB_LANE_2":{"ARRIVAL_WEIGHT": 0.025}, # Lane 2 Eastbound - Right turn
            
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.25}, # Lane 1 Westbound - Left turn
            "WB_LANE_2":{"ARRIVAL_WEIGHT": 0.05}, # Lane 2 Westbound - Straight ahead
            }    
    }

connections = {
    # Northbound connections
    ("INT1", "NB_LANE_1"):("INT2", "NB_LANE_1"),
    ("INT1", "NB_LANE_2"):("INT2", "NB_LANE_2"),
    ("INT2", "NB_LANE_1"):("INT3", "NB_LANE_1"),
    ("INT2", "NB_LANE_2"):("INT3", "NB_LANE_2"),
    ("INT3", "NB_LANE_1"):("INT4", "NB_LANE_1"),
    ("INT3", "NB_LANE_2"):("INT4", "NB_LANE_2"),
    
    # Southbound connections
    ("INT4", "SB_LANE_1"):("INT3", "SB_LANE_1"),
    ("INT4", "SB_LANE_2"):("INT3", "SB_LANE_2"),
    ("INT3", "SB_LANE_1"):("INT2", "SB_LANE_1"),
    ("INT3", "SB_LANE_2"):("INT2", "SB_LANE_2"),  
    ("INT2", "SB_LANE_1"):("INT1", "SB_LANE_1"),
    ("INT2", "SB_LANE_2"):("INT1", "SB_LANE_2"),  
    
    # Eastbound connections
    ("INT4", "EB_LANE_2"):("INT4", "SB_LANE_2"),
    ("INT1", "EB_LANE_1"):[("INT2", "NB_LANE_1"), ("INT2", "NB_LANE_2")],
    ("INT2", "EB_LANE_1"):[("INT3", "NB_LANE_1"), ("INT3", "NB_LANE_2")],
    ("INT3", "EB_LANE_1"):[("INT4", "NB_LANE_1"), ("INT4", "NB_LANE_2")],
    
    # Westbound connections
    ("INT4", "WB_LANE_1"):("INT3", "SB_LANE_1"),
    ("INT3", "WB_LANE_1"):[("INT2", "SB_LANE_1"), ("INT2", "SB_LANE_2")],
    ("INT2", "WB_LANE_1"):[("INT1", "SB_LANE_1"), ("INT1", "SB_LANE_2")],
    ("INT1", "WB_LANE_1"): [("INT2", "NB_LANE_1"), ("INT2", "NB_LANE_2")]
    }


















