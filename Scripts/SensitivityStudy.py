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
        'classoperation Main.DesignVars.fdl_rmin "Set Value" --value={:12f}'.format(DesignVars[8]),
        'classoperation Main.DesignVars.fdl_rmax "Set Value" --value={:12f}'.format( DesignVars[9]),
        'classoperation Main.DesignVars.fhl_rmin "Set Value" --value={:12f}'.format(DesignVars[10]),
        'classoperation Main.DesignVars.fhl_rmax "Set Value" --value={:12f}'.format( DesignVars[11]),
        'classoperation Main.DesignVars.tpl_rmin "Set Value" --value={:12f}'.format(DesignVars[12]),
        'classoperation Main.DesignVars.tpl_rmax "Set Value" --value={:12f}'.format( DesignVars[13]),
        'classoperation Main.DesignVars.tpm_rmin "Set Value" --value={:12f}'.format(DesignVars[14]),
        'classoperation Main.DesignVars.tpm_rmax "Set Value" --value={:12f}'.format( DesignVars[15]),
        'classoperation Main.DesignVars.bfcl_rmin "Set Value" --value={:12f}'.format(DesignVars[16]),
        'classoperation Main.DesignVars.bfcl_rmax "Set Value" --value={:12f}'.format( DesignVars[17]),
        'classoperation Main.DesignVars.bfcb_rmin "Set Value" --value={:12f}'.format(DesignVars[18]),
        'classoperation Main.DesignVars.bfcb_rmax "Set Value" --value={:12f}'.format( DesignVars[19]),
        'classoperation Main.DesignVars.std_rmin "Set Value" --value={:12f}'.format(DesignVars[20]),
        'classoperation Main.DesignVars.std_rmax "Set Value" --value={:12f}'.format( DesignVars[21]),
        'classoperation Main.DesignVars.smb_rmin "Set Value" --value={:12f}'.format(DesignVars[22]),
        'classoperation Main.DesignVars.smb_rmax "Set Value" --value={:12f}'.format( DesignVars[23]),
        'classoperation Main.DesignVars.vli_rmin "Set Value" --value={:12f}'.format(DesignVars[24]),
        'classoperation Main.DesignVars.vli_rmax "Set Value" --value={:12f}'.format( DesignVars[25]),
        'classoperation Main.DesignVars.vls_rmin "Set Value" --value={:12f}'.format(DesignVars[26]),
        'classoperation Main.DesignVars.vls_rmax "Set Value" --value={:12f}'.format( DesignVars[27]),
        'classoperation Main.DesignVars.vmi_rmin "Set Value" --value={:12f}'.format(DesignVars[28]),
        'classoperation Main.DesignVars.vmi_rmax "Set Value" --value={:12f}'.format( DesignVars[29]),
        'classoperation Main.DesignVars.vmm_rmin "Set Value" --value={:12f}'.format(DesignVars[30]),
        'classoperation Main.DesignVars.vmm_rmax "Set Value" --value={:12f}'.format( DesignVars[31]),
        'classoperation Main.DesignVars.vms_rmin "Set Value" --value={:12f}'.format(DesignVars[32]),
        'classoperation Main.DesignVars.vms_rmax "Set Value" --value={:12f}'.format( DesignVars[33]),
        'classoperation Main.DesignVars.vi_rmin "Set Value" --value={:12f}'.format(DesignVars[34]),
        'classoperation Main.DesignVars.vi_rmax "Set Value" --value={:12f}'.format( DesignVars[35]),
        'classoperation Main.DesignVars.rf_rmin "Set Value" --value={:12f}'.format(DesignVars[36]),
        'classoperation Main.DesignVars.rf_rmax "Set Value" --value={:12f}'.format( DesignVars[37]),
        'classoperation Main.DesignVars.tfl_rmin "Set Value" --value={:12f}'.format(DesignVars[38]),
        'classoperation Main.DesignVars.tfl_rmax "Set Value" --value={:12f}'.format( DesignVars[39]),
        'classoperation Main.DesignVars.gms_rmin "Set Value" --value={:12f}'.format(DesignVars[40]),
        'classoperation Main.DesignVars.gms_rmax "Set Value" --value={:12f}'.format( DesignVars[41]),
        'classoperation Main.DesignVars.gmi_rmin "Set Value" --value={:12f}'.format(DesignVars[42]),
        'classoperation Main.DesignVars.gmi_rmax "Set Value" --value={:12f}'.format( DesignVars[43]),
        'classoperation Main.DesignVars.LocalStrengthFactorPlantarFlexors "Set Value" --value={:12f}'.format( DesignVars[44]),
        'classoperation Main.DesignVars.LocalStrengthFactorKneeFlexor "Set Value" --value={:12f}'.format( DesignVars[45]),
        'classoperation Main.DesignVars.LocalStrengthFactorKneeExtensor "Set Value" --value={:12f}'.format( DesignVars[46]),
        'classoperation Main.DesignVars.LocalStrengthFactorHipExtensor "Set Value" --value={:12f}'.format( DesignVars[47]),
        'classoperation Main.DesignVars.LocalStrengthFactorHipFlexor "Set Value" --value={:12f}'.format( DesignVars[48]),
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
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputLongum1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.Semitendinosus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.Semimembranosus1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior4Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior5Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior6Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior4Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius4Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius5Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius6Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.RectusFemorisLateralis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.RectusFemorisMedialis1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TensorFasciaeLatae1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.TensorFasciaeLatae2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior4Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior5Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior6Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior1Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior2Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior3Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior4Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior5Par.Lt0 "Dump"',
        'classoperation Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior6Par.Lt0 "Dump"',
        'operation Main.RunApplication2',
        'run',
        'classoperation Main.Studies.ParameterStudies.PlantarFlexorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'classoperation Main.Studies.ParameterStudies.KneeFlexorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'classoperation Main.Studies.ParameterStudies.KneeExtensorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'classoperation Main.Studies.ParameterStudies.HipFlexorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'classoperation Main.Studies.ParameterStudies.HipExtensorMuscles.IsometricStrength.Output.Strength.Val "Dump"',
        'exit']]
       
    output = app.start_macro(macro, folderlist = [folder] )[0]
    
    return (output)
    
