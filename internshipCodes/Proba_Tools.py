# These functions take as argument the list of values of a Random Variable

def mean(x):    #Mean of a discrete Random Variable
    # x is the list of values the random variable takes
    res=0.0
    N=len(x)
    for i in range(N):
        res+=float(x[i])
    res=res/(N*1.0)
    return res

def mean_square_disp_1D(x):     # Empirical Mean square displacement of a Random Walker in 1 dimension
    # x is the list of values the random variable takes
    N=len(x)
    mean_square=0.0
    mean_x=mean(x)
    for i in range(N):
        mean_square+=float(x[i])**2
    mean_square=mean_square/(N*1.0)
    mean_square-=mean_x**2
    return mean_square

def mean_square_disp_2D(r):     # Empirical Mean square displacement of a Random Walker in 2 dimensions
    #r=[[x],[y]]
    # x is the list of values the first random variable takes
    # y is the list of values the second random variable takes
    N=len(r[0])
    # The first result is the mean square displacement
    mean_square_disp_x=mean_square_disp_1D(r[0])
    mean_square_disp_y=mean_square_disp_1D(r[1])
    # The mean square displacement of r
    mean_square_disp=mean_square_disp_x + mean_square_disp_y
    return mean_square_disp


