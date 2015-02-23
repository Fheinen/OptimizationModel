# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 12:55:01 2015

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

import matplotlib.pyplot as plt
import numpy as np

from anypytools.abcutils import AnyPyProcess
from SensitivityStudyPlantar import run_model, objfunc
app = AnyPyProcess()

import pyOptfh
from pyOptfh import SNOPT


opt_prob = pyOptfh.Optimization('Joint Strength Analysis2',objfunc)
opt_prob.addObj('f')

opt_prob.addVar('smrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('smrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('slrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('slrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('glrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('glrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('gmrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('gmrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('prmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('prmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('fhlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('fhlrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('LocalStrengthFactorPlantarFlexors','c',lower=0.1,upper=10,value=1)
opt_prob.addVar('x1','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x2','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x3','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x4','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x5','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x6','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x7','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x8','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x9','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x10','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x11','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x12','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x13','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x14','c',lower=0.0005,upper=5,value=0.3)

optimizer = SNOPT(  )
optimizer.setOption('Major optimality tolerance',value= 10e-6)
optimizer.setOption('Major feasibility tolerance',value= 10e-6)


optimizer(opt_prob, sens_type='fd,function', disp_opts=True, sens_mode='pgc')
print opt_prob

opt_prob.write2file(outfile='', disp_sols=False, solutions=[])
print opt_prob._solutions[0]

