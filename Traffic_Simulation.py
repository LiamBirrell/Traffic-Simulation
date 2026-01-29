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
waitlist = {"VEHICLE_ID": [],
            "ENTRY_INTER": [],
            "ENTRY_LANE": [],
            "EXIT_LANE": [],
            # "ROUTE": []
            }

sim_log = {"TIME_STEP": [],
            "CARS_EXITED": [],
            "LANE_COUNTS": {}}

for i in intersections:
    for j in intersections[i]["LANES"]:
        sim_log["LANE_COUNTS"][(i,j)] = []  
           
def is_full(lane_cells):
    for i in lane_cells:
        if i == 0:
            return False
    return True

lane_sum = 0
for i in intersections:
    for j in intersections[i]["LANES"]:
        lane_sum += len(intersections[i]["LANES"][j]["CELLS"])


def simulation(light_sequence, vehicles, routes, neighbour_map):
    start_time = time.perf_counter()
    car_counter = 0
    cars_exited = 0
    cars_merged = 0
    lane_sum = 0
    vehicle_route = {}
    waitlist = {"VEHICLE_ID": [],
                "ENTRY_INTER": [],
                "ENTRY_LANE": [],
                "EXIT_LANE": [],
                }
    sim_log = {"TIME_STEP": [],
                "CARS_EXITED": [],
                "LANE_COUNTS": {}}
    for i in intersections:
        for j in intersections[i]["LANES"]:
            sim_log["LANE_COUNTS"][(i,j)] = [] 
            lane_sum += len(intersections[i]["LANES"][j]["CELLS"])
    
    for t in range(sim_length):
        # Check how many cars are on the road at each timestep
        cars_on_road = len(vehicle_route) - cars_exited
        print(f"Timestep = {t} | Cars on road: {cars_on_road}")
        
        # Traffic Light change logic - green if 1, red if 0
        for i in intersections:
            for j in intersections[i]["LANES"]:
                if light_sequence[(i,j)][t] == 1:
                    intersections[i]["LANES"][j]["COLOUR"] = "GREEN"  
                else:
                    intersections[i]["LANES"][j]["COLOUR"] = "RED"  
                
        # Spawn logic
        while car_counter < len(vehicles) and t == vehicles[car_counter]["TIME_SLOT"]:
            # Check the next car from vehicle that's to be added to the simulation
            veh_id = vehicles[car_counter]["VEHICLE_ID"]
            inter = vehicles[car_counter]["ENTRY_LANE"][0]
            entry = vehicles[car_counter]["ENTRY_LANE"][1]
            ext = vehicles[car_counter]["EXIT_LANE"]      
            
            # If the entry lane is full, add the car to the waitlist instead
            if intersections[inter]["LANES"][entry]["CELLS"][-1] != 0:
                # print("\t\tLane assignment was full - adding vehicle to waitlist")
                waitlist["VEHICLE_ID"].append(veh_id)
                waitlist["ENTRY_INTER"].append(inter)
                waitlist["ENTRY_LANE"].append(entry)
                waitlist["EXIT_LANE"].append(ext)  
                car_counter += 1
                continue          
            
            # If entry lane had a cell available, add that car to the entry lane
            # Bust first check if there's cars waiting to be added from the waitlist
            wait_car_spawn = False
            for j in range(len(waitlist["VEHICLE_ID"])):
                if (inter, entry) == (waitlist["ENTRY_INTER"][j], waitlist["ENTRY_LANE"][j]):
                    # If car is waiting to be added to current lane, pop it from the waitlist
                    veh_id_w = waitlist["VEHICLE_ID"].pop(j)
                    inter_w = waitlist["ENTRY_INTER"].pop(j)
                    entry_w = waitlist["ENTRY_LANE"].pop(j)
                    ext_w = waitlist["EXIT_LANE"].pop(j)       
                    
                    # Add popped vehicle to the simulation
                    vehicle_route[car_counter] = {"VEHICLE_ID": veh_id_w, "ROUTE": routes[((inter_w, entry_w),ext_w)], "ROUTE_INDEX": 0}  
                    intersections[inter_w]["LANES"][entry_w]["CELLS"][-1] = veh_id_w
                    
                    # Add the original vehicle to the wait list
                    waitlist["VEHICLE_ID"].append(veh_id)
                    waitlist["ENTRY_INTER"].append(inter)
                    waitlist["ENTRY_LANE"].append(entry)
                    waitlist["EXIT_LANE"].append(ext)
                    
                    wait_car_spawn = True
                    break
            # If no car from the waitlist was added - add the original car to the simulation        
            if not wait_car_spawn:
                vehicle_route[car_counter] = {"VEHICLE_ID": veh_id, "ROUTE": routes[((inter, entry),ext)], "ROUTE_INDEX": 0}  
                intersections[inter]["LANES"][entry]["CELLS"][-1] = veh_id
            car_counter += 1
        
        
        # Move the vehicles
        for i in list(vehicle_route.keys()):
            # Initial data for current vehicle
            veh_id = vehicle_route[i]["VEHICLE_ID"]
            route_index = vehicle_route[i]["ROUTE_INDEX"]
            current_int = vehicle_route[i]["ROUTE"][route_index][0]
            current_lane = vehicle_route[i]["ROUTE"][route_index][1]
            destination_lane = vehicle_route[i]["ROUTE"][route_index+1]
            
            # Get current vehicle position from interesections dict
            lane_cell = intersections[current_int]["LANES"][current_lane]["CELLS"]
            if veh_id in lane_cell:
                veh_position = lane_cell.index(veh_id)
            else: continue         
            
            # If car is at the fron of the lane, apply lane change
            if veh_position == 0:
                # Check if Traffic Light at vehicles intersection is green first
                if intersections[current_int]["LANES"][current_lane]["COLOUR"] == "GREEN":
                    
                    # Check if cars destination lane is an exit lane - if yes then "remove" it
                    if "EXT" in destination_lane:
                        intersections[current_int]["LANES"][current_lane]["CELLS"][0] = 0
                        cars_exited += 1
                        print(f"Car Has Exited - Total cars exited = {cars_exited}")
                        continue
                    
                    # Check for merging
                    requires_merge = False
                    if (current_int, current_lane) in neighbour_map:
                        if neighbour_map[(current_int, current_lane)] == destination_lane:
                            requires_merge = True
                        
                    if requires_merge:           
                        target_int, target_lane = destination_lane
                        # If adjacent lane is free, merge into adjacent lane
                        if intersections[target_int]["LANES"][target_lane]["CELLS"][0] == 0:
                            
                            # Update next cells ID with previous cells ID
                            intersections[target_int]["LANES"][target_lane]["CELLS"][0] \
                             = intersections[current_int]["LANES"][current_lane]["CELLS"][0] 
                            
                            # Reset current lanes cell ID
                            intersections[current_int]["LANES"][current_lane]["CELLS"][0] = 0
                            
                            # Update counters/index
                            vehicle_route[i]["ROUTE_INDEX"] += 1
                            cars_merged += 1
                            print(f"Car Has Merged - Total cars merged = {cars_merged}")
                            continue 
                        
                        else: 
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
                
            # If the car isn't at the front, apply "move forward" mechanic
            if veh_position > 0:
                # First, check if the cars next lane is the adjacent lane (requires merging)
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
                            
                            # Update counters/index
                            vehicle_route[i]["ROUTE_INDEX"] += 1
                            cars_merged += 1
                            print(f"Car Has Merged - Total cars merged = {cars_merged}")
                            # continue
                        
                        # If adjacent lane isn't free, the car waits for an opening (skips move forward code below)
                        # else: continue
                
                # Move the rest of the cars in each lane forward one cell
                if lane_cell[veh_position - 1] == 0:
                    # Update next cells ID with previous cells ID
                    intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position-1] \
                    = intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position]
                    # Reset current lanes cell ID
                    intersections[current_int]["LANES"][current_lane]["CELLS"][veh_position] = 0
                    continue
                
        # Track the lane length after every minute has passed
        if t % 60 == 0:
            sim_log["TIME_STEP"].append(t)
            sim_log["CARS_EXITED"].append(cars_exited)
            for i in intersections:
                for j in intersections[i]["LANES"]:
                    lane_count = sum(1 for k in intersections[i]["LANES"][j]["CELLS"] if k != 0)
                    sim_log["LANE_COUNTS"][(i,j)].append(lane_count)
                
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")            
    return intersections, vehicles, vehicle_route, sim_log   

if __name__ == "__main__":
    intersections, vehicles, vehicle_route, sim_log = simulation(default_light_schedule, vehicles, routes, neighbour_map) 
