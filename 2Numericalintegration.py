from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER='Joseph Matthew Pye'
USER_ID='ljvs65'

#This is the function to be integrated
def f(x):				
	return (x**2)*numpy.sin(x)

#This finds an approximate definite integral of any function between x0 and x1 for a given number of panels
def compute_numeric_integral(x0,x1,n_panels):
	width=(x1-x0)/n_panels
	area=0
	for i in range (n_panels):
		L=x0+i*width
		R=L+width
		area=area+((width)/6)*(f(L)+4*f((L+R)/2)+f(R))
	return area
		
#This calculates a value of the definite integral of f(x) between x0 and x1
def compute_analytic_integral(x0,x1):
	return (2*x1*numpy.sin(x1)-(x1**2-2)*numpy.cos(x1))-(2*x0*numpy.sin(x0)-(x0**2-2)*numpy.cos(x0))
	
#These are the values that the module will use to plot a graph with 
PANEL_COUNTS=[5,10,20,50,100,200,400,800,1600]
X0,X1=0,2

#This sets up the values of the percentage errors in the Simpson's rule
y_data=[]
ref=compute_analytic_integral(X0,X1)
for n in PANEL_COUNTS:
	s=compute_numeric_integral(X0,X1,n)
	error=100*abs((s-ref)/ref)
	y_data.append(error)
	
#This creates and displays a figure of the percentage error against the number of panels used on a log scale
pyplot.figure(figsize=(6,6))
pyplot.loglog()
pyplot.scatter(PANEL_COUNTS,y_data)
pyplot.xlabel('Number of Panels used')
pyplot.ylabel('Percentage Error')
pyplot.title('Figure 1')
pyplot.show()

ANSWER1='Increasing the number of panels increases the accuracy exponentially, because it becomes closer to the true sum of the infinitessimal elements (the definition of an integral). If the panel count is too high, python can not calculate the error as accurately'


