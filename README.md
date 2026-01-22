# Traffic-Simulation

## WORK IN PROGRESS

A Python-based traffic simulation using array-based queuing and Gurobi optimization to minimize congestion in theoretical high-density intersections.



TO-DO:

1) Infrastructure
* ~~Traffic light Management - green/red light timers that are running off set patterns~~

2) Navigation
* ~~Using connections dictionary from traffic_data to make sure each car knows what it's next lane is throughout the routes~~
* ~~add mergings to routes~~

3) Main Sim
* ~~Traffic light switch logic~~
* ~~Make sure each car is placed into a lane at the correct timestamps~~
* Movement
    * Cars can only move forward if the next cell is empty 
    * Cars proceed into the next lane if the light is green
    * If a cars next lane is an adjacent lane, car must wait until the adjacent slot is empty
* Tracking
    * Every cars position at each timestep
        * How long they were in each Lane
        * Total trip duration
    * How many cars were in each lane at each timestep
* delete cars on exit

