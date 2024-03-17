# gas_motion.py
"""
Simulates and animates the motion of particles in a two-dimensional box.

In order to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).
"""
# DO NOT MODIFY the given function docstrings.

import numpy as np
import matplotlib.pyplot as plt
import shapes


def draw_molecules(xs, ys, r, w, h):
    """
    Draws the molecules in a box of width w and height h and show them for at
    least 0.01 seconds.
    xs[i], ys[i] are the x and y coordinates of the ith molecule. Draws all
    molecules in the same color except for the first one.

    Parameters:
        xs (1D numpy array): x positions of the molecules
        ys (1D numpy array): y positions of the molecules
        r (float): molecule radius
        w (float): diagram width, w > r*2
        h (float): diagram height, h > r*2
        
    Assumes all molecules fit inside the bounding box.
    """
    plt.cla()              # Clears current axes (removes all drawn objects).
    plt.xlim(0, w)         # Sets the x-axis to range from 0 to w.
    plt.ylim(0, h)         # Sets the y-axis to range form 0 to h.
    ax= plt.gca()          # Get current axes
    ax.set_aspect('equal') # Set current axes to equal scaling
    plt.xticks([])         # Removes the tick marks from the x-axis.
    plt.yticks([])         # Removes the tick marks from the y-axis.
    #######################################################
    ### DO NOT modify the function code above this line ###
    
    n= np.size(xs)

    shapes.draw_disk(xs[0], ys[0], r, 'r')
    for i in range(1,n):
        shapes.draw_disk(xs[i], ys[i], r, 'b')
        
        
        
        
    #####################################################################
    ### DO NOT delete the function code below this line               ###
    ### OK to change the pause time (pause longer) during development ###
    plt.show()            # Shows the plot.
    plt.pause(.01)        # Pauses 0.01 seconds.


def next_timestep(xs, ys, vxs, vys, r, w, h):
    """
    Returns the positions and velocities of the molecules at the next timestep,
    updated via the equations of motion, collisions between molecules and walls,
    and collisions between molecules and molecules.

    Parameters:
        xs (1D numpy array of floats): current x positions of the molecules
        ys (1D numpy array of floats): current y positions of the molecules
        vxs (1D numpy array of floats): current x velocities of the molecules
        vys (1D numpy array of floats): current y velocities of the molecules
        r (float): molecule radius
        w (float): diagram width
        h (float): diagram height
    Returns as a tuple:
        xs (1D numpy array of floats): x positions of the molecules after 1 timestep
        ys (1D numpy array of floats): y positions of the molecules after 1 timestep
        vxs (1D numpy array of floats): x velocities of the molecules after 1 timestep
        vys (1D numpy array of floats): y velocities of the molecules after 1 timestep
    """
    
    n = np.size(xs)
    xs += vxs
    ys += vys
    for i in range(n):
        if xs[i]<w/2 and ys[i]<h/2:
            if xs[i]<0:
                xs[i]=r
            if ys[i]<0:
                ys[i]=r
            
        elif xs[i]<w/2 and ys[i]>=h/2:
            if xs[i]<0:
                 xs[i]=r
            if ys[i]>=h:
                 ys[i]=h-r
             
        elif xs[i]>=w/2 and ys[i]<h/2:
            if xs[i]>=w:
                 xs[i]=w-r
            if ys[i]<0:
                 ys[i]=r
                 
        else:
            if xs[i]>=w:
                 xs[i]=w-r
            if ys[i]>=h:
                 ys[i]=h-r
             
        
        if xs[i]==r or xs[i]==w-r:
            vxs[i]= -1*vxs[i]
        if ys[i]==r or ys[i]==h-r:
            vys[i]= -1*vys[i]
        
    return (xs, ys, vxs, vys)
        
        
    
        
    



