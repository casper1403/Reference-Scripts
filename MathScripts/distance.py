from math import sqrt
import random
from statistics import mean
import matplotlib.pyplot as plt

"""Function that takes a number of iterations as inputs and output the average
distance between 2 point in a 1x1 graph


Casper van der Vliet
11052953"""

def square(n):
    average = []

    # Loop N times and determine 2 points named XY1 and XY2
    for i in range(n):
        XY1 = (random.random(),random.random())
        XY2 = (random.random(),random.random())

        #Calulate the distance between the two points
        average.append(sqrt(((XY2[0] - XY1[0])**2) + ((XY1[1] - XY2[1])**2)) )

    return mean(average)
