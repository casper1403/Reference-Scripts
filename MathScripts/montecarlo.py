import random
import numpy
import matplotlib.pyplot as plt
import math

"""Function to calculate the area under a function with the Monte Carlo mathod and plot the graph

Script takes a lot of time if the plot is made. To speed up the script increase the Xstept function


Casper Van der Vliet
11052953
"""

global Xsteps
Xsteps = 0.09

def func(x):
    return math.sin(x)

def montecarlo(func, x1, y1, x2, y2):

    global Xsteps

    # Define list for keeping track of points
    Above = []
    Under = []
    Function = []

    # Loop x times to determine x values
    for x in numpy.arange(x1,x2, Xsteps):
        # Call function to determine y value
        Y = func(x)
        Function.append(Y)

        # At the given x value generate random points between y1 an y2 and check if under or above Y
        for i in range(50):

            Ypoint = (x,  random.randrange((100 * y1) ,(100 * y2))/100)


            if Ypoint[1] > Y and Ypoint[1] > 0 :
                Above.append(Ypoint)


            if Ypoint[1] > Y and Ypoint[1] < 0 :
                Under.append(Ypoint)


            if Ypoint[1] < Y and Ypoint[1] > 0 :
                Under.append(Ypoint)


            if Ypoint[1] < Y and Ypoint[1] <0 :
                Above.append(Ypoint)




    for i in Above:
        plt.plot(i[0],i[1] , 'ro')
    for i in Under:
        plt.plot(i[0],i[1] , 'bo')
    plt.plot(numpy.arange(x1,x2, Xsteps), Function)
    plt.show()



    return ((len(Under)/ (len(Under) + len(Above))) * ((x2 - x1) * ( y2 - y1)) )

montecarlo(func,-2,-2,2,2)
