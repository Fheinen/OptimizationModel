# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:24:54 2013

@author: RIGAUD Thomas
"""
from __future__ import division
from os import getcwd, path as op
from numpy import array, sqrt, mean, zeros
from anypytools.abcutils import AnyPyProcess
from scipy.optimize import fmin_l_bfgs_b

global iteration_counter
iteration_counter = 0


def setup_study(designvars):
    if designvars is None:
        designvars = array([0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.5, 1.2, 0.85])
    basepath = op.join( getcwd(), '..')
    app = AnyPyProcess(basepath, anybodycon_path = "F:\Program Files\AnyBody Technology\AnyBody.6.0\AnyBodyCon.exe",
						num_processes = 5, disp = False)
    loadmacro = 'load "Optimization.main.any"'
    macrocmds = ['operation RunApplication', 'run']
    inputs = [('Main.DesignVars.ta_rmin', designvars[0]),
              ('Main.DesignVars.ta_rmax', designvars[1]),
              ('Main.DesignVars.edl_rmin', designvars[2]),
              ('Main.DesignVars.edl_rmax', designvars[3]),
              ('Main.DesignVars.ehl_rmin', designvars[4]),
              ('Main.DesignVars.ehl_rmax', designvars[5]),
              ('Main.DesignVars.sm_rmin', designvars[6]),
              ('Main.DesignVars.sm_rmax', designvars[7]),
              ('Main.DesignVars.sl_rmin', designvars[8]),
              ('Main.DesignVars.sl_rmax', designvars[9]),
              ('Main.DesignVars.gl_rmin', designvars[10]),
              ('Main.DesignVars.gl_rmax', designvars[11]),
              ('Main.DesignVars.gm_rmin', designvars[12]),
              ('Main.DesignVars.gm_rmax', designvars[13]),
              ('Main.DesignVars.fdl_rmin', designvars[14]),
              ('Main.DesignVars.fdl_rmax', designvars[15]),
              ('Main.DesignVars.fhl_rmin', designvars[16]),
              ('Main.DesignVars.fhl_rmax', designvars[17]),
              ('Main.DesignVars.tpl_rmin', designvars[18]),
              ('Main.DesignVars.tpl_rmax', designvars[19]),
              ('Main.DesignVars.tpm_rmin', designvars[20]),
              ('Main.DesignVars.tpm_rmax', designvars[21]),
              ('Main.DesignVars.GlobalStrengthFactor', designvars[22])
              ]
    outputs =  ['Main.Studies.ParameterStudies.PlantarFlexorMuscles.IsometricStrength.Output.Strength.Val',
                'Main.Studies.ParameterStudies.PlantarFlexorMuscles.ConcentricStrength.Output.Strength.Val',
                'Main.Studies.ParameterStudies.PlantarFlexorMuscles.EccentricStrength.Output.Strength.Val',
                'Main.Studies.ParameterStudies.DorsiFlexorMuscles.IsometricStrength.Output.Strength.Val',
                'Main.Studies.ParameterStudies.DorsiFlexorMuscles.ConcentricStrength.Output.Strength.Val',
                'Main.Studies.ParameterStudies.DorsiFlexorMuscles.EccentricStrength.Output.Strength.Val']
    return (app, loadmacro, macrocmds, inputs,outputs)

def eval_w_gradient(designvars,*arg):
    pertubation_factor = 10e-4
    global iteration_counter
    iteration_counter += 1
    print iteration_counter, 'Design vars:', designvars
    (app, loadmacro, macrocmds, inputs,outputs) = setup_study(designvars)
    (res, pert) = app.start_pertubation_job(loadmacro, macrocmds, inputs, outputs,
                              perturb_factor = pertubation_factor)
    key_isoplantarflex = outputs[0]; key_conplantarflex = outputs[1]; key_eccplantarflex = outputs[2];
    key_isodorsiflex = outputs[3]; key_condorsiflex = outputs[4]; key_eccdorsiflex = outputs[5]
    pertubations = zeros((len(designvars,)))
    for i in range(len(designvars,)):
        pertubations[i] = metric(pert[key_isoplantarflex][i], pert[key_conplantarflex][i], pert[key_eccplantarflex][i],                                
                                 pert[key_isodorsiflex][i],   pert[key_condorsiflex][i],   pert[key_eccdorsiflex][i])
    objective = metric(res[key_isoplantarflex],res[key_conplantarflex],res[key_eccplantarflex],res[key_isodorsiflex],res[key_condorsiflex],res[key_eccdorsiflex])
    gradient = (pertubations-objective)/pertubation_factor
    print 'Objective:', objective
    print 'Gradient:', gradient
    return objective, gradient

def metric(c_isoplantarflex, c_conplantarflex, c_eccplantarflex, c_isodorsiflex, c_condorsiflex, c_eccdorsiflex):
    if isinstance(c_isoplantarflex, list):
        c_isoplantarflex = c_isoplantarflex[0]
    if isinstance(c_conplantarflex, list):
        c_conplantarflex = c_conplantarflex[0]
    if isinstance(c_eccplantarflex, list):
        c_eccplantarflex = c_eccplantarflex[0]
    if isinstance(c_isodorsiflex, list):
        c_isodorsiflex = c_isodorsiflex[0]
    if isinstance(c_condorsiflex, list):
        c_condorsiflex = c_condorsiflex[0]
    if isinstance(c_eccdorsiflex, list):
        c_eccdorsiflex = c_eccdorsiflex[0]

    import experimental_data_R1 as data
    
    m_isoplantarflex = mean(data.isoplantarflexor_normalized,1)
    m_conplantarflex = mean(data.conplantarflexor_normalized,1)
    m_eccplantarflex = mean(data.eccplantarflexor_normalized,1)
    m_isodorsiflex = mean(data.isodorsiflexor_normalized,1)
    m_condorsiflex = mean(data.condorsiflexor_normalized,1)
    m_eccdorsiflex = mean(data.eccdorsiflexor_normalized,1)

    norm_factor = c_eccplantarflex[3]
    c_isoplantarflex = c_isoplantarflex/norm_factor
    c_conplantarflex = c_conplantarflex/norm_factor
    c_eccplantarflex = c_eccplantarflex/norm_factor
    c_isodorsiflex = c_isodorsiflex/norm_factor
    c_condorsiflex = c_condorsiflex/norm_factor
    c_eccdorsiflex = c_eccdorsiflex/norm_factor

    try:
        ss_isoplantarflex = sum(((c_isoplantarflex-m_isoplantarflex)/m_isoplantarflex)**2)
        ss_conplantarflex = sum(((c_conplantarflex-m_conplantarflex)/m_conplantarflex)**2)
        ss_eccplantarflex = sum(((c_eccplantarflex-m_eccplantarflex)/m_eccplantarflex)**2)
        ss_isodorsiflex = sum(((c_isodorsiflex-m_isodorsiflex)/m_isodorsiflex)**2)
        ss_condorsiflex = sum(((c_condorsiflex-m_condorsiflex)/m_condorsiflex)**2)
        ss_eccdorsiflex = sum(((c_eccdorsiflex-m_eccdorsiflex)/m_eccdorsiflex)**2)
    except TypeError:
        print 'Error in metric. Return 100'
        return 100
    N_total = len(m_isoplantarflex)+len(m_conplantarflex)+len(m_eccplantarflex)+len(m_isodorsiflex)+len(m_condorsiflex)+len(m_eccdorsiflex)
    weight = float(N_total) / array([len(m_isoplantarflex), len(m_conplantarflex), len(m_eccplantarflex), len(m_isodorsiflex), len(m_condorsiflex), len(m_eccdorsiflex)])
    return sqrt(ss_isoplantarflex*weight[0] + ss_conplantarflex*weight[1] + ss_eccplantarflex*weight[2] + ss_isodorsiflex*weight[3] + ss_condorsiflex*weight[4] + ss_eccdorsiflex*weight[5])





if __name__ == '__main__':
    x0 = array([0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 0.5, 1.4, 1])
    bounds = [(0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.1,0.7), (1,1.6), (0.7,1.1)] 
    epsilon = 1e-4
    (x,f,d) =  fmin_l_bfgs_b(func = eval_w_gradient, x0 = x0, args=(epsilon,), bounds = bounds)
#(x,nfeval,rc) = fmin_tnc(func = evaluate, x0 = x0, fprime = gradient, args=(epsilon,), bounds = bounds, maxCGit=0,  eta=-1, stepmx=0.05, disp=1)