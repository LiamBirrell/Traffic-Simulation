import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from Traffic_Simulation import *
# from Traffic_Optimisation import *

intersections, vehicles, vehicle_route, sim_log, cars_exited = simulation(default_light_schedule, vehicles, routes, neighbour_map) 

def plot_results(sim_log):
    # Graph total number of cars exited
    plt.figure(figsize=(10, 5))
    plt.plot(sim_log["TIME_STEP"], sim_log["CARS_EXITED"], color="r", linewidth=3)
    plt.title("Total Throughput Over Time", fontsize=14)
    plt.xlabel("Time [seconds]")
    plt.ylabel("Total Cars Exited")
    plt.grid(True, linestyle="-")
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
    plt.show()

plot_results(sim_log)
