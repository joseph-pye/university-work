from __future__ import division 
import numpy
import matplotlib.pyplot as pyplot

''' This module shows how the accuracy of the monte carlo method increases with number of points'''
#Please note that this module runs slowly due to number of loops but should still work

#This applies the monte carlo method to estimate pi for n points
def estimate_pi(n):
	hit=0
	r=numpy.zeros(n)
	x, y = numpy.random.uniform(0, 1, n), numpy.random.uniform(0, 1, n)
	for i in range(n):
		r[i] = numpy.sqrt(x[i]**2 + y[i]**2)
		if r[i] < 1: hit += 1
	return hit / n * 4
	
#This calculates the error in the monte carlo method for each value of n
def measure_error(n):
	error = numpy.zeros(50)
	for i in range(50):
		error[i] = (estimate_pi(n) - numpy.pi) / numpy.pi
	return numpy.std(error)
	
#These are the n values we will test
n = (25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200)

#Here, the values for the graph are set up
error_values=[]
for i in n:
	s = measure_error(i)
	error_values.append(s)
	
pyplot.figure()
pyplot.xlabel('Number of points used')
pyplot.ylabel('Fractional error in estimation')
pyplot.title('The Monte Carlo method applied to estimating pi')
pyplot.loglog()
pyplot.plot(n, error_values)
pyplot.show()

ANSWER1 = "As number of points increases, the accuracy increases asymptotically. This is because it becomes closer to a uniform distribution, which with an infinite number of points, would give pi."

	