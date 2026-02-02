import gurobipy as gp
from Traffic_Simulation import *

min_green = 30 # seconds
max_green = 60 # seconds

optimised_light_schedule = {(i,j): [0]*sim_length
                            for i in intersections for j in intersections[i]["LANES"]}

Y = list(intersections.keys())

BMP = gp.Model('Benders Master Problem')

# Variables
# X - 1 if light is green, 0 else
X = {(i,j): BMP.addVar(vtype = gp.GRB.BINARY) for (i,j) in optimised_light_schedule}

# No objective - BMP just creates the light patterns 
# might have to double check this - but i think it's right, since i'll be comparing to 
# the "score" value (cars_exited) in the call_back
BMP.setObjective(0, gp.GRB.MINIMIZE)

# Constraints
# Forbid lights being on at the same time as incompatible lights 
# eg. INT1 NB cannot be on at the same time as INT1 EB. 
BMP.addConstr(X["INT1", "NB_LANE_1"] + X["INT1", "EB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "NB_LANE_1"] + X["INT1", "EB_LANE_2"] <= 1)  
BMP.addConstr(X["INT1", "NB_LANE_2"] + X["INT1", "EB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "NB_LANE_2"] + X["INT1", "EB_LANE_2"] <= 1) 

BMP.addConstr(X["INT1", "NB_LANE_1"] + X["INT1", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "NB_LANE_1"] + X["INT1", "WB_LANE_2"] <= 1)  
BMP.addConstr(X["INT1", "NB_LANE_2"] + X["INT1", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "NB_LANE_2"] + X["INT1", "WB_LANE_2"] <= 1) 

BMP.addConstr(X["INT1", "SB_LANE_1"] + X["INT1", "EB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "SB_LANE_1"] + X["INT1", "EB_LANE_2"] <= 1)  
BMP.addConstr(X["INT1", "SB_LANE_2"] + X["INT1", "EB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "SB_LANE_2"] + X["INT1", "EB_LANE_2"] <= 1)  

BMP.addConstr(X["INT1", "SB_LANE_1"] + X["INT1", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "SB_LANE_1"] + X["INT1", "WB_LANE_2"] <= 1)  
BMP.addConstr(X["INT1", "SB_LANE_2"] + X["INT1", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT1", "SB_LANE_2"] + X["INT1", "WB_LANE_2"] <= 1)  
  
BMP.addConstr(X["INT2", "NB_LANE_1"] + X["INT2", "EB_LANE_1"] <= 1)
BMP.addConstr(X["INT2", "NB_LANE_2"] + X["INT2", "EB_LANE_1"] <= 1) 
BMP.addConstr(X["INT3", "NB_LANE_1"] + X["INT3", "EB_LANE_1"] <= 1)
BMP.addConstr(X["INT3", "NB_LANE_2"] + X["INT3", "EB_LANE_1"] <= 1)     

BMP.addConstr(X["INT2", "NB_LANE_1"] + X["INT2", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT2", "NB_LANE_2"] + X["INT2", "WB_LANE_1"] <= 1) 
BMP.addConstr(X["INT3", "NB_LANE_1"] + X["INT3", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT3", "NB_LANE_2"] + X["INT3", "WB_LANE_1"] <= 1)  

BMP.addConstr(X["INT4", "NB_LANE_2"] + X["INT4", "EB_LANE_2"] <= 1)
BMP.addConstr(X["INT4", "NB_LANE_2"] + X["INT4", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT4", "NB_LANE_2"] + X["INT4", "WB_LANE_2"] <= 1)

BMP.addConstr(X["INT4", "EB_LANE_2"] + X["INT4", "WB_LANE_1"] <= 1)
BMP.addConstr(X["INT4", "EB_LANE_2"] + X["INT4", "WB_LANE_2"] <= 1)

BMP.addConstr(X["INT4", "NB_LANE_1"] + X["INT4", "WB_LANE_1"] <= 1)

BMP.optimize()





# Lights must be green for a minimum of min_green seconds
# and cannot be green longer than max_green seconds

