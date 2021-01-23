#Code by GVV Sharma
#August 8, 2020
#released under GNU GPL
#Drawing a circle given two points
#and the line passing through the centre

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA



#if using termux
import subprocess
import shlex
#end if

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ


#Input parameters
O = 0.1*np.array(([7,13]))
P = np.array(([2,-2]))
Q = np.array(([3,4]))
f = -52/5
r = np.sqrt(LA.norm(O)**2-f)
m = np.array(([1,-1]))
A = np.array(([2,0]))
k1 = 2
k2 = -2
##Generating all lines
x_AB = line_dir_pt(m,A,k1,k2)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$x+y=2$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')


#Labeling the coordinates
tri_coords = np.vstack((P,Q,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/circex/CircOr.pdf')
#plt.savefig('./figs/circex/CircOr.png')
#subprocess.run(shlex.split("termux-open ./figs/circex/CircOr.pdf"))
#else
plt.show()








