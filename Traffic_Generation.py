from Traffic_Data import *
import numpy as np
import random

sim_length = 3600 # seconds
num_vehicles = 5000
mean = sim_length/2
std = mean/3

entry_weights_check = {(i): sum(entry_lane_weights[i].values())
                       for i in entry_lane_weights}

exit_weights_check = {(i): sum(exit_lane_weights[i].values())
                        for i in exit_lane_weights}

if sum(entry_weights_check.values()) != 1:
    print(entry_weights_check)
    print(f"total value is {sum(entry_weights_check.values())}: "\
          f"a disrepancy of {round(abs(1-sum(entry_weights_check.values())),3)} is present")
    raise ValueError("Values in entry_lane_weights do not sum to 1\n"\
                     "\t\t\tSee above for intersections and their summations")
     
# for i in exit_weights_check:
if sum(exit_weights_check.values()) != len(exit_weights_check):
    print(exit_weights_check)
    raise ValueError("Values in exit_lane_weights donot sum to 1\n"\
                      "\t\t\tSee above for Lanes and their summations")

entry_lane_dist = [entry_lane_weights[i][j]
                  for i in entry_lane_weights for j in entry_lane_weights[i]]

exit_lane_dist = [list(exit_lane_weights[i].values())
                 for i in exit_lane_weights]

entry_lane_assignments = np.random.multinomial(5000, entry_lane_dist)
        
exit_lane_assignments = [np.random.multinomial(i, j)
                         for i, j in zip(entry_lane_assignments, exit_lane_dist)]

time_slot_assignments = [int(np.clip(np.random.normal(mean, std), 0, sim_length-1))
              for i in range(num_vehicles)]




