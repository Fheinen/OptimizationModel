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

nDesVar = 13
np.save('nDesVar',nDesVar)

def run_model(DesignVars):
    ''' Ruturns the x,y potions for the tip of the A frame '''
    folder = 'C:/Users/fh/Documents/AAU/PhD-AAU/PhD projekt/OptimeringsArtikle/Scripts/OptimizationStudies'    
    app = AnyPyProcess(anybodycon_path = 'C:/Program Files (x86)/AnyBody Technology/AnyBody.6.0/AnyBodyCon.exe', ignore_errors = ['ERROR(OBJ.MCH.MUS6)'])
    macro = [['load "Optimization.main.any"',
        'classoperation Main.DesignVars.sm_rmin "Set Value" --value={:12f}'.format(DesignVars[0]),
        'classoperation Main.DesignVars.sm_rmax "Set Value" --value={:12f}'.format( DesignVars[1]),
        'classoperation Main.DesignVars.sl_rmin "Set Value" --value={:12f}'.format(DesignVars[2]),
        'classoperation Main.DesignVars.sl_rmax "Set Value" --value={:12f}'.format( DesignVars[3]),
        'classoperation Main.DesignVars.gl_rmin "Set Value" --value={:12f}'.format(DesignVars[4]),
        'classoperation Main.DesignVars.gl_rmax "Set Value" --value={:12f}'.format( DesignVars[5]),
        'classoperation Main.DesignVars.gm_rmin "Set Value" --value={:12f}'.format(DesignVars[6]),
        'classoperation Main.DesignVars.gm_rmax "Set Value" --value={:12f}'.format( DesignVars[7]),
        'classoperation Main.DesignVars.fhl_rmin "Set Value" --value={:12f}'.format(DesignVars[8]),
        'classoperation Main.DesignVars.fhl_rmax "Set Value" --value={:12f}'.format( DesignVars[9]),
        'classoperation Main.DesignVars.pr_rmin "Set Value" --value={:12f}'.format(DesignVars[10]),
        'classoperation Main.DesignVars.pr_rmax "Set Value" --value={:12f}'.format( DesignVars[11]),
        'classoperation Main.DesignVars.LocalStrengthFactorPlantarFlexors "Set Value" --value={:12f}'.format( DesignVars[12]),
        'operation Main.RunApplication1',
        'run',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusLateralis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusMedialis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.PeroneusLongus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.PeroneusLongus2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.PeroneusLongus3Par.Lt0 "Dump"',
        'operation Main.RunApplication2',
        'run',
        'classoperation Main.Studies.ParameterStudies.PlantarFlexorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'exit']]
       
    output = app.start_macro(macro, folderlist = [folder] )[0]
    
    return (output)
    
EDTuple = ExpData()
EDIsomDF = EDTuple[0]
EDIsomPF = EDTuple[1]

NormExpDataIsomPF = EDIsomPF/np.max(EDIsomPF)

def objfunc(x):
    f = 0
    g = 0
    fail = 0
    
    output = run_model(x)
    JointStrengthIsomPF = output['Main.Studies.ParameterStudies.PlantarFlexorMuscles.IsometricStrength.Output.Strength.Val']
    pf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis3Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusMedialis1Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.PeroneusLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.PeroneusLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.PeroneusLongus3Par.Lt0']])
    
    np.save('PlanFlex',pf)

#    print TibialisAnt3
    print JointStrengthIsomPF
    print x
    if JointStrengthIsomPF is None:
        fail = 1
    else:
        Nx = len(x)-len(pf)
        num = range(Nx,len(x),1)
        np.save('num',num)
        # Objective: 
        Lt0Pen1 = np.array(10.0*np.sum(((x[num[0]]-pf[0])**2)+((x[num[1]]-pf[1])**2)+((x[num[2]]-pf[2])**2)+((x[num[3]]-pf[3])**2)+((x[num[4]]-pf[4])**2)+((x[num[5]]-pf[5])**2)+((x[num[6]]-pf[6])**2)+((x[num[7]]-pf[7])**2)+((x[num[8]]-pf[8])**2)+((x[num[9]]-pf[9])**2)+((x[num[10]]-pf[10])**2)+((x[num[11]]-pf[11])**2)+((x[num[12]]-pf[12])**2)+((x[num[13]]-pf[13])**2)))
        NormStrengthIsomPF = JointStrengthIsomPF/np.max(EDIsomPF)

        f = np.sqrt(np.sum(np.sum(((NormExpDataIsomPF-NormStrengthIsomPF)**2)+Lt0Pen1)))
     
        print f
        print Lt0Pen1
        g = [0]
        
    return f, g, fail, 

def gradfunc(x,f,g):
    
    PlanFlex=np.load('PlanFlex.npy')
    num=np.load('num.npy')
    g_obj = [0.0]*66
    g_obj[0] = 10.0*2*(x[num[0]]-PlanFlex[0])
    g_obj[1] = 10.0*2*(x[num[1]]-PlanFlex[1])
    g_obj[2] = 10.0*2*(x[num[2]]-PlanFlex[2])
    g_obj[3] = 10.0*2*(x[num[3]]-PlanFlex[3])
    g_obj[4] = 10.0*2*(x[num[4]]-PlanFlex[4])
    g_obj[5] = 10.0*2*(x[num[5]]-PlanFlex[5])
    g_obj[6] = 10.0*2*(x[num[6]]-PlanFlex[6])
    g_obj[7] = 10.0*2*(x[num[7]]-PlanFlex[7])
    g_obj[8] = 10.0*2*(x[num[8]]-PlanFlex[8])
    g_obj[9] = 10.0*2*(x[num[9]]-PlanFlex[9])
    g_obj[10] = 10.0*2*(x[num[10]]-PlanFlex[10])
    g_obj[11] = 10.0*2*(x[num[11]]-PlanFlex[11])
    g_obj[12] = 10.0*2*(x[num[12]]-PlanFlex[12])
    g_obj[13] = 10.0*2*(x[num[13]]-PlanFlex[13])
  

    
    g_con = 0
    
    fail = 0
    return g_obj, g_con, fail
    
    