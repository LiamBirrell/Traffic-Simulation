# Traffic-Simulation

## WORK IN PROGRESS

A discrete time traffic optimisation framework utilising Logic-Based Benders Decomposition. Integrates a Gurobi Master Problem for traffic light schedule generation with a custom simulation Subproblem, using iterative callbacks to converge on optimal traffic light schedule.

TO-DO:

1) Simulation
* ~~Tracking LOG for each vehicle in the simulation~~

2) Visuals
* ~~Graphs of queue lengths for each lane throughout the sim~~
* ~~Heatmap of the lanes with how full each one is relative to its max length~~

3) Gurobi
* Master Problem - Traffic Light Sequence generation
    * ~~illegal lights on at sime time~~
    * lights can not be green for longer than 90 seconds and must be on for a minimum of 30 seconds
    * If car is at front of lane, light must go green within X seconds
* Sub Problem - Simulation
* Apply Benders' Decomposition algorithm (Callback)