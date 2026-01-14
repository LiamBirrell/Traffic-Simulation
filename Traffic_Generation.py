from Traffic_Data import *
import numpy as np
import random

num_vehicles = 5000
sim_length = 3600 # seconds


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

entry_lane_volume = {(i,j): num_vehicles*entry_lane_weights[i][j]
                     for i in entry_lane_weights for j in entry_lane_weights[i]}

exit_lane_volume = {(i,j): exit_lane_weights[i][j]*entry_lane_volume[i]
                    for i in entry_lane_volume for j in exit_lane_weights[i]}

