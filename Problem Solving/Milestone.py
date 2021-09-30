from __future__ import division
import numpy
import matplotlib.pyplot as plt
from scipy.integrate import quad

#Import data
data = numpy.loadtxt("C:/Users/Joseph/Documents/University/Problem_solving/sn_data.txt", usecols=(1,2,3))#"/Users/123pye123/Documents/University/Problem_solving/sn_data.txt"

#Define low redshift data
z1, m1, err1 = data[42:,0], data[42:,1], data[42:,2]

#Define all redshift data
z2, m2, err2 = data[:,0], data[:,1], data[:,2]

#Define constants
H0 = 75
c = 3 * 10**5
m0 = -20.45

#Finds comoving distance for low redshift
def CM(z):	
    return (c * z / H0)**2
	
#Calculates luminosity from given observed magnitude and redshift
def calc_L(m,z):
    return (10**((m0 - m) / 2.5) * 4 * numpy.pi * CM(z) * (1 + z)**2)
    
#Calculate an L value for all low redshift supernovae
L1 = []
for i in range(len(m1)):
    L1.append(calc_L(m1[i], z1[i]))
	
Lmax, Lmin, Lavg = max(L1), min(L1), numpy.mean(L1)
omegamax, omegamin = 0, 1

Lsteps = len(m1)
omegasteps = len(m2)
Lpeakguess = numpy.arange(Lmin, Lmax, (Lmax - Lmin)/Lsteps)
omegaguess = numpy.arange(omegamin, omegamax, (omegamax - omegamin)/omegasteps)

#Finds the Chi2 sum for a model value of L
def chi2L(L):
    X2 = 0
    for i in range(Lsteps):
	X2 = X2 + (m1[i] - (m0 - 2.5 * numpy.log10(L / (4 * numpy.pi * CM(z1[i]) * (1+z1[i])**2))))**2 / err1[i]**2
    return X2

#Creates an empty array for the Chi**2 values for different L values
chi2L_vals = []

#Populates chi**2 array for L
for i in range(Lsteps):
    chi2L_vals.append(chi2L(Lpeakguess[i]))

#Find the minimum chi**2 value and its corresponding Lpeakguess value, which is Lpeak
chi2Lmin = min(chi2L_vals)
index = chi2L_vals.index(chi2Lmin)
Lpeak = Lpeakguess[index]
print "Lpeak =", Lpeak

def CM2(Z, omega):
    f = lambda z: c / H0 * ((1 - omega)*((1 + z)**3)+1)**0.5
    return quad(f,0,Z)[0]

def chi2omega(omega):
    X2 = 0
    for i in range(omegasteps):
        X2 = X2 + (m2[i] - (m0 - 2.5 * numpy.log10( Lpeak / (4 * numpy.pi * CM2(z2[i], omega) * (1 + z2[i])**2))))**2 / err2[i]**2
 
chi2omega_vals = []       
for i in range(omegasteps):
    chi2omega_vals.append(chi2omega(omegaguess[i]))
    
print chi2omega_vals

plt.figure()
plt.subplot(211)
plt.plot(Lpeakguess, chi2L_vals)
plt.show()
		

