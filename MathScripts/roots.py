import numpy
import matplotlib.pyplot as plt

"""Function that takes to calculate and plot roots of polynomial"""

def roots(a, b ,c):

    root = []
    values = []

    #Call the function for the given values and determine if the function has x = 0
    for x in numpy.arange(-10 , 10 , 0.0001):
        zero = round(((a*(x**2)) + (b*x) + c),3)
        values.append(zero)
        # If x= 0  append to roots list
        if zero == 0:
            root.append(round(x,2))

    # If function has no roots return: string, plot and empty list.
    if len(root) == 0:
        print('This function does not have roots.')
        PlotGraph(values,root)
        return root
    # If function has roots return roots and plot graph
    else:
        PlotGraph(values,root)
        root = set(root)
        root = list(root)
        return root

# Plot graph of function
def PlotGraph(Values, zero):
    plt.plot(numpy.arange(-10 , 10 , 0.0001), Values)
    plt.axhline(y=0, color='r', linestyle='dotted')
    if len(zero) >= 1:
        plt.plot(zero[0],0,'ro')
        plt.plot(zero[-1],0,'ro')
    plt.show()

roots(3,6, 9)
