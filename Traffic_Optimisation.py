import gurobipy as gp
from Traffic_Data import *
from Traffic_Simulation import *
from Traffic_Generation import *

min_green = 20 # seconds
max_green = 90 # seconds

phases = ["INT1_NS", "INT1_EW", "INT2_NS", "INT2_EW", "INT3_NS", "INT3_EW", 
          "INT4_NB", "INT4_EB", "INT4_WB"]

incompatible_phases = {"INT1_NS": ["INT1_EW"],
                       "INT2_NS": ["INT2_EW"],
                       "INT3_NS": ["INT3_EW"],
                       "INT4_NB": ["INT4_EB", "INT4_WB"],
                       "INT4_EB": ["INT4_WB"]}

phase_to_lane = {"INT1_NS": [("INT1", "NB_LANE_1"), ("INT1", "NB_LANE_2"),
                             ("INT1", "SB_LANE_1"), ("INT1", "SB_LANE_2")],
                 "INT1_EW": [("INT1", "EB_LANE_1"), ("INT1", "EB_LANE_2"),
                             ("INT1", "WB_LANE_1"), ("INT1", "WB_LANE_2")],
                  
                 "INT2_NS": [("INT2", "NB_LANE_1"), ("INT2", "NB_LANE_2"),
                             ("INT2", "SB_LANE_1"), ("INT2", "SB_LANE_2")],
                 "INT2_EW": [("INT2", "EB_LANE_1"), ("INT2", "WB_LANE_1")],
                  
                 "INT3_NS": [("INT3", "NB_LANE_1"), ("INT3", "NB_LANE_2"),
                             ("INT3", "SB_LANE_1"), ("INT3", "SB_LANE_2")],
                 "INT3_EW": [("INT3", "EB_LANE_1"), ("INT3", "WB_LANE_1")],
                  
                 "INT4_NB": [("INT4", "NB_LANE_1"), ("INT4", "NB_LANE_2")],
                 "INT4_EB": [("INT4", "EB_LANE_1"), ("INT4", "EB_LANE_2")], 
                 "INT4_WB": [("INT4", "WB_LANE_1"), ("INT4", "WB_LANE_2")]
                 }

lane_to_phase = {lane: phase for phase, lanes in phase_to_lane.items() for lane in lanes}

optimised_light_schedule = {(i,j): [0]*sim_length
                            for i in intersections for j in intersections[i]["LANES"]}

BMP = gp.Model('Benders Master Problem')

# Variables
# X - 1 if phase p is "on" in timeslot t, 0 else
X = {(p,t): BMP.addVar(vtype = gp.GRB.BINARY) for p in phases for t in range(sim_length)}

Theta = BMP.addVar(vtype=gp.GRB.CONTINUOUS, lb=0, ub=num_vehicles)

BMP.setObjective(Theta, gp.GRB.MAXIMIZE)

# Constraints
# Incompatibility constraints
for pi in incompatible_phases.keys():
    for pj in incompatible_phases[pi]:
        for t in range(sim_length):
            BMP.addConstr(X[pi, t] + X[pj, t] <= 1)


# Lights cannot be green longer than max_green seconds 
for p in phases:
    for s in range(sim_length-max_green):
        BMP.addConstr(gp.quicksum(X[p,t] for t in range(s,s+max_green+1)) <= max_green)

# Lights must be green for a minimum of min_green seconds
for p in phases:
    for s in range(1, sim_length-min_green):
        BMP.addConstr(gp.quicksum(X[p,t] for t in range(s, s+min_green+1)) 
                     >= min_green*(X[p,s] - X[p,s-1]))

lane_increments = {(i,j): 0
                    for (i,j) in optimised_light_schedule}   
 
highest_percentage = {}
def Callback(model, where):
    if where == gp.GRB.Callback.MIPSOL:
        # Get Gurobi's proposed schedule
        XV = model.cbGetSolution(X)
        
        # Reconstruct Schedule
        current_schedule = {(i,j): [int(round(XV[p, t])) for t in range(sim_length)]
                            for p in phases for (i,j) in phase_to_lane[p]}
                
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
            congested_phase = lane_to_phase[(i,j)]
            capacity = len(intersections[i]["LANES"][j]["CELLS"])
            if any(count >= 0.95 * capacity for count in sim_log["LANE_COUNTS"][(i,j)]):
                
                # Find precantage of time the lane was "on" for
                current_green_pct = sum(current_schedule[(i,j)]) / sim_length
                
                if "INT4" in congested_phase:
                    max_cap = 0.30 
                else:
                    max_cap = 0.45
                    
                new_min_pct = min(max(current_green_pct + 0.025, 0.01), max_cap) 
                # Add feasibility cut if new_min_pct is greater than stored percentage
                if (congested_phase not in highest_percentage) or (new_min_pct > highest_percentage[congested_phase]):
                    model.cbLazy(gp.quicksum(X[congested_phase,t] for t in range(sim_length)) >= new_min_pct * sim_length)
                    highest_percentage[congested_phase] = new_min_pct
    

BMP.setParam("Seed", 97)
BMP.setParam("LazyConstraints", 1)
BMP.optimize(Callback)