EDTuple = ExpData()
EDIsomDF = EDTuple[0]
EDIsomPF = EDTuple[1]
EDIsomKF = EDTuple[2]
EDIsomKE = EDTuple[3]
EDIsomHF = EDTuple[4]
EDIsomHE = EDTuple[5]
#ExpDataIsomDF = np.array([28.578, 34.452, 35.982, 33.462, 32.62, 28.594])
#ExpDataIsomDF = np.array([11.25, 13.63, 15.97, 18.16, 20.07, 21.59, 22.69, 23.32, 23.51, 24.31])

NormExpDataIsomPF = EDIsomPF/np.max(EDIsomPF)
NormExpDataIsomKF = EDIsomKF/np.max(EDIsomKF)
NormExpDataIsomKE = EDIsomKE/np.max(EDIsomKE)
NormExpDataIsomHF = EDIsomHF/np.max(EDIsomHF)
NormExpDataIsomHE = EDIsomHE/np.max(EDIsomHE)

def objfunc(x):
    f = 0
    g = 0
    fail = 0
    
    output = run_model(x)
    JointStrengthIsomPF = output['Main.Studies.ParameterStudies.PlantarFlexorMuscles.IsometricStrength.Output.Strength.Val']
    JointStrengthIsomKF = output['Main.Studies.ParameterStudies.KneeFlexorMuscles.IsometricStrength.Output.Strength.Val']
    JointStrengthIsomKE = output['Main.Studies.ParameterStudies.KneeExtensorMuscles.IsometricStrength.Output.Strength.Val']
    JointStrengthIsomHF = output['Main.Studies.ParameterStudies.HipFlexorMuscles.IsometricStrength.Output.Strength.Val']
    JointStrengthIsomHE = output['Main.Studies.ParameterStudies.HipExtensorMuscles.IsometricStrength.Output.Strength.Val']
    pf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis3Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus3Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis3Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis3Par.Lt0']])
    Kf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputLongum1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.Semitendinosus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.Semimembranosus1Par.Lt0']])
    Ke = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior6Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior2Par.Lt0'],
                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior4Par.Lt0'],
                    output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius6Par.Lt0']])
