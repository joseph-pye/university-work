from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.cm
import random

'''This module simulates chemotaxis for 20 bacteria'''

USER = "Joseph Matthew Pye"
USER_ID = "ljvs65"

def f((x,y)): #This is the energy distribution that the bacteria will follow
	return 5000 - (x**2 + y**2)

x0, y0 = 20., 40. #These are the initial coordinates and the initial energy
E0 = f((x0, y0))
n = 1000		#This is the number of steps the bacteria will take
k = 0.2			#This constant defines the bacteria's sensitivity

def random_walk((x,y)):  #This function simulates a random walk which leads to an energy source
	dE_dt = 0
	dt = 100 / n
	r = numpy.array((x, y))
	coordinates = numpy.zeros((n,2))
	bearing = random.random()
	speed = (2 * numpy.sin(bearing), 2 * numpy.cos(bearing))
	shift_reg = [E0, E0, E0, E0, E0, E0, E0, E0, E0, E0]
	for i in range(n):
		t_half = 1 + k * dE_dt
		if t_half < 0.01:
			t_half = 0.01
		tau = t_half / numpy.log(2)
		q = random.random()
		if q < numpy.exp(-dt / tau):
			r[0] = r[0] + speed[0] * dt
			r[1] = r[1] + speed[1] * dt
			coordinates[i,0] = r[0]
			coordinates[i,1] = r[1]
		else:
			bearing = 2*numpy.pi*random.random()
			speed = (2 * numpy.sin(bearing), 2 *numpy.cos(bearing))
			r = r
			coordinates[i,0], coordinates[i,1] = r[0], r[1]
		new_energy = f(r)
		shift_reg.append(f(r))
		shift_reg = shift_reg[1:]
		dE = shift_reg[-1] - shift_reg[0]
		dE_dt = dE
	return coordinates

all_paths=[]	#This uses the random walk to simulate 20 bacteria
for i in range(20):
	a = random_walk((x0,y0))
	all_paths.append(a)
	
def find_ms((all_paths)): #This function finds the mean square displacement of the bacteria
	dist_energy=[]
	dist_start=[]
	for j in range(20):
		start, energy = [], []
		for i in range(n):
			dist1 = all_paths[j][i,0]**2 + all_paths[j][i,1]**2
			energy.append(dist1)
			dist2 = (all_paths[j][i,0]-20)**2 + (all_paths[j][i,1]-40)**2
			start.append(dist2)
		dist_energy.append(energy)
		dist_start.append(start)
	ms_energy = numpy.average(dist_energy, axis = 0)
	ms_start = numpy.average(dist_start, axis = 0)
	return ms_energy, ms_start

x0, x1, y0, y1 = -20, 50, -20, 50		#This sets up the data for the energy map in the graph
dx, dy = (x1 - x0) / 500, (y1 - y0) / 500
x_axis, y_axis = numpy.arange(x0,x1,dx), numpy.arange(y0,y1,dy)
data = numpy.zeros((len(x_axis), len(y_axis)))
for iy, y in enumerate(y_axis):
	for ix, x in enumerate(x_axis):
		data[iy, ix] = f((x, y))

pyplot.figure()
pyplot.subplot(221)		#This subplot plots the trajectories of the bacteria
pyplot.title('Trajectory of 20 bacteria')
im = pyplot.imshow(data, extent = (-30, 50, -20, 50), origin = 'lower', cmap = matplotlib.cm.gray)
pyplot.colorbar(im, orientation = 'vertical')
for i in range(20):
	pyplot.plot(all_paths[i][:,0], all_paths[i][:,1])
pyplot.xlabel('x Coordinate / microns')
pyplot.ylabel('y Coordinate / microns')
pyplot.subplot(222)		#This subplot plots the start and end points 
pyplot.title('Start and end points of bacteria')
im = pyplot.imshow(data, extent = (-10, 50, -10, 50), origin = 'lower', cmap = matplotlib.cm.gray)
pyplot.colorbar(im, orientation = 'vertical')
for i in range(20):
	start_end = numpy.array((all_paths[i][0,:], all_paths[i][-1,:]))
	pyplot.plot(start_end[:,0], start_end[:,1])
pyplot.xlabel('x Coordinate / microns')
pyplot.ylabel('y Coordinate / microns')
pyplot.subplot(212)		#This subplot plots the mean square displacement against time
pyplot.title('Mean square distance of bacteria')
p = find_ms((all_paths))
time = numpy.arange(0,100,0.1)
pyplot.plot(time, p[0], color = 'red', label = 'Mean square distance from energy origin')
pyplot.plot(time, p[1], color = 'blue', label = 'Mean square distance from start point')
pyplot.legend(loc=4)
pyplot.xlabel('Time / seconds')
pyplot.ylabel('Mean squared displacement / microns squared')
pyplot.tight_layout()
pyplot.show()


		
		
	
	
	