intersections = {
    "INT1":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},
            
            "SB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},
            "SB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},         
            "EB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},
            
            "WB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},
            "WB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},          
            
            "CURRENT PHASE":"MAIN ROAD"
            },
    "INT2":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},
            
            "SB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},
            "SB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25},
            "WB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25},      
            
            "CURRENT PHASE":"MAIN ROAD"
            },  
    "INT3":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},
            
            "SB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},
            "SB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25},  
            "WB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*25}, 
            
            "CURRENT PHASE":"MAIN ROAD"
            },  
    "INT4":{"NB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},
            "NB_LANE_2":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*150},

            "EB_LANE_1":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},        
            "EB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},
            
            "WB_LANE_1":{"COLOUR": "GREEN", "TIMER": 40, "CELLS": [0]*50},
            "WB_LANE_2":{"COLOUR": "RED", "TIMER": 0, "CELLS": [0]*50},
            
            "CURRENT PHASE":"MAIN ROAD"
            }    
    }

entry_prob = {
    "INT1":{"NB_LANE_1":{"ARRIVAL_WEIGHT": 0.15},
            "NB_LANE_2":{"ARRIVAL_WEIGHT": 0.5}, 
            "EB_LANE_1":{"ARRIVAL_WEIGHT": 0.125},
            "EB_LANE_2":{"ARRIVAL_WEIGHT": 0.0125},
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.0125},
            "WB_LANE_2":{"ARRIVAL_WEIGHT": 0.025},
            },
    
    "INT2":{"EB_LANE_1":{"ARRIVAL_WEIGHT": 0.0125},
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.025},
            }, 
    
    "INT3":{"EB_LANE_1":{"ARRIVAL_WEIGHT": 0.025},
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.0125},     
            }, 
    
    "INT4":{"EB_LANE_1":{"ARRIVAL_WEIGHT": 0.025},     
            "EB_LANE_2":{"ARRIVAL_WEIGHT": 0.025},
            "WB_LANE_1":{"ARRIVAL_WEIGHT": 0.25},
            "WB_LANE_2":{"ARRIVAL_WEIGHT": 0.05},
            }    
    }

exit_prob = {
    "INT1":{"NB_LANE_1":{"INT1_WB_LANE_1_EXT": 0.15,
                        "INT2_WB_LANE_1_EXT": 0,
                        "INT3_WB_LANE_1_EXT": 0,
                        "INT4_WB_LANE_1_EXT": 0,
                        "INT4_EB_LANE_2_EXT": 0,
                        },
            "NB_LANE_2":{"INT4_WB_LANE_1_EXT": 0,
                        "INT4_EB_LANE_2_EXT": 0,
                                },
            "EB_LANE_1":{"INT1_EB_LANE_1_EXT": 0.15,
                        "INT2_WB_LANE_1_EXT": 0,
                        "INT3_WB_LANE_1_EXT": 0,
                        "INT4_WB_LANE_1_EXT": 0,
                        "INT4_EB_LANE_2_EXT": 0,
                        },
            "EB_LANE_2":{"INT1_EB_LANE_2_EXT": 0,
                                 },
            "WB_LANE_1":{"INT1_WB_LANE_1_EXT": 0.15,
                        "INT1_SB_LANE_1_EXT": 0,
                        },
            "WB_LANE_2":{"INT1_WB_LANE_2_EXT": 0,
                                 },     
            },
    
    "INT2":{"EB_LANE_1":{"INT2_EB_LANE_1_EXT": 0,
                        "INT3_WB_LANE_1_EXT": 0,
                        "INT4_WB_LANE_1_EXT": 0,
                        "INT4_EB_LANE_2_EXT": 0,
                        },
            "WB_LANE_1":{"INT2_WB_LANE_1_EXT": 0.15,
                        "INT1_SB_LANE_1_EXT": 0,
                        "INT1_SB_LANE_2_EXT": 0,
                        "INT1_EB_LANE_1_EXT": 0.15,
                        },   
            },  
    "INT3":{"EB_LANE_1":{"INT3_EB_LANE_1_EXT": 0,
                        "INT4_WB_LANE_1_EXT": 0,
                        "INT4_EB_LANE_2_EXT": 0,
                        },
            "WB_LANE_1":{"INT2_WB_LANE_1_EXT": 0.15,
                        "INT1_SB_LANE_1_EXT": 0,
                        "INT1_SB_LANE_2_EXT": 0,
                        "INT1_EB_LANE_1_EXT": 0.15,
                        },   
            },
    "INT4":{"EB_LANE_1":{"INT4_EB_LANE_2_EXT": 0,
                        },
            "EB_LANE_2":{"INT4_EB_LANE_2_EXT": 0,
                        "INT3_EB_LANE_1_EXT": 0,
                        "INT2_EB_LANE_1_EXT": 0,
                        "INT1_EB_LANE_1_EXT": 0.15,
                        "INT1_SB_LANE_1_EXT": 0,
                        "INT1_SB_LANE_2_EXT": 0,
                        },
            "WB_LANE_1":{"INT4_WB_LANE_1_EXT": 0,
                        "INT3_EB_LANE_1_EXT": 0,
                        "INT2_EB_LANE_1_EXT": 0,
                        "INT1_EB_LANE_1_EXT": 0.15,
                        "INT1_SB_LANE_1_EXT": 0,
                        "INT1_SB_LANE_2_EXT": 0,
                        },   
            "WB_LANE_2":{"INT4_WB_LANE_2_EXT": 0
                        },  
            },
    }


