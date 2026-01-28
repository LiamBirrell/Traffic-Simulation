# Traffic-Simulation

## WORK IN PROGRESS

A Python-based traffic simulation using array-based queuing and Gurobi optimization to minimize congestion in theoretical high-density intersections.

TO-DO:

1) Simulation
* ~~Tracking LOG for each vehicle in the simulation~~

2) Visuals
* Graphs of queue lengths for each lane throughout the sim
* Heatmap of the lanes with how full each one is relative to its max length

3) Gurobi
* Master Problem - Traffic Light Sequence generation
* Sub Problem - Simulation
* Apply Benders' Decomposition algorithm (Callback)