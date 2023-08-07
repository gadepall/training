#Code by GVV Sharma
#June 12, 2022
#released under GNU GPL
#https://www.gnu.org/licenses/gpl-3.0.en.html

#Drawing a pair of tangents to a conic

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/gadepall/github/training/math/codes/CoordGeo')        #path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

flag = 0

h = np.array([3,4]).reshape(-1,1)
V = np.array(([4,0],[0,9]))
Pt = np.array(([-1 - np.sqrt(5),1 - np.sqrt(5)],[2,-2]))
P1 = np.block([[Pt[:,0].reshape(-1,1)/LA.norm(Pt[:,0]),Pt[:,1].reshape(-1,1)/LA.norm(Pt[:,1])]])
u = np.array([0,0]).reshape(-1,1)
f = -36

#intermediate
gh = h.T@V@h+2*u.T@h+f 

#matrix of tangents
sigmat = (V@h+u)@(V@h+u).T-gh*V

#Spectral decomposition
D, P = LA.eig(sigmat)

u1 = np.array(([np.sqrt(np.abs(D[1])),np.sqrt(np.abs(D[0]))]))
u2 = np.array(([np.sqrt(np.abs(D[1])),-np.sqrt(np.abs(D[0]))]))

u1 = u1.reshape(-1,1)
u2 = u2.reshape(-1,1)

#direction vectors
m1 = P@u1
m2 = P@u2
#print(m1,m2)
# Converting 1D array to a 2D numpy array of incompatible shape will cause error
'''
m1= np.reshape(m1, (2, 1))
m2= np.reshape(m2, (2, 1))
'''
mu1 = -(m1.T@(V@h+u))/(m1.T@V@m1)
mu2 = -(m2.T@(V@h+u))/(m2.T@V@m2)
#print(mu1,mu2)
x1 = h + mu1*m1
x2 = h + mu2*m2

#print(x1,x2)
#print(sigmat)
#print(D,-216*(1+np.sqrt(5)),216*(-1+np.sqrt(5)))
a = np.sqrt(0.5)
b = np.sqrt(1 + 1/np.sqrt(5))
c = np.sqrt(1 - 1/np.sqrt(5))
Q = a*np.array(([-b,-c],[c,-b]))
print(P,P1,Q)
#print(D)

#print(sigmat, P@np.diag(D)@P.T)
#print( P1@P1.T)

if flag==1:
    
    #Standard ellipse
    a = 2
    b = 1
    x = ellipse_gen(a,b)
    
    #Vertices
    A1 = np.array([a,0]).reshape(-1,1)
    A2 = -A1
    B1 = np.array([0,b]).reshape(-1,1)
    B2 = -B1
    
    #Plotting the ellipse
    plt.plot(x[0,:],x[1,:],label='Standard Ellipse')
    
    #Labeling the coordinates
    ellipse_coords = np.block([[A1,A2,B1,B2]])
    plt.scatter(ellipse_coords[0,:], ellipse_coords[1,:])
    vert_labels = ['$A_1$','$A_2$','$B_1$', '$B_2$']
    for i, txt in enumerate(vert_labels):
        plt.annotate(txt, # this is the text
                     (ellipse_coords[0,i], ellipse_coords[1,i]), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc='best')
    plt.grid() # minor
    plt.axis('equal')
    
    #if using termux
    #plt.savefig('./figs/ellipse.pdf')
    plt.savefig('/home/gadepall/github/training/math/figs/tangent.png')
    
    #plt.savefig('./figs/ellipse.png')
    #subprocess.run(shlex.split("termux-open ./figs/ellipse.pdf"))
    #else
    plt.show()
