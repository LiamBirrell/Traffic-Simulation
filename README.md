# Traffic-Simulation

## WORK IN PROGRESS

A discrete time traffic optimisation framework utilising Logic-Based Benders Decomposition. Integrates a Gurobi Master Problem for traffic light schedule generation with a custom simulation Subproblem, using iterative callbacks to converge on optimal traffic light schedule.

TO-DO:
* # Gurobi - Final Boss
* Master Problem - Traffic Light Sequence generation
    * ~~illegal lights on at sime time~~
    * lights can not be green for longer than 90 seconds and must be on for a minimum of 30 seconds
        * apply logic from sports timetabling project to "shift" through the timeslots
    * If car is at front of lane, light must go green within X seconds (is this needed?)
* Sub Problem - Simulation
* Apply Benders' Decomposition algorithm (Callback)
    * Run BMP solution through BSP (simulation)
    * Check if "cars exited" is a good value
    * if not - tell gurobi to not use that pattern again
    * keep going until the roof has been lowered enough that an optimal solution has been found that passes as many cars through the simulation as possible 