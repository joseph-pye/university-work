from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

'''This module compares results from Euler's and Heun's method to the analytical solution
to the differential equation which describes radioactive decay'''

USER='Joseph Matthew Pye'
USER_ID='ljvs65'

T_HALF = 20.8
TAU = T_HALF / numpy.log(2)

#This function returns the decay rate at a time when there are n atoms present
def f(n):
	return -n / TAU
	
'''This function returns the exact decay curve for an initial number of atoms, N0, with a 
decay constant TAU'''
def analytic(N0, timebase):
	return N0 * numpy.exp(- timebase / TAU)
	
'''This function uses Euler's method to calculate an approximation for the decay curve'''
def solve_euler(N0, t1, n_panels):
	dt = t1 / n_panels
	n = N0
	n_history=numpy.zeros(n_panels)
	for i in range(n_panels):
		n_history[i]=n
		n = n + f(n) * dt
	return n_history
	
'''This function uses Heun's method to calculate a more accurate approximation for the 
decay curve by improving on Euler's method'''
def solve_heun(N0, t1, n_panels):
	dt = t1 / n_panels
	n = N0
	n_history=numpy.zeros(n_panels)
	for i in range(n_panels):
		n_history[i] = n
		m = (f(n) + f(n + f(n) * dt))/2
		n = n + m * dt
	return n_history
	
'''This is the data that my module will use to plot its graphs'''	
N0 = 1000
t1 = 45
n_panels = 10
	
timebase = numpy.arange(0, t1, t1 / n_panels)
n_analytic = analytic(N0, timebase)
n_euler = solve_euler(N0, t1, n_panels)
n_heun = solve_heun(N0, t1, n_panels)
err_euler=100*abs(n_euler-n_analytic)/n_analytic
err_heun=100*abs(n_heun-n_analytic)/n_analytic

'''This section will plot 2 graphs, one displaying the decay curves of the analytical 
solution and the Euler and Heun approximations and the other will show the error in the 
Euler and Heun's method'''
pyplot.figure()
pyplot.subplot(211)
pyplot.title("Decay curves of Euler's and Heun's method as well as the true decay curve")
pyplot.plot(timebase, n_euler, color = 'red', label = "Euler's method")
pyplot.plot(timebase, n_heun, color = 'blue', linestyle = '--', label = "Heun's method")
pyplot.plot(timebase, n_analytic, color = 'grey', label = "True decay curve")
pyplot.xlabel("Time/hours")
pyplot.ylabel("Number of nuclei")
pyplot.subplot(212)
pyplot.title("Error in Euler's method and Heun's method")
pyplot.semilogy()
pyplot.plot(timebase, err_euler)
pyplot.plot(timebase, err_heun)
pyplot.xlabel("Time/hours")
pyplot.ylabel("Percentage error")
pyplot.tight_layout()
pyplot.show()

ANSWER1="Heun's method is more accurate than Euler's because Eulers method simply uses the gradient at the start of each step and assumes that it doesn't change until the next step. Heun's method finds the average gradient of each step by employing Euler's method and uses this, which is far more accurate"