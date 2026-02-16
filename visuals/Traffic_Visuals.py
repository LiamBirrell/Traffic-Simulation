import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
src_path = os.path.join(project_root, 'src')
data_path = os.path.join(project_root, 'data')

if src_path not in sys.path:
    sys.path.append(src_path)
    
if data_path not in sys.path:
    sys.path.append(data_path)
    
from Traffic_Data import *
from Traffic_Generation import *
from Traffic_Simulation import *
from optimised_schedule import optimised_schedule

_i, _v, _vr, default_sim_log, default_cars_exited = simulation(default_light_schedule, vehicles, routes, neighbour_map) 
_i, _v, _vr, optimised_sim_log, optimsied_cars_exited = simulation(optimised_schedule, vehicles, routes, neighbour_map) 

def plot_results(sim_log, save_name, intersections_data):
    # Graph total number of cars exited
    plt.figure(figsize=(10, 5))
    plt.plot(sim_log["TIME_STEP"], sim_log["CARS_EXITED"], color="r", linewidth=3)
    plt.title(f"{save_name} - Total Throughput Over Time", fontsize=14)
    plt.xlabel("Time [seconds]")
    plt.ylabel("Total Cars Exited")
    plt.grid(True, linestyle="-")
    plt.savefig(f"{save_name}_cars_exited.png")

    # Convert Lane density data to percentages for heatmap plot
    raw_counts = sim_log["LANE_COUNTS"]
    percentage_data = {}
    for (i, j), counts in raw_counts.items():
        # Get the physical capacity of this specific lane
        capacity = len(intersections_data[i]["LANES"][j]["CELLS"])
        # Avoid division by zero just in case a lane has 0 capacity
        if capacity > 0:
            percentage_data[(i, j)] = [(count / capacity) * 100 for count in counts]
        else:
            percentage_data[(i, j)] = [0 for _ in counts]
    df = pd.DataFrame(percentage_data)
    
    # Add time column index
    df.index = sim_log["TIME_STEP"]
    
    # Transpose it so Lanes are on the Y-axis and Time is on X-axis
    df = df.transpose()
    
    # Rename the tuple keys from (0,1) to strings "INT1, NB_LANE_1" etc.
    df.index = [f"{i}, {j}" for (i, j) in df.index]

    # Plot the heatmap of lane density per time step
    plt.figure(figsize=(12, 8))
    sns.heatmap(df, cmap="rocket_r", vmin=0, vmax=100, cbar_kws={'label': 'Lane Capacity Filled (%)'})
    plt.title(f"{save_name} - Traffic Congestion Heatmap", fontsize=16)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Lane ID")
    plt.savefig(f"{save_name}_heat_map.png")

plot_results(default_sim_log, "default_schedule", intersections)
plot_results(optimised_sim_log , "optimised_schedule", intersections)
