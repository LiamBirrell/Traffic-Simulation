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
from optimal_schedule import optimal_schedule

_i, _v, _vr, default_sim_log, _ce = simulation(default_light_schedule, vehicles, routes, neighbour_map) 
_i, _v, _vr, optimised_sim_log, _ce = simulation(optimal_schedule, vehicles, routes, neighbour_map) 

def plot_results(sim_log, save_name):
    # Graph total number of cars exited
    plt.figure(figsize=(10, 5))
    plt.plot(sim_log["TIME_STEP"], sim_log["CARS_EXITED"], color="r", linewidth=3)
    plt.title("Total Throughput Over Time", fontsize=14)
    plt.xlabel("Time [seconds]")
    plt.ylabel("Total Cars Exited")
    plt.grid(True, linestyle="-")
    plt.savefig(f"{save_name}_cars_exited.png")
    plt.show()

    # Convert Lane density data to spreadsheet for heatmap plot
    df = pd.DataFrame(sim_log["LANE_COUNTS"])
    
    # Add time column index
    df.index = sim_log["TIME_STEP"]
    
    # Transpose it so Lanes are on the Y-axis and Time is on X-axis
    df = df.transpose()
    
    # Rename the tuple keys from (0,1) to strings "Int1, NB_LANE_1" etc.
    df.index = [f"{i}, {j}" for (i, j) in df.index]

    # Plot the heatmap of lane density per time step
    plt.figure(figsize=(12, 8))
    sns.heatmap(df, cmap="rocket_r", cbar_kws={'label': 'Queue Length (Cars)'})
    plt.title("Traffic Congestion Heatmap", fontsize=16)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Lane ID")
    plt.savefig(f"{save_name}_heat_map.png")
    plt.show(sim_log)

plot_results(default_sim_log, "default_schedule")
plot_results(optimised_sim_log , "optimised_schedule")