#    sm = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis3Par.Lt0']])
#    sl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis3Par.Lt0']])
#    gas = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusMedialis1Par.Lt0']])
#    fdl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus3Par.Lt0']])
#    fhl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0']])
#    tpl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis3Par.Lt0']])
#    tpm = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis3Par.Lt0']])
#    bf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputLongum1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve3Par.Lt0']])
#    std = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.Semitendinosus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.Semimembranosus1Par.Lt0']])
#    vl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior6Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior2Par.Lt0']])
#    vm = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior6Par.Lt0']])
#    vi = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius6Par.Lt0']])
    hf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.RectusFemorisLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.RectusFemorisMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TensorFasciaeLatae1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TensorFasciaeLatae2Par.Lt0']])
    he = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior6Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior6Par.Lt0']])
#    ta = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior3Par.Lt0']])
#    edl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus3Par.Lt0']])
#    ehl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus3Par.Lt0']])

    np.save('PlanFlex',pf)
    np.save('KneeFlex',Kf)
    np.save('KneeEx',Ke)   
    np.save('HipFlex',hf)  
    np.save('HipEx',he)

#    np.save('TibialisAnt',ta)
#    np.save('ExtensorDL',edl)
#    np.save('ExtensorHL',ehl)

#    print TibialisAnt3
    print JointStrengthIsomPF
    print x
    if JointStrengthIsomPF is None:
        fail = 1
    else:
        # Objective: 
#        Lt0Pen = np.array(100.0*np.sum(((x[7]-ta[0])**2)+((x[8]-ta[1])**2)+((x[9]-ta[2])**2)+((x[10]-edl[0])**2)+((x[11]-edl[1])**2)+((x[12]-edl[2])**2)+((x[13]-ehl[0])**2)+((x[14]-ehl[1])**2)+((x[15]-ehl[2])**2)))
        Lt0Pen1 = np.array(10.0*np.sum(((x[49]-pf[0])**2)+((x[50]-pf[1])**2)+((x[51]-pf[2])**2)+((x[52]-pf[3])**2)+((x[53]-pf[4])**2)+((x[54]-pf[5])**2)+((x[55]-pf[6])**2)+((x[56]-pf[7])**2)+((x[57]-pf[8])**2)+((x[58]-pf[9])**2)+((x[59]-pf[10])**2)+((x[60]-pf[11])**2)+((x[61]-pf[12])**2)+((x[62]-pf[13])**2)+((x[63]-pf[14])**2)+((x[64]-pf[15])**2)+((x[65]-pf[16])**2)+((x[66]-pf[17])**2)+((x[67]-pf[18])**2)+((x[68]-pf[19])**2)))
        Lt0Pen2 = np.array(10.0*np.sum(((x[69]-Kf[0])**2)+((x[70]-Kf[1])**2)+((x[71]-Kf[2])**2)+((x[72]-Kf[3])**2)+((x[73]-Kf[4])**2)+((x[74]-Kf[5])**2)))
        Lt0Pen3 = np.array(10.0*np.sum(((x[75]-Ke[0])**2)+((x[76]-Ke[1])**2)+((x[77]-Ke[2])**2)+((x[78]-Ke[3])**2)+((x[79]-Ke[4])**2)+((x[80]-Ke[5])**2)+((x[81]-Ke[6])**2)+((x[82]-Ke[7])**2)+((x[83]-Ke[8])**2)+((x[84]-Ke[9])**2)+((x[85]-Ke[10])**2)+((x[86]-Ke[11])**2)+((x[87]-Ke[12])**2)+((x[88]-Ke[13])**2)+((x[89]-Ke[14])**2)+((x[90]-Ke[15])**2)+((x[91]-Ke[16])**2)+((x[92]-Ke[17])**2)+((x[93]-Ke[18])**2)+((x[94]-Ke[19])**2)+((x[95]-Ke[20])**2)+((x[96]-Ke[21])**2)))
        Lt0Pen4 = np.array(10.0*np.sum(((x[97]-hf[0])**2)+((x[98]-hf[1])**2)+((x[99]-hf[2])**2)+((x[100]-hf[3])**2)))
        Lt0Pen5 = np.array(10.0*np.sum(((x[101]-he[0])**2)+((x[102]-he[1])**2)+((x[103]-he[2])**2)+((x[104]-he[3])**2)+((x[105]-he[4])**2)+((x[106]-he[5])**2)+((x[107]-he[6])**2)+((x[108]-he[7])**2)+((x[109]-he[8])**2)+((x[110]-he[9])**2)+((x[111]-he[10])**2)+((x[112]-he[11])**2)))
