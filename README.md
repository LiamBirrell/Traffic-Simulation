# Traffic-Simulation

## WORK IN PROGRESS

A discrete time traffic optimisation framework utilising Logic-Based Benders Decomposition. Integrates a Gurobi Master Problem for traffic light schedule generation with a custom simulation Subproblem, using iterative callbacks to converge on optimal traffic light schedule.

TO-DO:
* # Gurobi - Final Boss
* ~~Master Problem - Traffic Light Sequence generation~~
    * Fix constraints so they obey time limit laws - its breaking for some reason
* ~~Sub Problem - Simulation~~
* Apply Benders' Decomposition algorithm (Callback)
    * Run BMP solution through BSP (simulation)
    * Check if "cars exited" is a good value
    * if not - tell gurobi to not use that pattern again
    * keep going until the roof has been lowered enough that an optimal solution has been found that passes as many cars through the simulation as possible 