connections = {
    # Intersection 1:
    # Northbound
    ("INT1", "NB_LANE_1"):[("INT2", "NB_LANE_1"), "INT1_WB_LANE_1_EXT"],
    ("INT1", "NB_LANE_2"):("INT2", "NB_LANE_2"), 
    # Southbound
    ("INT1", "SB_LANE_1"):[("INT1", "SB_LANE_1_EXT"), "INT1_EB_LANE_1_EXT"],
    ("INT1", "SB_LANE_2"):"INT1_SB_LANE_2_EXT",  
    # Eastbound
    ("INT1", "EB_LANE_1"):[("INT2", "NB_LANE_1"), "INT1_EB_LANE_1_EXT"],
    ("INT1", "EB_LANE_2"):"INT1_EB_LANE_2_EXT",
    # Westbound
    ("INT1", "WB_LANE_1"):[("INT1_SB_LANE_1_EXT"), "INT1_WB_LANE_1_EXT"],    
    ("INT1", "WB_LANE_2"):"INT1_WB_LANE_2_EXT", 
    
    # Intersection 2:
    # Northbound
    ("INT2", "NB_LANE_1"):[("INT3", "NB_LANE_1"), "INT2_WB_LANE_1_EXT"],
    ("INT2", "NB_LANE_2"):("INT3", "NB_LANE_2"),
    # Southbound
    ("INT2", "SB_LANE_1"):[("INT1", "SB_LANE_1"), "INT2_EB_LANE_1_EXT"],
    ("INT2", "SB_LANE_2"):("INT1", "SB_LANE_2"),    
    # Eastbound
    ("INT2", "EB_LANE_1"):[("INT3", "NB_LANE_1"), "INT2_EB_LANE_1_EXT"],
    # Westbound       
    ("INT2", "WB_LANE_1"):[("INT1", "SB_LANE_1"), "INT2_WB_LANE_1_EXT"],    
        
    # Intersection 3:
    # Northbound
    ("INT3", "NB_LANE_1"):[("INT4", "NB_LANE_1"), "INT3_WB_LANE_1_EXT"],
    ("INT3", "NB_LANE_2"):("INT4", "NB_LANE_2"),
    # Southbound
    ("INT3", "SB_LANE_1"):[("INT2", "SB_LANE_1"), "INT3_EB_LANE_1_EXT"],  
    ("INT3", "SB_LANE_2"):("INT2", "SB_LANE_2"),    
    # Eastbound
    ("INT3", "EB_LANE_1"):[("INT4", "NB_LANE_1"), "INT3_EB_LANE_1_EXT"],    
    # Westbound           
    ("INT3", "WB_LANE_1"):[("INT2", "SB_LANE_1"), "INT3_WB_LANE_1_EXT"],        
        
    # Intersection 4:
    # Northbound
    ("INT4", "NB_LANE_1"):"INT4_WB_LANE_1_EXT",
    ("INT4", "NB_LANE_2"):"INT4_EB_LANE_2_EXT",    
    # Southbound
        # is INT3_SB Lanes
    # Eastbound
    ("INT4", "EB_LANE_2"):[("INT3", "SB_LANE_2"), "INT4_EB_LANE_2_EXT"],
    ("INT4", "EB_LANE_1"):"INT4_EB_LANE_1_EXT",    
    # Westbound       
    ("INT4", "WB_LANE_1"):[("INT3", "SB_LANE_1"), "INT4_WB_LANE_1_EXT"],
    ("INT4", "WB_LANE_2"):"INT4_WB_LANE_2_EXT",    
    }
    




