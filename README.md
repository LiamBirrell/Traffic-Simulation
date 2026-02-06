# Traffic-Simulation

## WORK IN PROGRESS

A discrete time traffic optimisation framework utilising Logic-Based Benders Decomposition. Integrates a Gurobi Master Problem for traffic light schedule generation with a custom simulation Subproblem, using iterative callbacks to converge on optimal traffic light schedule.

TO-DO:
* Gurobi - Final Boss
    * Add lazyconstraint that increasese the percentage of time each lane can be green based on how congested they were in the simulation
    * maybe more, not sure yet. 