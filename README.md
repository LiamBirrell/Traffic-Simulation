# Traffic-Simulation

## WORK IN PROGRESS

A discrete time traffic optimisation framework utilising Logic-Based Benders Decomposition. Integrates a Gurobi Master Problem for traffic light schedule generation with a custom simulation Subproblem, using iterative callbacks to converge on optimal traffic light schedule.

TO-DO:
* Run model till completion or model returns infeasible.
* add a way to save the best light_schedule if the current_score > cars_exited from default run.