import numpy
import math
import random
import matplotlib.pyplot as plt

# These functions give as results the list of positions of an unbiassed Random Walk

def random_walk_1D(n):    # Random walk of n steps
    # The starting point is 0
    position = [0]
    for i in range (n):
        dx=random.choice([-1,1])
        new_x=position[i]+dx
        position.append(new_x)
    return position    #[x]

def random_walk_2D(n):    # Random walk of n steps
    # The starting point is (0,0)
    # The result is the set of positions the walker was in at each time step. It is a list of two lists: [[x],[y]]
    position = [[0],[0]]   # Initial position
    for i in range (n):
        [dx,dy]=random.choice([[0,1],[0,-1],[1,0],[-1,0]])
        new_x=position[0][i]+dx
        new_y=position[1][i]+dy
        position[0].append(new_x)
        position[1].append(new_y)
    return position[0],position[1]   #[x],[y]

def fBM_1D(n):      # n steps
    # The starting point is 0
    position = [0]
    alpha = 1./2.
    tau_t = 1.
    for i in range(n):
        r = numpy.random.rand()
        nn = (i+1)/tau_t   # n in the paper
        if (0<=r and r<alpha*(nn**(alpha-1.))):
            dx = 1
        elif (alpha*(nn**(alpha-1.))<=r and r<2*alpha*(nn**(alpha-1.))):
            dx = -1
        else:   # 2*alpha*(nn**(alpha-1.))<=r and r<1
            dx = 0
        new_x = position[i]+dx
        position.append(new_x)
    return position     #[x]

def CTRW_SubDiff_1D(final_time):    # A Pareto distribution is used for the time step
    # Inverse transform sampling is used to generate random numbers
    # The starting point is 0
    position = [0]
    alpha = 1./2.
    time=[0.]
    tau_t = 0.1
    while time[-1] <= final_time:
        r = numpy.random.rand()
        if r<1./2. :
            dx=1
        else:
            dx=-1
        dt=tau_t*((1.-r)**(-1./alpha)-1.)
        new_x = position[-1]+dx
        position.append(new_x)
        new_time = time[-1]+dt
        time.append(new_time)
    return position,time     #[x],[t]

def CTRW_SuperDiff_1D(n):   # n steps   # A Lévy distribution is used for the space step
    # Inverse transform sampling is used to generate random numbers
    # The starting point is 0
    # Constant waiting time: tau_t=1
    position = [0]
    dx = 1
    alpha = 3./2.
    for i in range(n):
        u = numpy.random.rand()
        v = numpy.random.rand()
        phi = (math.pi)*(v-1./2.)
        tau_x = dx*(math.sin(alpha*phi)/math.cos(phi))*(-numpy.log(u*math.cos(phi))/math.cos((1.-alpha)*phi))**(1.-1./alpha)
        new_x = position[i]+tau_x
        position.append(new_x)
    return position     #[x]

def plot_Random_Walk():
    choice = int(input("Which random walk would you like to draw?\n" \
        "type 1 for the 1-dimension Random Walk,\ntype 2 for the 2-dimension Random Walk,\n" \
        "type 3 for the fractional Brownian Motion,\ntype 4 for the CTRW Subdiffusion\n" \
        "type 5 for the CTRW Superdiffusion\n"))
    steps = int(input("Type the number of steps you want to simulate\n"))

    if (choice==1):
        x = random_walk_1D(steps)
        str_choice = "random_walk_1D"
    elif(choice==2):
        x,y = random_walk_2D(steps)
        str_choice = "random_walk_2D"
    elif(choice==3):
        x = fBM_1D(steps)
        str_choice = "fBM_1D"
    elif(choice==4):
        x,t = CTRW_SubDiff_1D(steps)
        str_choice = "CTRW_SubDiff_1D"
    elif(choice==5):
        x = CTRW_SuperDiff_1D(steps)
        str_choice = "CTRW_SuperDiff_1D"
    plt.ylabel('x(t)')
    if (choice==2):
        plt.xlabel('y(t)')
        plt.plot(y,x)
    elif (choice==4):
        plt.xlabel('t')
        plt.plot(t,x)
    else:
        plt.xlabel('t')
        plt.plot(x)
    plt.savefig(str_choice+str(steps)+'.png')
    plt.show()
    return
