#!/usr/bin/python
from numpy import *
import matplotlib.pyplot as plt
import pylab as pl

f_essi=open("result_essi.txt","r")
f_theory=open("result_theory.txt","r")

result_essi=linspace(0,0,11)
result_theory=linspace(0,0,11)

for i in range(11):
	result_essi[i] =f_essi.readline()

for i in range(11):
	result_theory[i] =f_theory.readline()

nu=linspace(0.0,0.45,10)
nu=append(nu, 0.49)

error = abs(result_essi-result_theory)/result_theory
error = error * 100
print error
fig=pl.figure(1)
plot=fig.add_subplot(111)
plot.plot(nu,error)
plot.tick_params(axis='both', which='major', labelsize=24)
plot.tick_params(axis='both', which='minor', labelsize=17)

plt.xlabel('Poisson\'s ratio',fontsize=24)
plt.ylabel('Error / (%)',fontsize=24)
# pl.show()

fig.savefig('error2d.png',bbox_inches='tight')

