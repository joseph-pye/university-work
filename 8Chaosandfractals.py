from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.cm

USER = 'Joseph Matthew Pye'
USER_ID = 'ljvs65'

'''This module will produce plots of the convergence of complex numbers to roots of the 
equation z^4 - 1 using the Newton Raphson Method'''

def f(z):		#This is the function which we will find roots of
	return z**4 - 1
	
def df_dz(z):	#This is the gradient of the function
	return 4*z**3

n = 40			#This is the maximum number of iterations that the root finder will use

#This takes a real and a complex argument and finds a root to the function by using the 
#Newton Raphson method starting from this point
def find_root(x, y):
	z = x + y*1j
	angle = 0
	counter = 0
	for i in range(n):
		counter += 1
		z = z - f(z)/df_dz(z)
		if numpy.abs(z) == 1:
			break
		if numpy.angle(z) > 3.14 or numpy.angle(z) < -3.14: #This if condition gets rid of the striped pattern on the left side of the plots due to there being a small difference between pi and -pi
			angle = numpy.pi
		else:
			angle = numpy.angle(z)
	return angle, counter
	
#This sets the image size and resolution that will be produced for a regular and zoomed in case
x_axis_1, x_axis_2 = numpy.arange(-10, 10, 0.05), numpy.arange(5, 7.7, 0.01) 
y_axis_1, y_axis_2 = numpy.arange(-10, 10, 0.05), numpy.arange(5, 7.7, 0.01)

#This gives blank images into which we can insert the data 
dat, time = numpy.zeros((len(x_axis_1), len(y_axis_1))), numpy.zeros((len(x_axis_1), len(y_axis_1)))
dat2, time2 = numpy.zeros((len(x_axis_2), len(y_axis_2))), numpy.zeros((len(x_axis_2), len(y_axis_2)))
 
#This inserts the data for the regular image 
for iy, y in enumerate(y_axis_1):
	for ix, x in enumerate(x_axis_1):
		p = find_root(x, y)
		dat[iy, ix] = p[0]
		time[iy, ix] = p[1]

#This inserts the data for the zoomed in image
for iy, y in enumerate(y_axis_2):
	for ix, x in enumerate(x_axis_2):
		p = find_root(x, y)
		dat2[iy, ix] = p[0]
		time2[iy, ix] = p[1]

#This plots all of the data for convergence to different roots and the time taken to converge	
pyplot.figure()
pyplot.title('Convergence of complex numbers using the Newton Raphson method')
pyplot.subplot(221)
im = pyplot.imshow(dat, extent = (-10, 10, -10, 10), origin = 'lower', cmap = matplotlib.cm.PuBuGn)
pyplot.title('Convergence to roots of z^4 -1'), pyplot.xlabel('Real'), pyplot.ylabel('Imaginary')
pyplot.subplot(222)
im = pyplot.imshow(dat2, extent = (5, 7.7, 5, 7.7), origin = 'lower', cmap = matplotlib.cm.PuBuGn)
pyplot.title('Convergence zoomed in'), pyplot.xlabel('Real'), pyplot.ylabel('Imaginary')
pyplot.subplot(223)
im = pyplot.imshow(time, extent = (-10, 10, -10, 10), origin = 'lower', cmap = matplotlib.cm.PuBuGn)
pyplot.title('Time taken to converge'), pyplot.xlabel('Real'), pyplot.ylabel('Imaginary')
pyplot.subplot(224)
im = pyplot.imshow(time2, extent = (5, 7.7, 5, 7.7), origin = 'lower', cmap = matplotlib.cm.PuBuGn)
pyplot.title('Time taken zoomed in'), pyplot.xlabel('Real'), pyplot.ylabel('Imaginary')
pyplot.tight_layout()  #This stops the x labels of the top plots overlapping with the bottom plot titles
pyplot.show()

ANSWER1 = "The top two plots of my programme display the chaotic nature of this system as for a tiny change in the start position, the resulting root that is found can be completely different, shown by the four different colours in the plot. The fractal nature of the system is shown by the repeating teardrop shapes, which have their edges made up of more teardop shapes, as seen in the plots on the right hand side. Also, if we zoom in towards the center of the left hand plots, the image remains unchanged (other than a decrease in resolution)"
	