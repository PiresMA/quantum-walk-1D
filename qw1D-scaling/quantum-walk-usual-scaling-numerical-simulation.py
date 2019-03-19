#!/usr/bin/python

# Quantum Walk:  numerical approach based on table 1 of [1]
#
# References:
# [1] Kendon, Vivien M. "A random walk approach to quantum algorithms." Philos. Trans. Royal Soc. A. 364.1849 (2006): 3407-3422.
# [2] J.Dingerink: Quantum walks of an atom in an optical lattice, 2016 https://esc.fnwi.uva.nl/thesis/centraal/files/f1472237352.pdf
# [3] Portugal, Renato. Quantum walks and search algorithms. Springer Science & Business Media, 2013.

import math as mt
import numpy   as   np
from matplotlib import pylab as plt
import sys


vecns = [50,100,200,400,800]
arg1 = int(sys.argv[1] )    # number of steps
nsteps = vecns[arg1]

print sys.argv[0]   #file name
print nsteps



# Main part: see line 120



# quantum coin
theta_degree = 45
c11 =  np.cos(mt.radians(theta_degree))
c12 =  np.sin(mt.radians(theta_degree))
c21 =  np.sin(mt.radians(theta_degree))
c22 = -np.cos(mt.radians(theta_degree))


# One Step:  1) Hadamard coin is flipped; 2) shift operator works on the state
def psiStep( psiInput ):
 psiOutput  =  [ ]
 for elem in psiInput:
   if elem[2]   ==  0:  # if the Hadamard coin state is \0>
    psiOutput.append([ c11*elem[0], elem[1]-1, 0]) # shift operator: S-
    psiOutput.append([ c12*elem[0], elem[1]+1, 1]) # shift operator: S+
   elif elem[2] == 1:   # if the Hadamard coin state is \1>
    psiOutput.append([ c21*elem[0], elem[1]-1, 0]) # shift operator: S-
    psiOutput.append([ c22*elem[0], elem[1]+1, 1]) # shift operator: S+   
 return(psiOutput)


# To remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


# Putting terms together: states with the same Position and Coin state
def psiGathering( psiInput ):
 psiPC = []   # PC = Position and Coin state
 for elem in psiInput:
  psiPC.append( [elem[1],elem[2]] )
  
 psiPC2 = Remove(psiPC) #Removing duplicate elements of the full psi

 vecamplit = []  # For amplitude
 for elem2 in psiPC2:
  amplit = 0
  label  = -1
  for elem in psiPC:
   label = label + 1
   if elem2 == elem:
    amplit = amplit + psiInput[label][0] # Sum probabiliy amplitudes 
  vecamplit.append(amplit)

 psiOutput = []
 for i in range(len(psiPC2)):
  psiOutput.append( [ vecamplit[i], psiPC2[i][0], psiPC2[i][1] ] )

 return psiOutput



# Putting terms together to compute the probability distribution
def probabilityDistribution( psiInput ):
 pisP = []
 for elem in psi:
  pisP.append( elem[1] )
  
 #Removing duplicate elements of the full psi
 pisP2 = []
 for i in pisP:
  if i not in pisP2:
   pisP2.append(i) 

 vecamplit = []   # For full amplitude
 for elem2 in pisP2:
  amplit = 0
  label  = -1
  for elem in pisP:
   label = label + 1
   if elem2 == elem:
    amplit = amplit + abs( psiInput[label][0] )**2 # Sum probabiliy amplitudes 
  vecamplit.append(amplit)
  
 # Get the occupancy probability distribution
 posProb = []
 for i in range(len(pisP2)):  
  posProb.append( [ pisP2[i], vecamplit[i], ] ) # output: [position,probability]

 return posProb 













#####  MAIN PART 

#print("Notation:  psi = [pre-factor(coefficient), position(walker), spin(coin)]\n") 


#####  time  = 0
#psi0asymmetric = [[1, 0, 1]]    # Ao=1  Bo=0
psi0symmetric  = [ [1/mt.sqrt(2), 0,1], [ 1j/mt.sqrt(2), 0, 0] ]

psi = psi0symmetric 

##### dynamics 
for t in  np.arange(1,nsteps,1):   
 psi = psiStep( psi )
 psi = psiGathering( psi )


# Get the occupancy probability distribution
vecamplitNumer = probabilityDistribution(psi)


# only sites with  non-zero occupancy probability
posProb = []
for i in np.arange(0,len(vecamplitNumer),1):  
 if vecamplitNumer[i][1]>0:
  posProb.append( [vecamplitNumer[i][0],vecamplitNumer[i][1]] )


if nsteps<100:   
 nameOut =  "qw-pos-prob-numeric-nsteps0{0}.txt".format(str(nsteps))
else:
 nameOut =  "qw-pos-prob-numeric-nsteps{0}.txt".format(str(nsteps))

np.savetxt(nameOut, posProb )


