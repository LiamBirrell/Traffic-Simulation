from Traffic_Generation import *
import numpy as np

CROSSROAD_TIMER = 45
CROSSROAD_REPEATS = sim_length/CROSSROAD_TIMER
T_JUNCTION_TIMER = 30
T_JUNCTION_REPEATS = sim_length/T_JUNCTION_TIMER
        
default_light_schedule = {}
for i in intersections:
    for j in intersections[i]["LANES"]:
        if intersections[i]["INTERSECTION_TYPE"] == "CROSSROAD":     
            if "NB" in j:
                default_light_schedule[i,j] = ([1]*CROSSROAD_TIMER+[0]*CROSSROAD_TIMER)*int(CROSSROAD_REPEATS/2)
            if "SB" in j:    
                default_light_schedule[i,j] = ([1]*CROSSROAD_TIMER+[0]*CROSSROAD_TIMER)*int(CROSSROAD_REPEATS/2)
            if "EB" in j:
                default_light_schedule[i,j] = ([0]*CROSSROAD_TIMER+[1]*CROSSROAD_TIMER)*int(CROSSROAD_REPEATS/2)
            if "WB" in j:    
                default_light_schedule[i,j] = ([0]*CROSSROAD_TIMER+[1]*CROSSROAD_TIMER)*int(CROSSROAD_REPEATS/2)
                
        if intersections[i]["INTERSECTION_TYPE"] == "T_JUNCTION":
            if "NB" in j:
                default_light_schedule[i,j] = ([1]*T_JUNCTION_TIMER+[0]*T_JUNCTION_TIMER*2)*int(T_JUNCTION_REPEATS/3)
            if "EB" in j:
                default_light_schedule[i,j] = ([0]*T_JUNCTION_TIMER*2+[1]*T_JUNCTION_TIMER)*int(T_JUNCTION_REPEATS/3)
            if "WB" in j:    
                default_light_schedule[i,j] = ([0]*(T_JUNCTION_TIMER)\
                                              +[1]*(T_JUNCTION_TIMER)\
                                              +[0]*(T_JUNCTION_TIMER))\
                                              *int((T_JUNCTION_REPEATS)/3)    

def get_neighbour(lane):
    if "NB_LANE_1" in lane[1]:
        for i in range(len(list(connections.keys()))):
            if lane[0] in list(connections.keys())[i]:
                if "NB_LANE_2" in list(connections.keys())[i][1]:
                    return list(connections.keys())[i]
                    
    if "SB_LANE_1" in lane[1]:
        for i in range(len(list(connections.keys()))):
            if lane[0] in list(connections.keys())[i]:
                if "SB_LANE_2" in list(connections.keys())[i][1]:
                    return list(connections.keys())[i]
                              
    if "NB_LANE_2" in lane[1]:
        for i in range(len(list(connections.keys()))):
            if lane[0] in list(connections.keys())[i]:
                if "NB_LANE_1" in list(connections.keys())[i][1]:
                    return list(connections.keys())[i]
                    
    if "SB_LANE_2" in lane[1]:
        for i in range(len(list(connections.keys()))):
            if lane[0] in list(connections.keys())[i]:
                if "SB_LANE_1" in list(connections.keys())[i][1]:
                    return list(connections.keys())[i]

def path_find(i,j,path):
    if j in list(connections[i]):
        return path + [j]
    for k in range(len(connections[(i)])):
        if "EXT" not in list(connections[(i)])[k]:
            next_lane = connections[i][k]
            result = path_find(next_lane,j,path+[next_lane])
            if not result:  
                for k in range(len(connections[(i)])):
                    if "EXT" not in list(connections[(i)])[k]:
                        next_lane = connections[i][k]
                        next_next_lane = get_neighbour(next_lane)
                        result = path_find(next_next_lane,j,path+[next_lane]+[next_next_lane])   
            if result:
                return result  

routes = {(i,j): path_find(i,j,[])
          for i in exit_lane_weights for j in list(exit_lane_weights[i].keys())}



        