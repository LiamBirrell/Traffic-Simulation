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

Theta = BMP.addVar(vtype=gp.GRB.CONTINUOUS, lb=0, ub=num_vehicles)

# No objective - BMP just creates the light patterns 
# might have to double check this - but i think it's right, since i'll be comparing to 
# the "score" value (cars_exited) in the call_back
# BMP.setObjective(0, gp.GRB.MINIMIZE)
BMP.setObjective(Theta, gp.GRB.MAXIMIZE)

# Constraints
# Forbid lights being on at the same time as incompatible lights 
# eg. INT1 NB cannot be on at the same time as INT1 EB. 
for t in range(sim_length):
    BMP.addConstr(X["INT1", "NB_LANE_1", t] + X["INT1", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "NB_LANE_1", t] + X["INT1", "EB_LANE_2", t] <= 1)  
    BMP.addConstr(X["INT1", "NB_LANE_1", t] + X["INT1", "WB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "NB_LANE_1", t] + X["INT1", "WB_LANE_2", t] <= 1) 

    BMP.addConstr(X["INT1", "NB_LANE_2", t] + X["INT1", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "NB_LANE_2", t] + X["INT1", "EB_LANE_2", t] <= 1) 
    BMP.addConstr(X["INT1", "NB_LANE_2", t] + X["INT1", "WB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "NB_LANE_2", t] + X["INT1", "WB_LANE_2", t] <= 1) 
    
    BMP.addConstr(X["INT1", "SB_LANE_1", t] + X["INT1", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "SB_LANE_1", t] + X["INT1", "EB_LANE_2", t] <= 1)  
    BMP.addConstr(X["INT1", "SB_LANE_1", t] + X["INT1", "WB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "SB_LANE_1", t] + X["INT1", "WB_LANE_2", t] <= 1)      
    
    BMP.addConstr(X["INT1", "SB_LANE_2", t] + X["INT1", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "SB_LANE_2", t] + X["INT1", "EB_LANE_2", t] <= 1)  
    BMP.addConstr(X["INT1", "SB_LANE_2", t] + X["INT1", "WB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT1", "SB_LANE_2", t] + X["INT1", "WB_LANE_2", t] <= 1)  
      
    BMP.addConstr(X["INT2", "NB_LANE_1", t] + X["INT2", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT2", "NB_LANE_1", t] + X["INT2", "WB_LANE_1", t] <= 1)    
    BMP.addConstr(X["INT2", "NB_LANE_2", t] + X["INT2", "EB_LANE_1", t] <= 1) 
    BMP.addConstr(X["INT2", "NB_LANE_2", t] + X["INT2", "WB_LANE_1", t] <= 1)     
    
    BMP.addConstr(X["INT2", "SB_LANE_1", t] + X["INT2", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT2", "SB_LANE_1", t] + X["INT2", "WB_LANE_1", t] <= 1)    
    BMP.addConstr(X["INT2", "SB_LANE_2", t] + X["INT2", "EB_LANE_1", t] <= 1)  
    BMP.addConstr(X["INT2", "SB_LANE_2", t] + X["INT2", "WB_LANE_1", t] <= 1)     
    
    BMP.addConstr(X["INT3", "NB_LANE_1", t] + X["INT3", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT3", "NB_LANE_1", t] + X["INT3", "WB_LANE_1", t] <= 1)    
    BMP.addConstr(X["INT3", "NB_LANE_2", t] + X["INT3", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT3", "NB_LANE_2", t] + X["INT3", "WB_LANE_1", t] <= 1) 
    
    BMP.addConstr(X["INT3", "SB_LANE_1", t] + X["INT3", "EB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT3", "SB_LANE_1", t] + X["INT3", "WB_LANE_1", t] <= 1)    
    BMP.addConstr(X["INT3", "SB_LANE_2", t] + X["INT3", "EB_LANE_1", t] <= 1)     
    BMP.addConstr(X["INT3", "SB_LANE_2", t] + X["INT3", "WB_LANE_1", t] <= 1) 
    
    BMP.addConstr(X["INT4", "NB_LANE_2", t] + X["INT4", "EB_LANE_2", t] <= 1)
    BMP.addConstr(X["INT4", "NB_LANE_2", t] + X["INT4", "WB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT4", "NB_LANE_2", t] + X["INT4", "WB_LANE_2", t] <= 1)
    
    BMP.addConstr(X["INT4", "EB_LANE_2", t] + X["INT4", "WB_LANE_1", t] <= 1)
    BMP.addConstr(X["INT4", "EB_LANE_2", t] + X["INT4", "WB_LANE_2", t] <= 1)
    
    BMP.addConstr(X["INT4", "NB_LANE_1", t] + X["INT4", "WB_LANE_1", t] <= 1)
    
# Lights cannot be green longer than max_green seconds 
for (i,j) in optimised_light_schedule:
    for s in range(sim_length-max_green):
        green_light_max = BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(s,s+max_green+1)) <= max_green)
          
# Lights must be green for a minimum of min_green seconds (if they're on)      
for (i,j) in optimised_light_schedule:
    for s in range(1, sim_length-min_green+1):     
        BreakLogic = BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(s, s+min_green)) 
                                    >= min_green*(X[i,j,s] - X[i,j,s-1]))

# All lights must be green for atleast 20% of the total sim length        
for (i,j) in optimised_light_schedule:
    BMP.addConstr(gp.quicksum(X[i,j,t] for t in range(sim_length)) >= 0.20 * sim_length)
    
def Callback(model, where):
    if where == gp.GRB.Callback.MIPSOL:
        # Get Gurobi's proposed schedule
        XV = model.cbGetSolution(X)
        
        # Reconstruct Schedule & Run Simulation
        current_schedule = {}
        for (i, j) in optimised_light_schedule:
            current_schedule[(i, j)] = [int(round(XV[i, j, t])) for t in range(sim_length)]
            
        _i, _v, _r, _l, current_score = simulation(current_schedule, vehicles, routes, neighbour_map)
        
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
                
BMP.setParam("LazyConstraints", 1)
BMP.optimize(Callback)
BMP.optimize()
