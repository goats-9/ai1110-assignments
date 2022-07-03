#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

bv = np.loadtxt('ber_new.dat', dtype='double')
nv = np.loadtxt('gau.dat', dtype='double')

def emp_err(g):
    ral_file = "ral_"+str(int(g)).zfill(2)+".dat"
    rv = np.loadtxt(ral_file, dtype='double')
    sig = rv*bv + nv
    n0 = np.count_nonzero(bv > 0)
    e0 = np.count_nonzero((sig < 0) & (bv > 0)) 
    return e0/n0

emp_err_vec = scipy.vectorize(emp_err, otypes=['double'])

def expected_err(g):
    return 0.5*(1 - ((g/(g+2))**(0.5)))

expected_err_vec = scipy.vectorize(expected_err, otypes=['double'])

maxrange=100
G = np.linspace(1,10,10)
x = np.linspace(0,10,1000)
plt.plot(G, emp_err_vec(G), '.')
plt.plot(x, expected_err_vec(x))
plt.grid() #creating the grid
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/7_1.png')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
