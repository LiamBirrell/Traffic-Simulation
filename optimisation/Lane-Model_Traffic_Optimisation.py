import gurobipy as gp
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
src_path = os.path.join(project_root, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)
from Traffic_Data import *
from Traffic_Generation import *
from Traffic_Simulation import *

min_green = 20 # seconds
max_green = 90 # seconds

optimised_light_schedule = {(i,j): [0]*sim_length
                            for i in intersections for j in intersections[i]["LANES"]}

BMP = gp.Model('Benders Master Problem')

# Variables
# X - 1 if intersection (i,j) light is green in timeslot t, 0 else
X = {(i,j,t): BMP.addVar(vtype = gp.GRB.BINARY) for (i,j) in optimised_light_schedule
                                                for t in range(sim_length)}

Theta = BMP.addVar(vtype=gp.GRB.CONTINUOUS, lb=0, ub=num_vehicles)

BMP.setObjective(Theta, gp.GRB.MAXIMIZE)

incompatible_lights = {("INT1", "NB_LANE_1"): [("INT1", "EB_LANE_1"), ("INT1", "EB_LANE_2"),
                                        ("INT1", "WB_LANE_1"), ("INT1", "WB_LANE_2")],
                ("INT1", "NB_LANE_2"): [("INT1", "EB_LANE_1"), ("INT1", "EB_LANE_2"),
                                        ("INT1", "WB_LANE_1"), ("INT1", "WB_LANE_2")],
                ("INT1", "SB_LANE_1"): [("INT1", "EB_LANE_1"), ("INT1", "EB_LANE_2"),
                                        ("INT1", "WB_LANE_1"), ("INT1", "WB_LANE_2")],                
                ("INT1", "SB_LANE_2"): [("INT1", "EB_LANE_1"), ("INT1", "EB_LANE_2"),
                                        ("INT1", "WB_LANE_1"), ("INT1", "WB_LANE_2")], 
                
                ("INT2", "NB_LANE_1"): [("INT2", "EB_LANE_1"), ("INT2", "WB_LANE_1")],
                ("INT2", "NB_LANE_2"): [("INT2", "EB_LANE_1"), ("INT2", "WB_LANE_1")],                
                ("INT2", "SB_LANE_1"): [("INT2", "EB_LANE_1"), ("INT2", "WB_LANE_1")],
                ("INT2", "SB_LANE_2"): [("INT2", "EB_LANE_1"), ("INT2", "WB_LANE_1")], 

                ("INT3", "NB_LANE_1"): [("INT3", "EB_LANE_1"), ("INT3", "WB_LANE_1")],
                ("INT3", "NB_LANE_2"): [("INT3", "EB_LANE_1"), ("INT3", "WB_LANE_1")],                
                ("INT3", "SB_LANE_1"): [("INT3", "EB_LANE_1"), ("INT3", "WB_LANE_1")],
                ("INT3", "SB_LANE_2"): [("INT3", "EB_LANE_1"), ("INT3", "WB_LANE_1")],  
                
                ("INT4", "NB_LANE_2"): [("INT4", "EB_LANE_2"), ("INT4", "WB_LANE_1"),
                                        ("INT4", "WB_LANE_2")],
                ("INT4", "NB_LANE_1"): [("INT4", "WB_LANE_1")],
                
                ("INT4", "EB_LANE_2"): [("INT4", "WB_LANE_1"), ( "INT4", "WB_LANE_2")]
                }

# Constraints
# Incompatibility constraints
for (i,j) in incompatible_lights.keys():
    for (k,m) in incompatible_lights[i,j]:
        for t in range(sim_length):
            BMP.addConstr(X[i, j, t] + X[k, m, t] <= 1)

# Lights cannot be green longer than max_green seconds 
for (i,j) in optimised_light_schedule:
    for s in range(sim_length-max_green):
        BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(s,s+max_green+1)) <= max_green)

# Lights must be green for a minimum of min_green seconds
for (i,j) in optimised_light_schedule:
    for s in range(1, sim_length-min_green):
        BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(s, s+min_green+1)) 
                     >= min_green*(X[i,j,s] - X[i,j,s-1]))

lane_increments = {(i,j): 0
                    for (i,j) in optimised_light_schedule}   
 
congestion_cuts_added = set()
def Callback(model, where):
    if where == gp.GRB.Callback.MIPSOL:
        # Get Gurobi's proposed schedule
        XV = model.cbGetSolution(X)
        
        # Reconstruct Schedule
        current_schedule = {(i, j): [int(round(XV[i, j, t])) for t in range(sim_length)] 
                            for (i, j) in optimised_light_schedule}
        
        # Run the simulation with the current schedule
        _i, _v, _r, sim_log, current_score = simulation(current_schedule, vehicles, routes, neighbour_map)
        print(f"\n--- New Potential Schedule Found ---")
        print(f"Simulation Score (Cars Exited): {current_score}")

        # Build the Hamming Distance Expression
        # Score is capped at current_score unless the schedule is changed
        # by at least 100 seconds (epsilon)
        current_on_keys = [k for k in X if XV[k] > 0.5] # Identify Green Lights   
        val_n_on = len(current_on_keys) # How many lights are green in the schedule
        expr_sum_all = gp.quicksum(X.values()) # How many lights are green in next schedule
        expr_sum_active = gp.quicksum(X[k] for k in current_on_keys) # Cancel out lights that stay the same
        dist_expr = val_n_on + expr_sum_all - 2*expr_sum_active # Difference between last schedule and new schedule
        epsilon = 100
        # Add the optimality cut
        model.cbLazy(Theta <= current_score + (num_vehicles) * (dist_expr / epsilon))
        
        # Congestion cuts
        # If a lane hits 95% capacity at any point in the simulation,
        # force a higher minimum green-time percentage for that lane.         
        for (i,j) in optimised_light_schedule:
            if (i,j) not in congestion_cuts_added:
                capacity = len(intersections[i]["LANES"][j]["CELLS"])
                if any(count >= 0.95 * capacity for count in sim_log["LANE_COUNTS"][(i,j)]):
                    # Find precantage of time the lane was "on" for
                    current_green_pct = sum(current_schedule[(i,j)]) / sim_length
                    # Set lane "on" time. Cap at 60%
                    # new_min_pct = min(current_green_pct * 1.01, 0.6) 
                    if current_score < 2000:
                        # Aggressive push to break gridlocks
                        new_min_pct = min(current_green_pct * 1.20, 0.50) 
                    else:
                        # Gentle refinement for high scores
                        new_min_pct = min(current_green_pct * 1.01, 0.45)
                    
                    # Add feasibility cut
                    model.cbLazy(gp.quicksum(X[i,j,t] for t in range(sim_length)) >= new_min_pct * sim_length)
                    congestion_cuts_added.add((i,j))
        

BMP.setParam("Seed", 97)
BMP.setParam("LazyConstraints", 1)
# BMP.setParam("Threads", 8)
BMP.optimize(Callback)