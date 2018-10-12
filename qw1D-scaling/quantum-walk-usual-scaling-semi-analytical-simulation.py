#!/usr/bin/python

# Quantum Walk: semi-analytical approach based on the recursive method described in page 27 of [3]
# References:
# [1] Kendon, Vivien M. "A random walk approach to quantum algorithms." Philos. Trans. Royal Soc. A. 364.1849 (2006): 3407-3422.
# [2] J.Dingerink: Quantum walks of an atom in an optical lattice, 2016 https://esc.fnwi.uva.nl/thesis/centraal/files/f1472237352.pdf
# [3] Portugal, Renato. Quantum walks and search algorithms. Springer Science & Business Media, 2013.


import cmath as cmt
import math as mt
import numpy as np
from matplotlib import pylab as plt
import sys

vecns = [50,100,200,400,800]
arg1 = int(sys.argv[1] )    # number of steps
nsteps = vecns[arg1]

print sys.argv[0]   #file name
print nsteps



# Main part: see line 60



# Putting terms together to compute the probability distribution
def recursive_A_B(vecA, vecB):
 vecA2   = []
 vecB2   = []

 # Left boundary
 vecA2.append( 0 ) 
 vecB2.append( 0 ) 

 # Other positions
 for i in  np.arange(1,len(xpos)-1,1):    
   vecA2.append( (vecA[i-1] + vecB[i-1])/mt.sqrt(2) ) 
   vecB2.append( (vecA[i+1] - vecB[i+1])/mt.sqrt(2) ) 

 # Right boundary
 vecA2.append( 0 ) 
 vecB2.append( 0 ) 

 return vecA2,vecB2
 
 
 
 








# MAIN PART
npos   = 2*nsteps+1  # number of positions
xc     = nsteps      # central position = nsteps   #Index Start at 0

xpos = np.arange(-nsteps, nsteps+1, 1)   


#####  time  = 0
vecB     =  np.zeros(npos, dtype=np.complex_)    
vecA     = np.zeros(npos)
vecA[xc] =  1/mt.sqrt(2)
vecB[xc] = 1j/cmt.sqrt(2)   


##### Dynamics
for t in  np.arange(1,nsteps,1):
 vecA,vecB = recursive_A_B(vecA, vecB)

#print( np.around(np.array( vecA ),2) )
#print( np.around(np.array( vecB ),2) )


# Only sites with non-zero occupancy probability
vecpos     = [ ]
vecprob    = [ ]
posProb = [ ]
for i in  np.arange(0,len(xpos),1):
 prob =  abs(vecA[i])**2 +  abs(vecB[i])**2  
 if prob>0:
  vecpos.append(  xpos[i] )
  vecprob.append(  prob )
  posProb.append( [xpos[i],prob] )

if nsteps<100:   
 nameOut =  "qw-pos-prob-semi-analyt-nsteps0{0}.txt".format(str(nsteps))
else:
 nameOut =  "qw-pos-prob-semi-analyt-nsteps{0}.txt".format(str(nsteps))

np.savetxt(nameOut, posProb )


