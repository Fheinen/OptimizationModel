# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:29:25 2015

@author: fh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 08:34:00 2014

@author: fh
"""

import os, sys, time

try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    myrank = comm.Get_rank()
except:
    print 'mpi4py is required for parallelization'

print sys.executable 

#import matplotlib.pyplot as plt
import numpy as np

from anypytoolsfh.abcutils import AnyPyProcess
from GlobalStrengthFactor import run_model, objfunc
app = AnyPyProcess()



import pyOptfh
from pyOptfh import SNOPT
#import gradientdemo
#from gradientdemo import SNOPT


opt_prob = pyOptfh.Optimization('Joint Strength Analysis2',objfunc)
opt_prob.addObj('f')

opt_prob.addVar('GlobalStrengthFactor','c',lower=0.1,upper=10.0,value=1.0)


optimizer = SNOPT(  )
optimizer.setOption('Major optimality tolerance',value= 10e-6)
optimizer.setOption('Major feasibility tolerance',value= 10e-6)


optimizer(opt_prob, sens_type='fd', disp_opts=True, sens_mode='pgc')
print opt_prob

#optimizer(opt_prob,store_hst=True) , sens_mode='pgc'
#print opt_prob.solution(0)

opt_prob.write2file(outfile='', disp_sols=False, solutions=[])
print opt_prob._solutions[0]