#        Lt0Pen = np.array(100.0*np.sum(((x[3]-ta1)**2)+((x[4]-ta2)**2)+((x[5]-ta3)**2)))
#        NormStrengthIsomDF = JointStrengthIsomDF/np.max(EDIsomDF)
        NormStrengthIsomPF = JointStrengthIsomPF/np.max(EDIsomPF)
        NormStrengthIsomKF = JointStrengthIsomKF/np.max(EDIsomKF)
        NormStrengthIsomKE = JointStrengthIsomKE/np.max(EDIsomKE)
        NormStrengthIsomHF = JointStrengthIsomHF/np.max(EDIsomHF)
        NormStrengthIsomHE = JointStrengthIsomHE/np.max(EDIsomHE)
#        demo = NormExpDataIsomDF-NormStrengthIsomDF
#        demo2 = (NormExpDataIsomDF-NormStrengthIsomDF)**2
#        demo3 = np.sqrt((NormExpDataIsomDF-NormStrengthIsomDF)**2)
#        demo4 = np.sum(np.sqrt((NormExpDataIsomDF-NormStrengthIsomDF)**2))+Lt0Pen
        f = np.sqrt(np.sum(np.sum(((NormExpDataIsomPF-NormStrengthIsomPF)**2)+Lt0Pen1)+np.sum(((NormExpDataIsomKF-NormStrengthIsomKF)**2)+Lt0Pen2)+np.sum(((NormExpDataIsomKE-NormStrengthIsomKE)**2)+Lt0Pen3)+np.sum(((NormExpDataIsomHF-NormStrengthIsomHF)**2)+Lt0Pen4)+np.sum(((NormExpDataIsomHE-NormStrengthIsomHE)**2)+Lt0Pen5)))
#        print demo3        
        print f
        print Lt0Pen1
        g = [0]
        
    return f, g, fail, 

def gradfunc(x,f,g):
    
    PlanFlex=np.load('PlanFlex.npy')
    KneeFlex=np.load('KneeFlex.npy')
    KneeEx=np.load('KneeEx.npy')
    HipFlex=np.load('HipFlex.npy')
    HipEx=np.load('HipEx.npy')

