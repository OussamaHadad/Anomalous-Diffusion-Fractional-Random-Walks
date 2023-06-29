import numpy
import math
import matplotlib.pyplot as plt
from Random_Walk import *
from Proba_Tools import *

def Mean_square_displacement(model,samples,steps_list):
    n = len(steps_list)
    variance_list=numpy.zeros(n)
    for j in range (samples):
        for i in range (n):
            if (model==2):
                r=random_walk_2D(steps_list[i])
                variance_r = mean_square_disp_2D(r)
                variance_list[i] += variance_r
            else:
                if (model==1):
                    x=random_walk_1D(steps_list[i])
                elif (model==3):
                    x=fBM_1D(steps_list[i])
                elif (model==4):
                    x,t=CTRW_SubDiff_1D(steps_list[i])
                elif (model==5):
                    x=CTRW_SuperDiff_1D(steps_list[i])
                variance_x = mean_square_disp_1D(x)
                variance_list[i] += variance_x
    variance_list = variance_list/(samples*1.0)
    return variance_list

def plot_MSD(steps_list):    # it is the list of steps we simulate
    choice = int(input("Which Random Walk would you like to use?\n" \
        "type 1 for the 1-dimension Random Walk,\ntype 2 for the 2-dimension Random Walk,\n" \
        "type 3 for the fractional Brownian Motion,\ntype 4 for the CTRW Subdiffusion\n" \
        "type 5 for the CTRW Superdiffusion\n"))
    samples = int(input("Type the number of samples you want to average on\n"))
    log_scale = int(input("Type 1 to use the log-log scale, otherwise type 0\n"))

    MSD = Mean_square_displacement(choice,samples,steps_list)

    if (choice==1):
        str_choice = "random_walk_1D"
    elif(choice==2):
        str_choice = "random_walk_2D"
    elif(choice==3):
        str_choice = "fBM_1D"
    elif(choice==4):
        str_choice = "CTRW_SubDiff_1D"
    elif(choice==5):
        str_choice = "CTRW_SuperDiff_1D"

    plt.xlabel('t')
    plt.ylabel('MSD')
    if (log_scale==1):
            plt.xscale("log")
            plt.yscale("log")
    plt.plot(steps_list,MSD,'-o')
    plt.savefig('MSD'+str_choice+str(samples)+'.png')
    plt.show()
    return

def Linear_Regression(steps_list):  # Using the least squares method
    # The plots are in the log-log scale
    choice = int(input("Which Random Walk would you like to use?\n" \
        "type 1 for the 1-dimension Random Walk,\ntype 2 for the 2-dimension Random Walk,\n" \
        "type 3 for the fractional Brownian Motion,\ntype 4 for the CTRW Subdiffusion\n" \
        "type 5 for the CTRW Superdiffusion\n"))
    str_choice = str(choice)
    samples = int(input("Type the number of samples you want to average on\n"))

    MSD = Mean_square_displacement(choice,samples,steps_list)

    n = len(MSD)
    Y = [math.log(MSD[i]) for i in range(n)]
    Y_mean = mean(Y)
    X = [math.log(steps_list[i]) for i in range(n)]
    X_mean = mean(X)

    SSxy = 0.
    SSxx = 0.
    SSyy = 0.
    for i in range(n):
        SSxy += (X[i] - X_mean)*(Y[i] - Y_mean)
        SSxx += (X[i] - X_mean)**2
        SSyy += (Y[i] - Y_mean)**2  # To compute the errors
    m = SSxy/SSxx   # alpha
    b = Y_mean - m*X_mean   # log(2D) or log(4D) in the 2-dimensional case

    # Compute D
    if (choice==2):
        D = 0.25*math.exp(b)
    else:
        D = 0.5*math.exp(b)
    print("D = ",D)

    # Compute the standard errors
    S = math.sqrt((SSyy - m*SSxy)/(n-2))
    SE_m = S/math.sqrt(SSxx)
    SE_b = S*math.sqrt((X_mean**2)/SSxx + 1./n)

    print("SE_m = ",SE_m)
    print("SE_b = ",SE_b)

    Y_predicted = []
    for i in range(n):
        Y_predicted.append(b + m*X[i])

    plt.title("\u03B1 = "+str(m))
    plt.xlabel('log(t)')
    plt.plot(X,Y,color='g')
    plt.plot(X,Y_predicted,color='r')
    plt.legend(["log(MSD)","Linear Regression"])
    plt.savefig('LinReg'+str_choice+str(samples)+'.png')
    plt.show()
    return


# Example:
N=[100,200,500,1000,2000,5000,10000]
M=Mean_square_displacement(1,100,N)
plot_MSD(N)
Linear_Regression(N)
