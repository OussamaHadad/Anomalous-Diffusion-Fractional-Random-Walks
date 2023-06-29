import numpy
import random
import matplotlib.pyplot as plt
import matplotlib.colors as col

echelle = col.ListedColormap(['black','blue','white']) # White for open edges & black for closed edges

def init_grid(length, probability):
    grid = numpy.zeros((length, length))
    for i in range(length):
        for j in range(length):
            r = numpy.random.rand()
            if r < probability:
                grid[i][j] = 1.	# 1 indicates an open link and 0 a closed link
    return grid

def waterPercolation(initialGrid):
    grid = initialGrid.copy()
    length = len(grid[0])
    lst = []
    for i in range(length): # From left to right in the 1st row
        if grid[0][i] == 1.: # Empty grids from the first line
            grid[0][i] = 0.5 # Filled grids and added to lst; 0.5 indicates a grid that is filled by water
            lst.append((0, i))  # Boxes occupied by water are registered in lst
    while len(lst) > 0: # Going down row by row in the grid
        (i, j) = lst.pop() # A box coordinates are extracted from lst
        if i>0 and grid[i-1][j]==1. : # if the neighbour above is empty then it is filled by water
            grid[i-1][j] = 0.5
            lst.append((i-1, j))
        if i < length - 1 and grid[i+1][j] == 1.: # if the neighbour below is empty then it is filled by water
            grid[i+1][j] = 0.5
            lst.append((i+1, j))
        if j > 0 and grid[i][j-1] == 1.: # if the neighbour at left is empty then it is filled by water
            grid[i][j-1] = 0.5
            lst.append((i, j-1))
        if j < length - 1 and grid[i][j+1] == 1.: # if the neighbour at right is empty then it is filled by water
            grid[i][j+1] = 0.5
            lst.append((i, j+1))
    return grid


def rwPercolation(initialGrid,t):   #Random Walk and Percolation
    grid = initialGrid.copy()
    length = len(grid[0])
    lst = []
    currentPosition = [length//2, length//2]
    while grid[0][currentPosition[1]] == 0:
        currentPosition[0] += 1
        currentPosition[1] += 1
    lst.append(currentPosition)
    for i in range(t): # t is the time
        step = random.randint(1,4)    #1 for right, 2 for left, 3 for up & 4 for down
        move = 0    # move is 1 if the random walker moves and 0 if not
        position = []
        if step == 1: # and currentPosition[0]<length-1:
            position = [currentPosition[0]+1,currentPosition[1]]
            move = 1
        elif step == 2: # and currentPosition[0]>0:
            position = [currentPosition[0]-1,currentPosition[1]]
            move = 1
        elif step == 3: #and currentPosition[1]>0:
            position = [currentPosition[0],currentPosition[1]-1]
            move = 1
        elif step == 4: #and currentPosition[1]<length-:
            position = [currentPosition[0],currentPosition[1]+1]
            move = 1
        if move == 1:
            if position[0] == 0 or position[0] == length:
            	break
            if position[1] == 0 or position[1] == length:
            	break
            grid[position[0]][position[1]] = 0.5
            currentPosition = position
            lst.append(currentPosition)
    return grid

# Example:
# Parameters
length = 50
probability = 0.6
finalTime = 16000
# Functions call
first_grid = init_grid(length, probability)
last_grid = waterPercolation(first_grid)
last_grid = rwPercolation(first_grid,finalTime)
# Plotting
plt.matshow(first_grid,cmap=echelle)
plt.savefig('firstGrid'+str(probability)[2]+'.png')
plt.matshow(last_grid,cmap=echelle)
plt.savefig('finalGrid'+str(probability)[2]+'t'+str(finalTime)+'.png')
plt.show()