#    TibialisAnt=np.load('TibialisAnt.npy')
#    ExtensorDL=np.load('ExtensorDL.npy')
#    ExtensorHL=np.load('ExtensorHL.npy')
    g_obj = [0.0]*66
    g_obj[0] = 10.0*2*(x[49]-PlanFlex[0])
    g_obj[1] = 10.0*2*(x[50]-PlanFlex[1])
    g_obj[2] = 10.0*2*(x[51]-PlanFlex[2])
    g_obj[3] = 10.0*2*(x[52]-PlanFlex[3])
    g_obj[4] = 10.0*2*(x[53]-PlanFlex[4])
    g_obj[5] = 10.0*2*(x[54]-PlanFlex[5])
    g_obj[6] = 10.0*2*(x[55]-PlanFlex[6])
    g_obj[7] = 10.0*2*(x[56]-PlanFlex[7])
    g_obj[8] = 10.0*2*(x[57]-PlanFlex[8])
    g_obj[9] = 10.0*2*(x[58]-PlanFlex[9])
    g_obj[10] = 10.0*2*(x[59]-PlanFlex[10])
    g_obj[11] = 10.0*2*(x[60]-PlanFlex[11])
    g_obj[12] = 10.0*2*(x[61]-PlanFlex[12])
    g_obj[13] = 10.0*2*(x[62]-PlanFlex[13])
    g_obj[14] = 10.0*2*(x[63]-PlanFlex[14])
    g_obj[15] = 10.0*2*(x[64]-PlanFlex[15])
    g_obj[16] = 10.0*2*(x[65]-PlanFlex[16])
    g_obj[17] = 10.0*2*(x[66]-PlanFlex[17])
    g_obj[18] = 10.0*2*(x[67]-PlanFlex[18])
    g_obj[19] = 10.0*2*(x[68]-PlanFlex[19])
    g_obj[20] = 10.0*2*(x[69]-KneeFlex[0])
    g_obj[21] = 10.0*2*(x[70]-KneeFlex[1])
    g_obj[22] = 10.0*2*(x[71]-KneeFlex[2])
    g_obj[23] = 10.0*2*(x[72]-KneeFlex[3])
    g_obj[24] = 10.0*2*(x[73]-KneeFlex[4])
    g_obj[25] = 10.0*2*(x[74]-KneeFlex[5])
    g_obj[26] = 10.0*2*(x[75]-KneeEx[0])
    g_obj[27] = 10.0*2*(x[76]-KneeEx[1])
    g_obj[28] = 10.0*2*(x[77]-KneeEx[2])
    g_obj[29] = 10.0*2*(x[78]-KneeEx[3])
    g_obj[30] = 10.0*2*(x[79]-KneeEx[4])
    g_obj[31] = 10.0*2*(x[80]-KneeEx[5])
    g_obj[32] = 10.0*2*(x[81]-KneeEx[6])
    g_obj[33] = 10.0*2*(x[82]-KneeEx[7])
    g_obj[34] = 10.0*2*(x[83]-KneeEx[8])
    g_obj[35] = 10.0*2*(x[84]-KneeEx[9])
    g_obj[36] = 10.0*2*(x[85]-KneeEx[10])
    g_obj[37] = 10.0*2*(x[86]-KneeEx[11])
    g_obj[38] = 10.0*2*(x[87]-KneeEx[12])
    g_obj[39] = 10.0*2*(x[88]-KneeEx[13])
    g_obj[40] = 10.0*2*(x[89]-KneeEx[14])
    g_obj[41] = 10.0*2*(x[90]-KneeEx[15])
    g_obj[42] = 10.0*2*(x[91]-KneeEx[16])
    g_obj[43] = 10.0*2*(x[92]-KneeEx[17])
    g_obj[44] = 10.0*2*(x[93]-KneeEx[18])
    g_obj[45] = 10.0*2*(x[94]-KneeEx[19])
    g_obj[46] = 10.0*2*(x[95]-KneeEx[20])
    g_obj[47] = 10.0*2*(x[96]-KneeEx[21])
    g_obj[48] = 10.0*2*(x[97]-HipFlex[0])
    g_obj[49] = 10.0*2*(x[98]-HipFlex[1])
    g_obj[50] = 10.0*2*(x[99]-HipFlex[2])
    g_obj[51] = 10.0*2*(x[100]-HipFlex[3])
    g_obj[52] = 10.0*2*(x[101]-HipEx[0])
    g_obj[53] = 10.0*2*(x[102]-HipEx[1])
    g_obj[54] = 10.0*2*(x[103]-HipEx[2])
    g_obj[55] = 10.0*2*(x[104]-HipEx[3])
    g_obj[56] = 10.0*2*(x[105]-HipEx[4])
    g_obj[57] = 10.0*2*(x[106]-HipEx[5])
    g_obj[58] = 10.0*2*(x[107]-HipEx[6])
    g_obj[59] = 10.0*2*(x[108]-HipEx[7])
    g_obj[60] = 10.0*2*(x[109]-HipEx[8])
    g_obj[61] = 10.0*2*(x[110]-HipEx[9])
    g_obj[62] = 10.0*2*(x[111]-HipEx[10])
    g_obj[63] = 10.0*2*(x[112]-HipEx[11])
    
    g_con = 0
    
    fail = 0
    return g_obj, g_con, fail
    
    