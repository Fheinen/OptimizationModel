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
from SensitivityStudy import run_model, objfunc, gradfunc
app = AnyPyProcess()



import pyOptfh
from pyOptfh import SNOPT
#import gradientdemo
#from gradientdemo import SNOPT


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
opt_prob.addVar('fdlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('fdlrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('fhlrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('fhlrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('tplrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('tplrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('tpmrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('tpmrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('bfclrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('bfclrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('bfcbrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('bfcbrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('stdrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('stdrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('smbrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('smbrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('vlirmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('vlirmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('vlsrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('vlsrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('vmirmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('vmirmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('vmmrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('vmmrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('vmsrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('vmsrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('virmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('virmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('rfrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('rfrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('tflrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('tflrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('gmsrmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('gmsrmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('gmirmin','c',lower=0.1,upper=0.8,value=0.5)
opt_prob.addVar('gmirmax','c',lower=1.1,upper=1.8,value=1.2)
opt_prob.addVar('LocalStrengthFactorPlantarFlexors','c',lower=0.1,upper=2.0,value=1.0)
opt_prob.addVar('LocalStrengthFactorKneeFlexors','c',lower=0.1,upper=2.0,value=1.0)
opt_prob.addVar('LocalStrengthFactorKneeExtensor','c',lower=0.1,upper=2.0,value=1.0)
opt_prob.addVar('LocalStrengthFactorHipExtensor','c',lower=0.1,upper=2.0,value=1.0)
opt_prob.addVar('LovalStrengthFactorHipFlexor','c',lower=0.1,upper=2.0,value=1.0)
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
opt_prob.addVar('x15','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x16','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x17','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x18','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x19','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x20','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x21','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x22','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x23','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x24','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x25','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x26','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x27','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x28','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x29','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x30','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x31','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x32','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x33','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x34','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x35','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x36','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x37','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x38','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x39','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x40','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x41','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x42','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x43','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x44','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x45','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x46','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x47','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x48','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x49','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x50','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x51','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x52','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x53','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x54','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x55','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x56','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x57','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x58','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x59','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x60','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x61','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x62','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x63','c',lower=0.0005,upper=5,value=0.3)
opt_prob.addVar('x64','c',lower=0.0005,upper=5,value=0.3)




optimizer = SNOPT(  )
optimizer.setOption('Major optimality tolerance',value= 10e-6)
optimizer.setOption('Major feasibility tolerance',value= 10e-6)


optimizer(opt_prob, sens_type='fd,function', disp_opts=True)
print opt_prob

#optimizer(opt_prob,store_hst=True) , sens_mode='pgc'
#print opt_prob.solution(0)

opt_prob.write2file(outfile='', disp_sols=False, solutions=[])
print opt_prob._solutions[0]

