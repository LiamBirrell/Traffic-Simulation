intersections = {
    "INT1":{"INTERSECTION_TYPE": "CROSSROAD",
            "LANES": {"NB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*50},
                      "NB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*50},
                      "EB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*50},         
                      "EB_LANE_2":{"COLOUR": "RED", "CELLS": [0]*50},
                      "WB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*50},
                      "WB_LANE_2":{"COLOUR": "RED", "CELLS": [0]*50},  
                      "SB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*50},
                      "SB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*50}
                      }
            },
    
    "INT2":{"INTERSECTION_TYPE": "CROSSROAD",
            "LANES": {"NB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "NB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*150},  
                      "SB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "SB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "EB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*25},
                      "WB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*25}
                      }
            },  
    
    "INT3":{"INTERSECTION_TYPE": "CROSSROAD",
            "LANES": {"NB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "NB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "SB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*50},
                      "SB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*50},
                      "EB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*25},  
                      "WB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*25}
                      }
            },  
    "INT4":{"INTERSECTION_TYPE": "T_JUNCTION",
            "LANES": {"NB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "NB_LANE_2":{"COLOUR": "GREEN", "CELLS": [0]*150},
                      "EB_LANE_1":{"COLOUR": "RED", "CELLS": [0]*50},        
                      "EB_LANE_2":{"COLOUR": "RED", "CELLS": [0]*50},
                      "WB_LANE_1":{"COLOUR": "GREEN", "CELLS": [0]*50},
                      "WB_LANE_2":{"COLOUR": "RED", "CELLS": [0]*50}
                      }
            }    
    }


entry_lane_weights = {
    ("INT1","NB_LANE_1"): 0.1,
    ("INT1","NB_LANE_2"): 0.4, 
    ("INT1","EB_LANE_1"): 0.125,
    ("INT1","EB_LANE_2"): 0.0125,
    ("INT1","WB_LANE_1"): 0.0125,
    ("INT1","WB_LANE_2"): 0.0125,
     
    ("INT2","EB_LANE_1"): 0.00625,
    ("INT2","WB_LANE_1"): 0.00625, 
    
    ("INT3","EB_LANE_1"): 0.0125,
    ("INT3","WB_LANE_1"): 0.0125,
    
    ("INT4","EB_LANE_1"): 0.025,     
    ("INT4","EB_LANE_2"): 0.025,
    ("INT4","WB_LANE_1"): 0.2,
    ("INT4","WB_LANE_2"): 0.05
    }


exit_lane_weights = {
    ("INT1","NB_LANE_1"):{"INT1_WB_LANE_1_EXT": 0.025,
                        "INT2_WB_LANE_1_EXT": 0.025,
                        "INT3_WB_LANE_1_EXT": 0.05,
                        "INT4_WB_LANE_1_EXT": 0.45,
                        "INT4_EB_LANE_2_EXT": 0.45,
                        },
    ("INT1","NB_LANE_2"):{"INT4_WB_LANE_1_EXT": 0.5,
                        "INT4_EB_LANE_2_EXT": 0.5,
                                },
    ("INT1","EB_LANE_1"):{"INT1_EB_LANE_1_EXT": 0.05,
                        "INT2_WB_LANE_1_EXT": 0.075,
                        "INT3_WB_LANE_1_EXT": 0.075,
                        "INT4_WB_LANE_1_EXT": 0.4,
                        "INT4_EB_LANE_2_EXT": 0.4,
                        },
    ("INT1","EB_LANE_2"):{"INT1_EB_LANE_2_EXT": 1,
                                 },
    ("INT1","WB_LANE_1"):{"INT1_WB_LANE_1_EXT": 0.8,
                        "INT1_SB_LANE_1_EXT": 0.2,
                        },
    ("INT1","WB_LANE_2"):{"INT1_WB_LANE_2_EXT": 1,
                        },  
    
    ("INT2","EB_LANE_1"):{"INT2_EB_LANE_1_EXT": 0.1,
                        "INT3_WB_LANE_1_EXT": 0.1,
                        "INT4_WB_LANE_1_EXT": 0.4,
                        "INT4_EB_LANE_2_EXT": 0.4,
                        },
    ("INT2","WB_LANE_1"):{"INT2_WB_LANE_1_EXT": 0.1,
                        "INT1_EB_LANE_1_EXT": 0.1, 
                        "INT1_SB_LANE_1_EXT": 0.4,
                        "INT1_SB_LANE_2_EXT": 0.4,
                        },   
    ("INT3","EB_LANE_1"):{"INT3_EB_LANE_1_EXT": 0.1,
                        "INT4_WB_LANE_1_EXT": 0.45,
                        "INT4_EB_LANE_2_EXT": 0.45,
                        },
    ("INT3","WB_LANE_1"):{"INT2_WB_LANE_1_EXT": 0.05,
                        "INT1_EB_LANE_1_EXT": 0.05, 
                        "INT1_SB_LANE_1_EXT": 0.45,
                        "INT1_SB_LANE_2_EXT": 0.45,
                        },   
    
    ("INT4","EB_LANE_1"):{"INT4_EB_LANE_2_EXT": 1
                         },
    ("INT4","EB_LANE_2"):{"INT4_EB_LANE_2_EXT": 0.2,
                        "INT3_EB_LANE_1_EXT": 0.1,
                        "INT2_EB_LANE_1_EXT": 0.1,
                        "INT1_EB_LANE_1_EXT": 0.2,
                        "INT1_SB_LANE_1_EXT": 0.2,
                        "INT1_SB_LANE_2_EXT": 0.2,
                        },
    ("INT4","WB_LANE_1"):{"INT4_WB_LANE_1_EXT": 0.2,
                        "INT3_EB_LANE_1_EXT": 0.1,
                        "INT2_EB_LANE_1_EXT": 0.1,
                        "INT1_EB_LANE_1_EXT": 0.2,
                        "INT1_SB_LANE_1_EXT": 0.2,
                        "INT1_SB_LANE_2_EXT": 0.2,
                        },   
    ("INT4","WB_LANE_2"):{"INT4_WB_LANE_2_EXT": 1
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