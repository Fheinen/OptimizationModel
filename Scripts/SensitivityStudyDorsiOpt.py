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
delta = 25*5e-5
AnyBody = 0.0004748338
Factor = 2000 

opt_prob = pyOpt.Optimization('Joint Strength Analysis2',objfunc)
opt_prob.addObj('f')

opt_prob.addVar('tarmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('edlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('ehlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('tarmax','c',lower=0.7,upper=1.6,value=1.2)
opt_prob.addVar('edlrmax','c',lower=0.7,upper=1.6,value=1.2)
opt_prob.addVar('ehlrmax','c',lower=0.7,upper=1.6,value=1.2)
opt_prob.addVar('LocalStrengthFactorDorsiFlexors','c',lower=0.1,upper=10,value=1)
opt_prob.addVar('x1','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x2','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x3','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x4','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x5','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x6','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x7','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x8','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x9','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x10','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x11','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x12','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x13','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x14','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x15','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x16','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x17','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x18','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x19','c',lower=0.0,upper=np.inf,value=0)
opt_prob.addVar('x20','c',lower=0.0,upper=np.inf,value=0)

opt_prob.addCon('g1','i', lower=0.1,upper=np.inf)
opt_prob.addCon('g2','i', lower=0.1,upper=np.inf)
opt_prob.addCon('g3','i', lower=0.1,upper=np.inf)
opt_prob.addCon('g4','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g5','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g6','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g7','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g8','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g9','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g10','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g11','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g12','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g13','i', lower=Factor*(AnyBody+delta),upper=np.inf)
opt_prob.addCon('g14','i', lower=-np.inf,upper=(0.2995546-delta)*Factor)
opt_prob.addCon('g15','i', lower=-np.inf,upper=(0.2503117-delta)*Factor)
opt_prob.addCon('g16','i', lower=-np.inf,upper=(0.176632-delta)*Factor)
opt_prob.addCon('g17','i', lower=-np.inf,upper=(0.4342194-delta)*Factor)
opt_prob.addCon('g18','i', lower=-np.inf,upper=(0.3532385-delta)*Factor)
opt_prob.addCon('g19','i', lower=-np.inf,upper=(0.2421254-delta)*Factor)
opt_prob.addCon('g20','i', lower=-np.inf,upper=(0.2320532-delta)*Factor)
opt_prob.addCon('g21','i', lower=-np.inf,upper=(0.3413624-delta)*Factor)
opt_prob.addCon('g22','i', lower=-np.inf,upper=(0.2766059-delta)*Factor)
opt_prob.addCon('g23','i', lower=-np.inf,upper=(0.2257777-delta)*Factor)

optimizer = SNOPT(  )
optimizer.setOption('Major optimality tolerance',value= 10e-6)
optimizer.setOption('Major feasibility tolerance',value= 10e-6)

print opt_prob
optimizer(opt_prob, store_hst=True, sens_type='fd', disp_opts=True, sens_mode ='pgc')


opt_prob.write2file(outfile='', disp_sols=False, solutions=[])
print opt_prob._solutions[0]

