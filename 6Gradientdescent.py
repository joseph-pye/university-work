from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.cm

'''This function implements the gradient descent method to find a minimum in the banana function'''

USER = 'Joseph Matthew Pye'
USER_ID = 'ljvs65'

#This is the function which is to be minimised
def f((x, y)):
	function = (1 - x)**2 + 100 * (y - x**2)**2
	return function
	
#This is the corresponding vector function or gradient of f
def grad_f((x, y)):
	df_dx = - (2 * (1 - x)) - 400 * x * (y - x**2)
	df_dy = 200 * (y - x**2)
	gradient = numpy.array((df_dx, df_dy))
	return gradient

#These are the points at which our minimisation technique will begin
r1 = 0.1, 0.7
r2 = 0.3, 0.7
r3 = 0.5, 0.7

#This is the number of steps our gradient descent will use
n = 5000

#This returns the coordinate of every step which is taken
def find_min(r, gamma):
	path = numpy.zeros((n, 2))
	for i in range(n):
		path[i] = r
		r = r - gamma * numpy.array( grad_f(r) )
	return path	

#These are the values between which f((x, y)) will be shown
x0, x1 = -2, 2
y0, y1 = -2, 2

#This sets up the domain for the image
image_res = 1000
dx = (x1 - x0) / image_res
dy = (y1 - y0) / image_res
x_axis = numpy.arange(x0, x1, dx)
y_axis = numpy.arange(y0, y1, dy)
image = numpy.zeros((len(x_axis), len(y_axis)))

#This transfers the data from the function to the image array
for iy, y in enumerate(x_axis):
	for ix, x in enumerate(y_axis):
		image[iy, ix] = f((x, y))
	
#These are the different paths which will be taken
path_1 = find_min(r1, 0.002)
path_2 = find_min(r2, 0.005)
path_3 = find_min(r3, 0.0001)

#This list contains the coordinates of the minimum point
minimum = path_1[-1,0], path_1[-1,1]

#This prints the minimum point
ANSWER2 = 'The minimum point is %.2f, %.2f' %(minimum)
print ANSWER2

#This plots all 3 paths on a grayscale map of the function, red demonstrates a sensible 
#value of gamma, blue is too large and green is too small
pyplot.figure()
pyplot.plot(path_1[:,0], path_1[:,1], color = 'red', marker = 'x', label = 'Sensible gamma value')
pyplot.plot(path_2[:,0], path_2[:,1], color = 'blue', marker = 's', label = 'Gamma too big')
pyplot.plot(path_3[:,0], path_3[:,1], color = 'green', marker = '*', label = 'Gamma too small')
im = pyplot.imshow(image, 
					extent = (x0, x1, y0, y1), 
					origin = 'lower', 
					cmap = matplotlib.cm.gray,
					norm = matplotlib.colors.LogNorm(vmin = 0.01, vmax = 2000))
pyplot.colorbar(im, orientation = 'vertical')
pyplot.xlabel('x Coordinate')
pyplot.ylabel('y Coordinate')
pyplot.legend()
pyplot.title('Minimising the Banana Function using Gradient descent')
pyplot.show()

ANSWER1 = '''For a gamma value which is too big (like the blue plot on my graph),the 
position of the marker oscillates about the lowest point, if it were even bigger, it would
diverge from it. For a gamma value of about the right size, the marker will reach the
minimum point without too many iterations. For a gamma value too small, the marker will 
either not reach the minimum or it will take too many iterations.'''





			
	

	


		
	