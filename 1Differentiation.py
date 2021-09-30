'''This module contains functions to compute the derivative of f(x)=xsin(x) via analytical and numerical methods, it then plots a graph of these against a series of x values'''
USER='JOSEPH MATTHEW PYE'
USER_ID='LJVS65'

import numpy
import matplotlib.pyplot as pyplot

pi=numpy.pi
dx=0.25

def f(x):									#This function will return an array of xsin(x) values corresponding to an array of x values which are input
	return x*(numpy.sin(x))
	
def f_prime_analytic(x):					#This function will return an array of the derivative of f(x)=xsin(x) corresponding to an array of x values, using the function f(x)
	return x*(numpy.cos(x))+numpy.sin(x)
	
def f_prime_numeric(x):						#This function will return approximation of the first derivative of f(x) using 0.25 as an "infinitesimal", this would also work if the function f(x) was changed
    return (f(x+dx)-f(x))/(dx) 
       
x_values=numpy.linspace(-pi,pi,100)			
y_values=f(x_values)
analytic_values=f_prime_analytic(x_values)
numeric_values=f_prime_numeric(x_values)		#This is a list of all the values which my module will need in order to produce the graph   
 
pyplot.figure()
pyplot.figure(figsize=(8,3))			#This specifies the size which the plot produced will be
pyplot.plot(x_values,analytic_values,color='green',label='Results from analytical method')	#This produces a plot of the array of f'(x) values found by the analytical method against the array of x values
pyplot.plot(x_values,numeric_values,color='blue',label='Results from numerical method')		#This produces a plot of the array of f'(x) values found by the numerical method against the array of x values
pyplot.xlabel('x - no units')			
pyplot.ylabel('xcos(x)+sin(x) - no units') 
pyplot.legend()				#This creates the legend in which the plot labels will appear
pyplot.show()

ANSWER1= 'The smaller the value of dx is, the closer the plot will be to the plot of the true values of df(x)/dx'






	