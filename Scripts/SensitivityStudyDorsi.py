# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 12:57:59 2015

@author: fh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 08:28:47 2014

@author: fh
"""


import matplotlib.pyplot as plt
import numpy as np

from anypytools.abcutils import AnyPyProcess
app = AnyPyProcess()

from anypytools.abcutils import AnyPyProcess 
 
from ExperimentalData import ExpData

#nDesVar = 7
#np.save('nDesVar',nDesVar)

def run_model(DesignVars):
    ''' Ruturns the x,y potions for the tip of the A frame '''
    folder = 'C:\Users\fh\Documents\GitHub\OptimizationModel\Scripts\OptimizationStudies'    
    app = AnyPyProcess(anybodycon_path = 'C:\Program Files (x86)\AnyBody Technology\AnyBody.6.0/AnyBodyCon.exe', ignore_errors = ['ERROR(OBJ.MCH.MUS6)'])
    macro = [['load "Optimization.main.any"',
        'classoperation Main.DesignVars.ta_rmin "Set Value" --value={:12f}'.format(DesignVars[0]),
        'classoperation Main.DesignVars.edl_rmin "Set Value" --value={:12f}'.format(DesignVars[1]),
        'classoperation Main.DesignVars.ehl_rmin "Set Value" --value={:12f}'.format(DesignVars[2]),
        'classoperation Main.DesignVars.ta_rmax "Set Value" --value={:12f}'.format( DesignVars[3]),
        'classoperation Main.DesignVars.edl_rmax "Set Value" --value={:12f}'.format( DesignVars[4]),
        'classoperation Main.DesignVars.ehl_rmax "Set Value" --value={:12f}'.format( DesignVars[5]),
        'classoperation Main.DesignVars.LocalStrengthFactorDorsiFlexors "Set Value" --value={:12f}'.format( DesignVars[6]),
        'operation Main.RunApplication1',
        'run',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus4Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus3Par.Lt0 "Dump"',
        'operation Main.RunApplication2',
        'run',
        'classoperation Main.DesignVars.LocalStrengthFactorDorsiFlexors "Dump"',
        'classoperation Main.Studies.ParameterStudies.DorsiFlexorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'exit']]
       
    output = app.start_macro(macro, folderlist = [folder] )[0]
    np.save('Log',DesignVars)
    return (output)
    
EDTuple = ExpData()
EDIsomDF = EDTuple[0]
#EDIsomPF = EDTuple[1]

NormExpDataIsomDF = EDIsomDF/np.max(EDIsomDF)

def objfunc(x):
    f = 0
    g = 0
    fail = 0
    
    output = run_model(x)
    StrengthFactor = output['Main.DesignVars.LocalStrengthFactorDorsiFlexors']
    JointStrengthIsomDF = output['Main.Studies.ParameterStudies.DorsiFlexorMuscles.IsometricStrength.Output.Strength.Val']
    pf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus3Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus1Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus3Par.Lt0']])
    
    np.save('PlanFlex',pf)
    Nx = len(x)-len(pf)
    num = range(Nx,len(x),1)
    np.save('num',num)
    c = 10.0
    Lt0Pen = [0.0]*len(num)
    
    for i in range(len(num)):
        Lt0Pen[i] = np.sum((c*x[num[i]])+(0.5*(x[num[i]])**2))
    
    Lt0Pen2 = np.sum(Lt0Pen)
#    print TibialisAnt3
    print JointStrengthIsomDF
    print x
    if JointStrengthIsomDF is None:
        fail = 1
    else:

        # Objective: 
    
#        Lt0Pen1 = np.array(np.sum(((c*x[num[i]])+(0.5*(x[num[i]])**2))+((c*x[num[1]])+(0.5*(x[num[1]])**2))+((c*x[num[2]])+(0.5*(x[num[2]])**2))+((c*x[num[3]])+(0.5*(x[num[3]])**2))+((c*x[num[4]])+(0.5*(x[num[4]])**2))+((c*x[num[5]])+(0.5*(x[num[5]])**2))+((c*x[num[6]])+(0.5*(x[num[6]])**2))+((c*x[num[7]])+(0.5*(x[num[7]])**2))+((c*x[num[8]])+(0.5*(x[num[8]])**2))+((c*x[num[9]])+(0.5*(x[num[9]])**2))))
        
        NormStrengthIsomDF = JointStrengthIsomDF/np.max(EDIsomDF)

        f = np.sqrt(np.sum((NormExpDataIsomDF-NormStrengthIsomDF)**2))+Lt0Pen2
        
        lenDemo =(len(x)-np.size(StrengthFactor)-len(num))/2 #length of Rmin Rmax designvars
        g = [0.0]*(len(x)-np.size(StrengthFactor)-lenDemo) # Number of constraints needed
#        lenRminRmax = (len(x)-np.size(StrengthFactor))/2
#        g = [0.0]*(((len(x)-np.size(StrengthFactor))/2)+len(pf))
        
        count = 0 # initialization
        
            
        for i in range(lenDemo):
            #count = i
            g[count] = x[i+lenDemo]-x[i]
            # update count
            count = count + 1
            
        for i in range(len(num)/2):
            g[count] = 2000*pf[i]+x[num[i]]
           
            # update count
            count = count + 1
        
        for i in range(len(num)):
            g[count] = 2000*pf[i]-x[num[i]]
            
            # update count
            count = count +1
        
        
        
        
            
#        g[1] = pf[1]+x[num[1]]
#        g[2] = pf[2]+x[num[2]]
#        g[3] = pf[3]+x[num[3]]
#        g[4] = pf[4]+x[num[4]]
#        g[5] = pf[5]+x[num[5]]
#        g[6] = pf[6]+x[num[6]]
#        g[7] = pf[7]+x[num[7]]
#        g[8] = pf[8]+x[num[8]]
#        g[9] = pf[9]+x[num[9]]

        print f
#        print Lt0Pen2
        
        
    return f, g, fail, 

#def gradfunc(x,f,g):
#    
#    PlanFlex=np.load('PlanFlex.npy')
#    num=np.load('num.npy')
#    g_obj = [0.0]*66
#    g_obj[0] = 10.0*2*(x[num[0]]-PlanFlex[0])
#    g_obj[1] = 10.0*2*(x[num[1]]-PlanFlex[1])
#    g_obj[2] = 10.0*2*(x[num[2]]-PlanFlex[2])
#    g_obj[3] = 10.0*2*(x[num[3]]-PlanFlex[3])
#    g_obj[4] = 10.0*2*(x[num[4]]-PlanFlex[4])
#    g_obj[5] = 10.0*2*(x[num[5]]-PlanFlex[5])
#    g_obj[6] = 10.0*2*(x[num[6]]-PlanFlex[6])
#    g_obj[7] = 10.0*2*(x[num[7]]-PlanFlex[7])
#    g_obj[8] = 10.0*2*(x[num[8]]-PlanFlex[8])
#    g_obj[9] = 10.0*2*(x[num[9]]-PlanFlex[9])
#    g_obj[10] = 10.0*2*(x[num[10]]-PlanFlex[10])
#    g_obj[11] = 10.0*2*(x[num[11]]-PlanFlex[11])
#    g_obj[12] = 10.0*2*(x[num[12]]-PlanFlex[12])
#    g_obj[13] = 10.0*2*(x[num[13]]-PlanFlex[13])
#  
#
#    
#    g_con = 0
#    
#    fail = 0
#    return g_obj, g_con, fail
#    
    