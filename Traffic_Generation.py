from Traffic_Data import *
import numpy as np
# import random

sim_length = 3600 # seconds
num_vehicles = 5000
mean = sim_length/2
std = mean/3

entry_weights_check = sum(entry_lane_weights.values())
         
exit_weights_check = {(i): sum(exit_lane_weights[i].values())
                        for i in exit_lane_weights}

if entry_weights_check != 1:
    raise ValueError("Values in entry_lane_weights do not sum to 1\n"\
                      f"\t\t\tTotal summation is {round(entry_weights_check,9)}")
     
if sum(exit_weights_check.values()) != len(exit_weights_check):
    for i in exit_weights_check:
        print({i: exit_weights_check[i]})
    raise ValueError("Values in exit_lane_weights donot sum to 1\n"\
                      "\t\t\tSee above for Lanes and their summations")


def vehicle_generation(entry_lanes, exit_lanes):
    entry_lane_dist = [entry_lanes[i]
                      for i in entry_lanes]
    
    exit_lane_dist = [list(exit_lanes[i].values())
                      for i in exit_lanes]
    
    entry_lane_slots = np.random.multinomial(5000, entry_lane_dist)
            
    exit_lane_slots = [np.random.multinomial(i, j)
                       for i, j in zip(entry_lane_slots, exit_lane_dist)]
    
    entry_lane_assignments = [[list(entry_lanes.keys())[j]]*entry_lane_slots[j]
                              for (i,j) in zip(entry_lanes, range(len(entry_lane_slots)))]
    
    exit_lane_assignments = [[list(exit_lanes[i].keys())[k]]*exit_lane_slots[j][k]
                              for (i,j) in zip(entry_lanes, range(len(entry_lane_slots)))
                              for k in range(len(exit_lane_slots[j]))]
    
    entry_lane_flatten = [entry_lane_assignments[i][j]
                          for i in range(len(entry_lane_assignments))
                          for j in range(len(entry_lane_assignments[i]))]
                         
    exit_lane_flatten = [exit_lane_assignments[i][j]
                          for i in range(len(exit_lane_assignments))
                          for j in range(len(exit_lane_assignments[i]))]
    
    time_slots = [int(np.clip(np.random.normal(mean, std), 0, sim_length*0.9))
                  for i in range(num_vehicles)]    
    
    vehicles = []
    for (i,j,k,t) in zip(range(num_vehicles),entry_lane_flatten, exit_lane_flatten, time_slots):
        vehicle_new = {"VEHICLE_ID": i+1, "ENTRY_LANE": j, "EXIT_LANE": k, "TIME_SLOT": t}
        vehicles.append(vehicle_new)
        vehicles.sort(key=lambda x: x['TIME_SLOT'])
    
    return vehicles

    
