from __future__ import division
import numpy
import matplotlib.pyplot as plt

#Import data
data = numpy.loadtxt("C:\Users\Joseph\Documents\University\sn_data.txt", usecols=(1,2,3))

#Define low redshift data
z1, m1, err1 = data[42:,0], data[42:,1], data[42:,2]

#Define constants
H0 = 75
c = 3 * 10**5

#Create and populate comoving distance array
R0 = []
for i in range(len(z1)):
    R0.append(c * z1[i] / H0)
    
#Calculate observed flux from magnitude
fObs = []
for i in range(len(m1)):
    fObs.append(10**((-20.45-m1[i])/2.5))
    
print fObs