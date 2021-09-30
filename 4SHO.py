from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import scipy.integrate

'''This module models the angular displacement and angular velocity of a damped harmonic oscillator'''

USER="Joseph Matthew Pye"
USER_ID="ljvs65"
#REMEMBER TO GET RID OF T VALUES THEY DO NOTHING

#Physical constants
g=9.81

#System properties
LENGTH=1.00
KAPPA=0.20
MASS=1.00

'''This function defines the motion of the oscillator'''
def f((theta, omega), t):
	dTheta = omega
	dOmega = - KAPPA * omega -  g / LENGTH * numpy.sin(theta)
	return numpy.array((dTheta, dOmega))
	
#Initial conditions
THETA0 = 0.2
OMEGA0 = 0
X0 = numpy.array((THETA0, OMEGA0))	

'''This function solves the equation for the oscillator numerically'''
def solve_euler(X0, t1, n_panels):
	x = X0
	res_euler = numpy.zeros((n_panels,2))
	t = t1
	for i in range (n_panels):
		t = t + dt
		res_euler[i] = x
		x = x + f(x, t) * dt
	return res_euler
	
n_panels, t1 = 5000, 20
dt = t1 / n_panels
timebase = numpy.arange(n_panels)*dt
values = scipy.integrate.odeint(f, X0, timebase) #odeint finds an exact solution
euler_values = solve_euler(X0, t1, n_panels)

'''This plots a graph of displacement against time for both solutions and then the velocity against displacement'''
pyplot.figure()
pyplot.subplot(211)
pyplot.plot(timebase, values[:,0], color='grey')
pyplot.plot(timebase, euler_values[:,0])
pyplot.xlabel('Time')
pyplot.ylabel('Angular displacement')
pyplot.subplot(212)
pyplot.plot(euler_values[:,0],euler_values[:,1])
pyplot.plot(values[:,0],values[:,1], color='grey')
pyplot.xlabel('Angular velocity')
pyplot.ylabel('Angular displacement')
pyplot.show()

ANSWER1='Euler appears to have a larger amplitude, this is due to Eulers method overestimating'
ANSWER2='The amplitude of oscillation increases which is clearly not valid as damping could not do this'