def check_collision(xs, ys, vxs, vys, r):
    """
    Returns the velocities of two molecules.  The velocities are updated if 
    the molecules have collided; otherwise the velocities are unchanged.

    Parameters:
        xs (1D numpy array of floats): x positions of the two molecules
        ys (1D numpy array of floats): y positions of the two molecules
        vxs (1D numpy array of floats): x velocities the two molecules
        vys (1D numpy array of floats): y velocities the two molecules
        r (float): molecule radius
    Returns as a tuple:
        vxsNew (1D numpy array of floats): x velocities the two molecules
        vysNew (1D numpy array of floats): y velocities the two molecules
    """
    pass  ### TODO: implement this function
    n = np.size(xs)
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]
    for i in range (n):
        vxsNew_one = 1/((dx**2)+(dy**2))*((vxs[1]*(dx**2))+(vys[1]*dx*dy)+(vxs[0]*(dy**2))-(vys[0]*dx*dy))
        vysNew_one = 1/((dx**2)+(dy**2))*((vxs[1]*(dx*dy))+(vys[1]*(dy**2))-(vxs[0]*(dx*dy))+(vys[0]*(dx**2)))
        vxsNew_two = 1/((dx**2)+(dy**2))*((vxs[0]*(dx**2))+(vys[0]*dx*dy)+(vxs[1]*(dy**2))-(vys[1]*dx*dy))
        vysNew_two = 1/((dx**2)+(dy**2))*((vxs[0]*(dx*dy))+(vys[0]*(dy**2))-(vxs[1]*(dx*dy))+(vys[1]*(dx**2)))
        vxsNew = np.array([vxsNew_one, vxsNew_two]) 
        vysNew = np.array([vysNew_one, vysNew_two])
        print(vxsNew, vysNew)
    
    
    return(vxsNew,vysNew)


def simulate_motion(xs, ys, vxs, vys, r, w, h, nt):
    """
    Draws a simulation of the molecules for nt timesteps.

    Parameters:
        xs (1D numpy array of floats): initial x positions of the molecules
        ys (1D numpy array of floats): initial y positions of the molecules
        vxs (1D numpy array of floats): initial x velocities of the molecules
        vys (1D numpy array of floats): initial y velocities of the molecules
        r (float): molecule radius
        w (float): diagram width
        h (float): diagram height
        nt (int): number of time steps
    """
    # Set up figure window
    plt.close()
    plt.figure(1)
    plt.pause(2)
    plt.show()
    #######################################################
    ### DO NOT modify the function code above this line ###
    ### TODO: add your code below this line             ###
    draw_molecules(xs, ys, r, w,h) 
    for i in range(nt):
        next_timestep(xs, ys, vxs, vys, r, w, h)
        draw_molecules(xs, ys, r, w, h)
        check_collision(xs, ys, vxs, vys, r)
    

    
    
#### Script code
if __name__ == '__main__':
    # Code in this if-block executes only if this file is run as a script.
    # Code in this if-block will not execute if this module is imported.
    
    ### Add code below to test your functions ###
    

    plt.close('all')  # Close all currently opened figure windows
    #### Case A: 1 molecule for initial program development
    # Box size, molecule radius, number of time steps
    w= 6.            # Width of box
    h= 4.            # Height of box
    r= min(w,h)/20   # Radius of a molecule
    nt= 400          # Number of time steps in simulation
    # Initial position and velocity of molecule
    # xs= np.array([1.])  # array of one floating point value
    # ys= np.array([3.])
    # vxs= np.array([0.2])  # set molecule to initially go northeast
    # vys= np.array([0.2])
    # draw_molecules(xs, ys, r, w,h)
    
    ### Case B: 3 molecules for testing
    ### Works with box size and radius from Case A
    xs= np.array([1., 2, 5])  # array of floating point values, not integers
    ys= np.array([1., 1, 1])
    vxs= np.array([0.2, -0.1,   0])  # one molecule goes northeast, 
    vys= np.array([0.2,    0, 0.1])  #   one goes west, and one goest north
    # draw_molecules(xs, ys, r, w,h)    
    # next_timestep(xs,ys, vxs, vys, r, w, h)
  
    # Start simulation        
    simulate_motion(xs, ys, vxs, vys, r, w, h, nt)
