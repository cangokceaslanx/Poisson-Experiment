from scipy.stats import norm
from scipy.special import gamma 
from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#In the second part, datas are called as variable data
#( the 1st is n0 )
#( the 2nd is n1 )
data = [0.4,3.8,1.2,0.6,2.2,0.3,1.3,0.3,0.5,0.7,0.7,1.2,2.1,1.7,0.6,0.7,0.5,1.7,0.3,1.1,0.9,0.4,0.3,0.4,1.1,1,1.1,1.7,1.8,0.2,3,0.2,1.1,2.7,0.4,0.8,1.1,0.2,2.1,1.1,0.4,0.4,1.1,0.5,0.5,0.6,1.2,1.3,0.5,1.4,0.8,1.9,1.2,2.6,1,2.4,0.6,2.5,1.4,0.3,0.2,1,0.3,1.5,1.5,1.6,0.5,1.6,1.2,1.2,0.6,1.2,0.1,0.2,0.3,1.1,3.1,1,0.3,1.6,1,0.3,0.8,0.3,2.9,1.7,0.8,1,0.2,1.9,1.1,0.9,2.7,0.4,2.9,0.2,0.3,1,0.7,1]
#data = [4.2,5,1.8,2.8,2.5,1.6,1.6,0.8,1.2,1.4,1.9,3.3,3.8,2.3,1.3,1.2,2.2,2,1.4,2,1.3,0.7,0.7,1.5,2.1,2.1,2.8,3.5,2,3.2,3.2,1.3,3.8,3.1,1.2,1.9,1.3,2.3,3.2,1.5,0.8,1.5,1.6,1,1.1,1.8,2.5,1.8,1.9,2.2,2.7,3.1,3.8,3.6,3.4,3,3.1,3.9,1.7,0.5,1.2,1.3,1.8,3,3.1,2.1,2.1,2.8,2.4,1.8,1.8,1.3,0.3,0.5,1.4,4.2,4.1,1.3,1.9,2.6,1.3,1.1,1.1,3.2,4.6,2.5,1.8,1.2,2.1,3,2,3.6,3.1,3.3,3.1,0.5,1.3,1.7,1.7]

def poissonFitting(a,mu):
    return (mu**a/gamma(a+1))*np.exp(-mu)
data.sort()
n, bins, patches=plt.hist(data, bins=10,normed=True,color="#ff0000")
mean = sum(data)/len(data)
x=np.linspace(0,6,400)
plt.plot(x,poissonFitting(x,mean),"-",linewidth=4,label="Poisson Fit") #This is the poisson fit
plt.xlabel("Bin ranges")
plt.ylabel("Number distribution of Counts") 
title = "Poisson fit over the second data (1s)"
plt.title(title)
plt.grid(True)
plt.legend()
plt.show()
def ChiFitting_poisson(bincenters, binvalues):
    totalChiFitting=0
    width=bins[1]-bins[0]
    amp=width*100
    for i in range(len(bincenters)):
        totalChiFitting+=(binvalues[i]*amp-poissonFitting(bincenters[i],mean)*amp)**2
    
    return totalChiFitting/( mean * (len(bincenters) - 1) )
    
print("Poisson ChiFitting=",ChiFitting_poisson(bins,y))
print("Poisson mu = %.3f, sigma = %.3f" % (mean,sqrt(mean)))
