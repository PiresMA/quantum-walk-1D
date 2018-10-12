
import math as mt
import numpy   as   np
from matplotlib import pylab as plt

# line 30: part I
# line 75: part II


# standard deviation of the probability distribution for symmetric QW
def QWsd(dataIN):
 #If the probability distribution of the QW is symmetric the mean=0
 n=len(dataIN)
 sum1=0 
 for i in range(n):
  x    = dataIN[i][0]
  prob = dataIN[i][1]
  sum1 = sum1 + (x**2)*prob   # Eq 3.24 of R.P.
    
 sd=mt.sqrt(sum1)
 
 return sd



vecns = [50,100,200,400,800]



### PART I
vecsd = [ ]
for nsteps in vecns:
 if nsteps<100:   
  nameOut =  "qw-pos-prob-numeric-nsteps0{0}.txt".format(str(nsteps))
 else:
  nameOut =  "qw-pos-prob-numeric-nsteps{0}.txt".format(str(nsteps))
 
 data = np.loadtxt(fname = nameOut,  ndmin=2, usecols=(0,1) )
 vecsd.append( QWsd(data) )



#Taking the logarithm to base 10 
logA = np.log10(vecns)
logB = np.log10(vecsd)

#Fit on the log data
coef = np.polyfit(logA, logB, 1)  #polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
polynomial = np.poly1d(coef)
print polynomial
ys = polynomial(logA)


plt.plot(logA,logB, 'ro',markerfacecolor='red', markersize=12)
plt.plot(logA, ys, color='red', linestyle='dashed')
plt.text(1.7, 2.7, "Fit:", fontsize=15)
plt.text(1.8, 2.7, polynomial, fontsize=15)
plt.text(1.7, 2.5, r'$\sigma^2 \sim t^\alpha $', fontsize=20)
plt.text(1.7, 2.3, r'$\alpha = 1.006 $', fontsize=20)
plt.xlabel(r'$\log(t)  \quad\quad (t = n_{steps})$')
plt.ylabel(r'$\log(\sigma^2)$')
plt.savefig("qw-fit-sd-numeric.png")












### PART II
vecsd = [ ]
for nsteps in vecns:
 if nsteps<100:   
  nameOut =  "qw-pos-prob-semi-analyt-nsteps0{0}.txt".format(str(nsteps))
 else:
  nameOut =  "qw-pos-prob-semi-analyt-nsteps{0}.txt".format(str(nsteps))
 
 data = np.loadtxt(fname = nameOut,  ndmin=2, usecols=(0,1) )
 vecsd.append( QWsd(data) )
 #print 'sd: ', QWsd(data)


#Taking the logarithm to base 10 
logA = np.log10(vecns)
logB = np.log10(vecsd)

#Fit on the log data
coef = np.polyfit(logA, logB, 1)  #polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
polynomial = np.poly1d(coef)
print polynomial
ys = polynomial(logA)


plt.plot(logA,logB, 'bo',markerfacecolor='blue', markersize=12)
plt.plot(logA, ys, color='blue', linestyle='dashed')
plt.text(1.7, 2.7, "Fit:", fontsize=15)
plt.text(1.8, 2.7, polynomial, fontsize=15)
plt.text(1.7, 2.5, r'$\sigma^2 \sim t^\alpha $', fontsize=20)
plt.text(1.7, 2.3, r'$\alpha = 1.006 $', fontsize=20)
plt.xlabel(r'$\log(t)  \quad\quad (t = n_{steps})$')
plt.ylabel(r'$\log(\sigma^2)$')
plt.savefig("qw-fit-sd-semi-analyt.png")

