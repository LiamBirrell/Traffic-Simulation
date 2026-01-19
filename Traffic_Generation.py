from Traffic_Data import *
import numpy as np
import random

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

entry_lane_dist = [entry_lane_weights[i]
                  for i in entry_lane_weights]

exit_lane_dist = [list(exit_lane_weights[i].values())
                  for i in exit_lane_weights]

entry_lane_slots = np.random.multinomial(5000, entry_lane_dist)
        
exit_lane_slots = [np.random.multinomial(i, j)
                          for i, j in zip(entry_lane_slots, exit_lane_dist)]

time_slots = [int(np.clip(np.random.normal(mean, std), 0, sim_length-1))
                         for i in range(num_vehicles)]

entry_lane_assignments = {(i): [list(entry_lane_weights.keys())[j]]*entry_lane_slots[j]
                          for (i,j) in zip(entry_lane_weights, range(len(entry_lane_slots)))}

exit_lane_assignments = {}
for (i,j) in zip(entry_lane_weights, exit_lane_slots): 
    current_exits = []
    for (k,j) in zip(exit_lane_weights[i],j):                  
        current_exits.extend([k]*j)
    exit_lane_assignments[i] = current_exits
    
