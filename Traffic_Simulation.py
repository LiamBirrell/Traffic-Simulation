from Traffic_Generation import *
import numpy as np
import copy

INT1_TIMER = 45
INT1_REPEATS = sim_length/INT1_TIMER
INT4_TIMER = 30
INT4_REPEATS = sim_length/INT4_TIMER

INT1_schedule = {}
for i in intersections["INT1"]:
    if "NB" in i:
        INT1_schedule[i] = ([1]*INT1_TIMER+[0]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "SB" in i:    
        INT1_schedule[i] = ([1]*INT1_TIMER+[0]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "EB" in i:
        INT1_schedule[i] = ([0]*INT1_TIMER+[1]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "WB" in i:    
        INT1_schedule[i] = ([0]*INT1_TIMER+[1]*INT1_TIMER)*int(INT1_REPEATS/2)
        
INT2_schedule = {}
for i in intersections["INT2"]:
    if "NB" in i:
        INT2_schedule[i] = ([0]*INT1_TIMER+[1]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "SB" in i: 
        INT2_schedule[i] = ([0]*INT1_TIMER+[1]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "EB" in i:
        INT2_schedule[i] = ([1]*INT1_TIMER+[0]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "WB" in i:  
        INT2_schedule[i] = ([1]*INT1_TIMER+[0]*INT1_TIMER)*int(INT1_REPEATS/2)
             
INT3_schedule = {}
for i in intersections["INT3"]:
    if "NB" in i:
        INT3_schedule[i] = ([1]*INT1_TIMER+[0]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "SB" in i:    
        INT3_schedule[i] = ([1]*INT1_TIMER+[0]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "EB" in i:
        INT3_schedule[i] = ([0]*INT1_TIMER+[1]*INT1_TIMER)*int(INT1_REPEATS/2)
    if "WB" in i:    
        INT3_schedule[i] = ([0]*INT1_TIMER+[1]*INT1_TIMER)*int(INT1_REPEATS/2)
        
INT4_schedule = {}
for i in intersections["INT4"]:
    if "NB" in i:
        INT4_schedule[i] = ([1]*INT4_TIMER+[0]*INT4_TIMER)*int(INT4_REPEATS/2)
    if "EB" in i:
        INT4_schedule[i] = ([0]*INT4_TIMER+[1]*INT4_TIMER)*int(INT4_REPEATS/2)
    if "WB" in i:    
        INT4_schedule[i] = [0]*(INT4_TIMER*2)+[1]*(INT4_TIMER*2)+([0]*INT4_TIMER+[1]*INT4_TIMER)*int((INT4_REPEATS-4)/2)
        
