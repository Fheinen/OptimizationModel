# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:27:17 2015

@author: fh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 08:28:47 2014

@author: fh
"""


import matplotlib.pyplot as plt
import numpy as np

from anypytoolsfh.abcutils import AnyPyProcess
app = AnyPyProcess()

from anypytoolsfh.abcutils import AnyPyProcess 
 
from ExperimentalData import ExpData

    

def run_model(DesignVars):
    ''' Ruturns the x,y potions for the tip of the A frame '''
    folder = 'C:/Users/fh/Documents/AAU/PhD-AAU/PhD projekt/OptimeringsArtikle/Scripts/OptimizationStudies'    
    app = AnyPyProcess(anybodycon_path = 'C:/Program Files (x86)/AnyBody Technology/AnyBody.6.0/AnyBodyCon.exe', ignore_errors = ['ERROR(OBJ.MCH.MUS6)'])
    macro = [['load "Optimization.main.any"',
        'classoperation Main.DesignVars.GlobalStrengthFactor "Set Value" --value={:12f}'.format( DesignVars[0]),
        'operation Main.RunApplication1',
        'run',
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
#    pf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusMedialis3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.SoleusLateralis3Par.Lt0'],
#                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GastrocnemiusMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorDigitorumLongus3Par.Lt0'],
#                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.FlexorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorLateralis3Par.Lt0'],
#                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisPosteriorMedialis3Par.Lt0']])
#    Kf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputLongum1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.BicepsFemorisCaputBreve3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.Semitendinosus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.Semimembranosus1Par.Lt0']])
#    Ke = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisInferior6Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusLateralisSuperior2Par.Lt0'],
#                   output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisMid2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusMedialisSuperior4Par.Lt0'],
#                    output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.VastusIntermedius6Par.Lt0']])
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
#    hf = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.RectusFemorisLateralis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.RectusFemorisMedialis1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TensorFasciaeLatae1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TensorFasciaeLatae2Par.Lt0']])
#    he = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusSuperior6Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior3Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior4Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior5Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.GluteusMaximusInferior6Par.Lt0']])
#    ta = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.TibialisAnterior3Par.Lt0']])
#    edl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorDigitorumLongus3Par.Lt0']])
#    ehl = np.array([output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus1Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus2Par.Lt0'],output['Main.HumanModel.BodyModel.Right.Leg.MusPar.ExtensorHallucisLongus3Par.Lt0']])

#    np.save('PlanFlex',pf)
#    np.save('KneeFlex',Kf)
#    np.save('KneeEx',Ke)   
#    np.save('HipFlex',hf)  
#    np.save('HipEx',he)

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
#        Lt0Pen1 = np.array(10.0*np.sum(((x[1]-pf[0])**2)+((x[2]-pf[1])**2)+((x[3]-pf[2])**2)+((x[4]-pf[3])**2)+((x[5]-pf[4])**2)+((x[6]-pf[5])**2)+((x[7]-pf[6])**2)+((x[8]-pf[7])**2)+((x[9]-pf[8])**2)+((x[10]-pf[9])**2)+((x[11]-pf[10])**2)+((x[12]-pf[11])**2)+((x[13]-pf[12])**2)+((x[14]-pf[13])**2)+((x[15]-pf[14])**2)+((x[16]-pf[15])**2)+((x[17]-pf[16])**2)+((x[18]-pf[17])**2)+((x[19]-pf[18])**2)+((x[20]-pf[19])**2)))
#        Lt0Pen2 = np.array(10.0*np.sum(((x[20]-Kf[0])**2)+((x[21]-Kf[1])**2)+((x[22]-Kf[2])**2)+((x[23]-Kf[3])**2)+((x[24]-Kf[4])**2)+((x[25]-Kf[5])**2)))
#        Lt0Pen3 = np.array(10.0*np.sum(((x[26]-Ke[0])**2)+((x[27]-Ke[1])**2)+((x[28]-Ke[2])**2)+((x[29]-Ke[3])**2)+((x[30]-Ke[4])**2)+((x[31]-Ke[5])**2)+((x[32]-Ke[6])**2)+((x[33]-Ke[7])**2)+((x[34]-Ke[8])**2)+((x[35]-Ke[9])**2)+((x[36]-Ke[10])**2)+((x[37]-Ke[11])**2)+((x[87]-Ke[12])**2)+((x[88]-Ke[13])**2)+((x[89]-Ke[14])**2)+((x[90]-Ke[15])**2)+((x[91]-Ke[16])**2)+((x[92]-Ke[17])**2)+((x[93]-Ke[18])**2)+((x[94]-Ke[19])**2)+((x[95]-Ke[20])**2)+((x[96]-Ke[21])**2)))
#        Lt0Pen4 = np.array(10.0*np.sum(((x[97]-hf[0])**2)+((x[98]-hf[1])**2)+((x[99]-hf[2])**2)+((x[100]-hf[3])**2)))
#        Lt0Pen5 = np.array(10.0*np.sum(((x[101]-he[0])**2)+((x[102]-he[1])**2)+((x[103]-he[2])**2)+((x[104]-he[3])**2)+((x[105]-he[4])**2)+((x[106]-he[5])**2)+((x[107]-he[6])**2)+((x[108]-he[7])**2)+((x[109]-he[8])**2)+((x[110]-he[9])**2)+((x[111]-he[10])**2)+((x[112]-he[11])**2)))
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
        f = np.sqrt(np.sum(np.sum(((NormExpDataIsomPF-NormStrengthIsomPF)**2))+np.sum(((NormExpDataIsomKF-NormStrengthIsomKF)**2))+np.sum(((NormExpDataIsomKE-NormStrengthIsomKE)**2))+np.sum(((NormExpDataIsomHF-NormStrengthIsomHF)**2))+np.sum(((NormExpDataIsomHE-NormStrengthIsomHE)**2))))
#        print demo3        
        print f
        
        g = [0]
        
    return f, g, fail, 


    
    