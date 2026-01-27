from Traffic_Generation import *
import numpy as np
import time

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
          
def simulation(light_sequence, vehicles, routes, neighbour_map):
    start_time = time.perf_counter()
    car_counter = 0
    cars_exited = 0
    cars_merged = 0
    vehicle_route = {}
    for t in range(sim_length):
        print(f"Timetep = {t}")
        # Check how many cars are on the road at each timestep
        cars_on_road = len(vehicle_route) - cars_exited
        print(f"Timestep = {t} | Cars on road: {cars_on_road}")
        
        # Traffic Light change logic
        for i in intersections:
            for j in intersections[i]["LANES"]:
                if light_sequence[(i,j)][t] == 1:
                    intersections[i]["LANES"][j]["COLOUR"] = "GREEN"  
                else:
                    intersections[i]["LANES"][j]["COLOUR"] = "RED"  

        while car_counter < len(vehicles) and t == vehicles[car_counter]["TIME_SLOT"]:
            veh_id = vehicles[car_counter]["VEHICLE_ID"]
            inter = vehicles[car_counter]["ENTRY_LANE"][0]
            entry = vehicles[car_counter]["ENTRY_LANE"][1]
            ext = vehicles[car_counter]["EXIT_LANE"]
            vehicle_route[car_counter] = {"VEHICLE_ID": veh_id, "ROUTE": routes[((inter, entry),ext)], "ROUTE_INDEX": 0}
            i = 0
            while i < len(intersections[inter]["LANES"][entry]["CELLS"]):
                if intersections[inter]["LANES"][entry]["CELLS"][i] == 0:
                    intersections[inter]["LANES"][entry]["CELLS"][i] = veh_id
                    break
                else: i += 1
            car_counter += 1 
        
        # Move the vehicles
        for i in range(len(vehicle_route)):
            # Initial data for current vehicle
            veh_id = vehicle_route[i]["VEHICLE_ID"]
            route_index = vehicle_route[i]["ROUTE_INDEX"]
            current_int = vehicle_route[i]["ROUTE"][route_index][0]
            current_lane = vehicle_route[i]["ROUTE"][route_index][1]
            destination_lane = vehicle_route[i]["ROUTE"][route_index+1]
            
            lane_cell = intersections[current_int]["LANES"][current_lane]["CELLS"]
            if veh_id in lane_cell:
                veh_position = lane_cell.index(veh_id)
            else: continue         
            
            # Moves cars at front of the lane
            if veh_position == 0:
                # Check if Traffic Light at vehicles intersection is green
                if intersections[current_int]["LANES"][current_lane]["COLOUR"] == "GREEN":
                    
                    # Check if cars destination lane is an exit lane - if yes then "remove" it
                    if "EXT" in destination_lane:
                        intersections[current_int]["LANES"][current_lane]["CELLS"][0] = 0
                        cars_exited += 1
                        print(f"Car Has Exited - Total cars exited = {cars_exited}")
                        continue
                    
                    # Check if last cell in next lane is not empty   
                    if intersections[destination_lane[0]]["LANES"][destination_lane[1]]["CELLS"][-1] == 0: 
                        
                        # Update next lanes cell ID with previous lanes cell ID
                        intersections[destination_lane[0]]["LANES"][destination_lane[1]]["CELLS"][-1] \
                        = intersections[current_int]["LANES"][current_lane]["CELLS"][0]
                        # Reset current lanes cell ID
                        intersections[current_int]["LANES"][current_lane]["CELLS"][0] = 0
                        # Update vehicles routeing index
                        vehicle_route[i]["ROUTE_INDEX"] += 1
                        continue
                
            # Move cars in the rest of the lane
            if veh_position > 0:
                # Check if the cars next lane is the adjacent lane (requires merging)
                if vehicle_route[i]["ROUTE"][vehicle_route[i]["ROUTE_INDEX"]] in neighbour_map:
                    if vehicle_route[i]["ROUTE"][vehicle_route[i]["ROUTE_INDEX"]+1] ==\
                        neighbour_map[vehicle_route[i]["ROUTE"][vehicle_route[i]["ROUTE_INDEX"]]]:
                        # If adjacent lane is free, merge into adjacent lane
                        if intersections[destination_lane[0]]["LANES"][destination_lane[1]]["CELLS"][veh_position] == 0:
                            # Update next cells ID with previous cells ID
                            intersections[destination_lane[0]]["LANES"][destination_lane[1]]["CELLS"][veh_position] \
                            = intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position]  
                            # Reset current lanes cell ID
                            intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position] = 0
                            vehicle_route[i]["ROUTE_INDEX"] += 1
                            cars_merged += 1
                            print(f"Car Has Merged - Total cars merged = {cars_merged}")
                            continue
                
                if lane_cell[veh_position - 1] == 0:
                    # Update next cells ID with previous cells ID
                    intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position-1] \
                    = intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position]
                    # Reset current lanes cell ID
                    intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position] = 0
                    continue
                
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")            
    return intersections, vehicles, vehicle_route

intersections, vehicles, vehicle_route = simulation(default_light_schedule, vehicles,  routes, neighbour_map)      
