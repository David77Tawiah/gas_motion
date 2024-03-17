#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:48:37 2024

@author: david
"""

from gas_motion import simulate_motion
import matplotlib as plt
import numpy as np

#### Case A: 1 molecule for initial program development
# Box size, molecule radius, number of time steps
w= 15            # Width of box
h= 15            # Height of box
r= min(w,h)/40   # Radius of a molecule
nt= 1000          # Number of time steps in simulation
# Initial position and velocity of molecule
# xs= np.array([1.])  # array of one floating point value
# ys= np.array([3.])
# vxs= np.array([0.2])  # set molecule to initially go northeast
# vys= np.array([0.2])
# draw_molecules(xs, ys, r, w,h)

### Case B: 3 molecules for testing
### Works with box size and radius from Case A
xs= np.random.rand(30)*15  # randome array of floating point valuesof the x positions of molecules, not integers
ys= np.random.rand(30)*15 # random array of y positions of the molecules
vxs= np.random.rand(30)  # random array of x velocities of the molecules
vys= np.random.rand(30)  # random array of y velocities of the molecules
# draw_molecules(xs, ys, r, w,h)    
# next_timestep(xs,ys, vxs, vys, r, w, h)

# Start simulation        
simulate_motion(xs, ys, vxs, vys, r, w, h, nt)
 