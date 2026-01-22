# Traffic-Simulation

## WORK IN PROGRESS

A Python-based traffic simulation using array-based queuing and Gurobi optimization to minimize congestion in theoretical high-density intersections.



TO-DO:

1) Infrastructure
* ~~Traffic light Management - green/red light timers that are running off set patterns~~

2) Navigation
* ~~Using connections dictionary from traffic_data to make sure each car knows what it's next lane is throughout the routes~~
* ~~add mergings to routes~~

3) Traffic/movement Laws
* Car can only move forward if the next cell is empty
* Cars at front of the lane cannot proceed into the destination lane unless the light is green
* if the light is green but the destination lane is full, the car must wait at the light until it a spot is free
* Merging laws - if a cars next lane is an adjacent lane, car must wait until the adjacent slot is empty

4) Main Engine
* The simulation loop that loops over every timestamp and tracks every cars position and at each timestep
* Make sure each car is placed into a lane at the correct timestamps
* Lane state tracking - ensuring each lane array is correctly tracking which "spots" (cells) are occupied
    * light updates
    * cars spawn/move
    * if a car needs to merge, once it enters the lane, it waits to see if the adjacent lane is empty and waits until it is
    * Record data
* delete cars on exit

