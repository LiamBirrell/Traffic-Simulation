import gurobipy as gp
from Traffic_Simulation import *
from Traffic_Generation import *

min_green = 20 # seconds
max_green = 90 # seconds

optimised_light_schedule = {(i,j): [0]*sim_length
                            for i in intersections for j in intersections[i]["LANES"]}

BMP = gp.Model('Benders Master Problem')

# Variables
# X - 1 if intersection (i,j) light is green in timeslot t, 0 else
X = {(i,j,t): BMP.addVar(vtype = gp.GRB.BINARY) for (i,j) in optimised_light_schedule
                                                for t in range(sim_length)}

# Y - 1 if intersection (i,j) turned green in timeslot t, 0 else
Y = {(i,j,t) :BMP.addVar(vtype = gp.GRB.BINARY) for (i,j) in optimised_light_schedule
                                                for t in range(sim_length)}

Theta = BMP.addVar(vtype=gp.GRB.CONTINUOUS, lb=0, ub=num_vehicles)

# No objective - BMP just creates the light patterns 
# might have to double check this - but i think it's right, since i'll be comparing to 
# the "score" value (cars_exited) in the call_back
# BMP.setObjective(0, gp.GRB.MINIMIZE)
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
# Linking constraint
for (i,j) in optimised_light_schedule:
    for t in range(sim_length):
        # At start, if X is 1, then Y is 1
        if t == 0:
            BMP.addConstr(Y[i,j,t] >= X[i,j,t])
            # If X turns "on", Y must be 1
        else:
            BMP.addConstr(X[i,j,t] - X[i,j,t-1] <= Y[i,j,t])

# Forbid lights being on at the same time as incompatible lights 
# eg. INT1 NB cannot be on at the same time as INT1 EB. 
for (i,j) in incompatible_lights.keys():
    for (k,m) in incompatible_lights[i,j]:
        for t in range(sim_length):
            BMP.addConstr(X[i, j, t] + X[k, m, t] <= 1)

# Lights cannot be green longer than max_green seconds 
# i.e., X can only be 1 for a total of max_green time window segments
for (i,j) in optimised_light_schedule:
    for s in range(sim_length-max_green):
        green_light_max = BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(s,s+max_green+1)) <= max_green)
          
# Lights must be green for a minimum of min_green seconds (if they're on) 
# i.e., if Y=1 within the last 19 seconds, then X at this timestep must also be 1
for (i,j) in optimised_light_schedule:
    for t in range(sim_length):
        start_window = max(0, t - min_green + 1)
        BMP.addConstr(X[i,j,t] >= gp.quicksum(Y[i,j,k] for k in range(start_window, t+1)))

# Lights cannot be turned "on" in the last min_green seconds
cutoff = sim_length - min_green
for (i,j) in optimised_light_schedule:
    for t in range(cutoff + 1, sim_length):
        BMP.addConstr(Y[i,j,t] == 0)

# # All lights must be green for atleast 20% of the total sim length        
for (i,j) in optimised_light_schedule:
    BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(sim_length)) >= 0.20 * sim_length)
  
lane_increments = {(i,j): 0.2
                    for (i,j) in optimised_light_schedule}    
  
def Callback(model, where):
    if where == gp.GRB.Callback.MIPSOL:
        # Get Gurobi's proposed schedule
        XV = model.cbGetSolution(X)
        
        # Reconstruct Schedule & Run Simulation
        current_schedule = {}
        for (i, j) in optimised_light_schedule:
            current_schedule[(i, j)] = [int(round(XV[i, j, t])) for t in range(sim_length)]
            
        # Run the simulation with the current schedule
        _i, _v, _r, sim_log, current_score = simulation(current_schedule, vehicles, routes, neighbour_map)
        
        cuts_added = set()
        for t in range(int(sim_length/60)):
            for (i,j) in current_schedule:
                if sim_log["LANE_COUNTS"][i, j][t] == len(intersections[i]["LANES"][j]["CELLS"]):
                            cuts_added.add((i,j))
                            
        # If a lane is full during any 60 second interval of the simulation
        # Add a cut that increases the amount of "on" time that lane can have            
        if (i,j) not in cuts_added:
            if lane_increments[i,j] <= 0.7:
                lane_increments[i, j] += 0.05
                model.cbLazy(gp.quicksum(X[i,j,k] for k in range(sim_length)) >= lane_increments[i, j] * sim_length)
    
        # Identify Green Lights
        current_on_keys = [k for k in X if XV[k] > 0.5]
        
        # Build the Hamming Distance Expression
        # Distance = (N_On) + (Sum_All_Vars) - 2*(Sum_Active_Vars)
        val_n_on = len(current_on_keys)
        expr_sum_all = gp.quicksum(X.values())
        expr_sum_active = gp.quicksum(X[k] for k in current_on_keys)
        
        dist_expr = val_n_on + expr_sum_all - 2*expr_sum_active
        
        # Add the cut
        model.cbLazy(Theta <= current_score + num_vehicles * dist_expr)   
  
# WarmStart
for (i,j) in optimised_light_schedule:
    for t in range(sim_length):
        X[i,j,t].Start = default_light_schedule[i,j][t]   

BMP.setParam("LazyConstraints", 1)
BMP.optimize(Callback)
