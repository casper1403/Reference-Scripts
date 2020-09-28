import numpy
import matplotlib.pyplot as plt

"""Script that takes a function, a starting point, an endpoint and stepsize as input and outputs the
integal of that function

Casper van der Vliet
11052953"""

def func1(x):
	return x**2

def plot(YValues, deltaX , a , b):
	#Function to plot he graph when called

	plt.plot(numpy.arange(a , b , deltaX), YValues)
	plt.show()


def riemann(func1,a,b,N):

	YValues = []
	Squares = []

	#Set step size
	deltaX = ((b-a)/(N))

	#Determine the Y values by calling the function
	for x in numpy.arange(a , b , deltaX):
		YValues.append(func1(x))

	#determine te area of each square and append to list
	for i in range(0,len(YValues)):
		Squares.append((YValues[i] * deltaX))


	#Plot the grapg of the input function
	plot(YValues, deltaX , a , b)


	#Return the sum of the Square list to return integral
	return sum(Squares)

riemann(func1,-10, 10 , 10)
