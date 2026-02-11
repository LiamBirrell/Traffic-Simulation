# Traffic-Simulation

## WORK IN PROGRESS

A discrete time traffic optimisation framework utilising Logic-Based Benders Decomposition. Integrates a Gurobi Master Problem for traffic light schedule generation with a custom simulation Subproblem, using iterative callbacks to converge on optimal traffic light schedule.

TO-DO:
* find better solutions

### Default Schedule
![Default Heatmap](default_schedule_heatmap.png)
![Default Throughput](default_schedule_cars_exited.png)

### Optimal Schedule (10% increase in throughput)
![Optimized Heatmap](optimised_schedule_heatmap.png)
![Optimized Throughput](optimised_schedule_cars_exited.png)