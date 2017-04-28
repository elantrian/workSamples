#!/usr/bin/env python3

# by Elantrian
# www.elizabethlagesse.com
# github.com/elantrian

import math
import random
import matplotlib.pyplot as plt
from scipy import stats
import numpy

"""
Random walk in 1D and 3D. 10,000 time steps for each trial, 100 trials for each dimensionality. Arbitrary time
and distance units used throughout. R^2 and slope print to stdout, overlay plot is generated automatically. Uses
built in python pseudo-random number generator to choose from a set of directions for each step.

Call as "python3 randomWalk.py"

Requires scipy for linear regression, numpy for vector/matrix operations (for 3D), matplotlib to produce the
plots, as well as the standard python modules random and math. All modules are standard inclusions with
scientific distributions such as enthought/canopy, anaconda, etc. python3 assumed throughout.

Removing the parentheses in each print function will allow compatability with python2.6+. If scipy isn't available,
comment out import statement, as well as lines 45-49, 73-77. 1D diffusion can be performed without numpy.

"""

#1D random walk, position on x axis
#for each of 100 trials, 10,000 time steps are allowed
x = 0
position1D = [[],[]]
iterator = 0
repeat = 0
options = [1, -1]
while repeat < 100:
	iterator = 0
	x = 0
	while iterator < 10000:
		x += random.choice(options)
		#first time through, build a container
		if repeat == 0:
			position1D[1].append(x**2)
			position1D[0].append(iterator+1)
		#subsequently, just add to it
		else:
			position1D[1][iterator] += x**2
		iterator +=1
	repeat +=1

#calculate average (sum already constructed on the fly)
for item in position1D[1]:
	item = (item/100)

#linear regression
m1, b1, r1, p1, err1 = stats.linregress(position1D[0], position1D[1])

print("R^2 for 1D", r1**2)

print("Slope for 1D", m1)

#3D random walk, cartesian coord. stored as vectors
position3D = numpy.array([0,0,0])
positionList = [[],[]]
iterator = 0
repeat = 0
#vectors corresponding to the steps on various axes
options3 = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
while repeat < 100:
	iterator = 0
	#convert to vector object
	position3D = numpy.array([0,0,0])
	while iterator < 10000:
		#add vectors to perform the walk step
		position3D += numpy.array(random.choice(options3))
		if repeat == 0:
			#assuming the orgin (0,0,0) as d(0), calculate norm of vector as d(t)
			#first time through creating the appropriate container
			positionList[1].append((numpy.linalg.norm(position3D))**2)
			positionList[0].append(iterator+1)
		else:
			positionList[1][iterator] += ((numpy.linalg.norm(position3D))**2)
		iterator +=1
	repeat +=1

#calculate average (sum already constructed on the fly)
for item in positionList[1]:
	item = (item/100)


#linear regression
m3, b3, r3, p3, err3 = stats.linregress(positionList[0], positionList[1])

print("R^2 for 3D", r3**2)

print("Slope for 3D", m3)

#produce plots
plt.scatter(position1D[0], position1D[1], color='purple')
plt.scatter(positionList[0], positionList[1], color='blue')

plt.axis([0, 11000, 0, 1200000])


plt.show()
