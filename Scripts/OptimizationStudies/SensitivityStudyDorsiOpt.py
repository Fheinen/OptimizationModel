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

#try:
#    from mpi4py import MPI
#    comm = MPI.COMM_WORLD
#    myrank = comm.Get_rank()
#except:
#    print 'mpi4py is required for parallelization'

print sys.executable 

import matplotlib.pyplot as plt
import numpy as np

from anypytools.abcutils import AnyPyProcess
from SensitivityStudyDorsi import run_model, objfunc
app = AnyPyProcess()

import pyOpt
from pyOpt import SNOPT


opt_prob = pyOpt.Optimization('Joint Strength Analysis2',objfunc)
opt_prob.addObj('f')

opt_prob.addVar('tarmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('tarmax','c',lower=0.7,upper=1.6,value=1.2)
opt_prob.addVar('edlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('edlrmax','c',lower=0.7,upper=1.6,value=1.2)
opt_prob.addVar('ehlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('ehlrmax','c',lower=0.7,upper=1.6,value=1.2)
opt_prob.addVar('LocalStrengthFactorDorsiFlexors','c',lower=0.1,upper=10,value=1)
opt_prob.addVar('x1','c',lower=0.0005,upper=0.2995546,value=0.1)
opt_prob.addVar('x2','c',lower=0.0005,upper=0.2503117,value=0.1)
opt_prob.addVar('x3','c',lower=0.0005,upper=0.176632,value=0.1)
opt_prob.addVar('x4','c',lower=0.0005,upper=0.4342194,value=0.1)
opt_prob.addVar('x5','c',lower=0.0005,upper=0.3532385,value=0.1)
opt_prob.addVar('x6','c',lower=0.0005,upper=0.2421254,value=0.1)
opt_prob.addVar('x7','c',lower=0.0005,upper=0.2320532,value=0.1)
opt_prob.addVar('x8','c',lower=0.0005,upper=0.3413624,value=0.1)
opt_prob.addVar('x9','c',lower=0.0005,upper=0.2766059,value=0.1)
opt_prob.addVar('x10','c',lower=0.0005,upper=0.2257777,value=0.1)


optimizer = SNOPT(  )
optimizer.setOption('Major optimality tolerance',value= 10e-6)
optimizer.setOption('Major feasibility tolerance',value= 10e-6)


optimizer(opt_prob, sens_type='fd', disp_opts=True, sens_mode ='pgc')
print opt_prob

opt_prob.write2file(outfile='', disp_sols=False, solutions=[])
print opt_prob._solutions[0]

