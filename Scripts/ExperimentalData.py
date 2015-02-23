# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:14:39 2014

@author: fh
"""

import numpy as np
#import SensitivityStudy
#from SensitivityStudy import S
#


""" S1 = S1, S2 = S2, S3 = L1, S4 = L2, S10 = RefModel"""
S = 4

def ExpData():

    if S == 1:
        ExpDataIsomDF = np.array([24.093, 27.33, 27.82, 26.194, 24.033, 21.925, 17.863])
        ExpDataIsomPF = np.array([74.59, 86.207, 76.242, 76.492, 71.596, 64.251, 57.044])
        ExpDataIsomKneeEx = np.array([33.59, 87.48, 181.57, 181.57, 222.17, 215.22, 150.71])
        ExpDataIsomKneeFlex = np.array([95.28, 104.72, 112.05, 112.97, 104.49, 84.56])
        ExpDataIsomHipEx = np.array([95.02130366, 118.3611658, 129.252697, 119.0747124, 112.4053434, 128.6762827, 238.1047207])
        ExpDataIsomHipFlex = np.array([179.3446172, 124.4025573, 113.1709132, 96.58074401, 83.6610253, 80.72746721, 78.07377119])
        
        NExpDataIsomDF = ExpDataIsomDF/np.max(ExpDataIsomDF)
        NExpDataIsomPF = ExpDataIsomPF/np.max(ExpDataIsomPF)
        NExpDataIsomKneeEx = ExpDataIsomKneeEx/np.max(ExpDataIsomKneeEx)
        NExpDataIsomKneeFlex = ExpDataIsomKneeFlex/np.max(ExpDataIsomKneeFlex)
        NExpDataIsomHipEx = ExpDataIsomHipEx/np.max(ExpDataIsomHipEx)
        NExpDataIsomHipFlex = ExpDataIsomHipFlex/np.max(ExpDataIsomHipFlex)
        
#        ExpDataIsokDFCon = np.array([1])
#        ExpDataIsokPFCon = np.array([1])
#        ExpDataIsokKneeExCon = np.array([1])
#        ExpDataIsokKneeFlexCon = np.array([1])
#        ExpDataIsokHipExCon = np.array([1])
#        ExpDataIsokHipFlexCon = np.array([1])
#        
#        NExpDataIsokDFCon = ExpDataIsokDFCon/np.max(ExpDataIsokDFCon)
#        NExpDataIsokPFCon = ExpDataIsokPFCon/np.max(ExpDataIsokPFCon)
#        NExpDataIsokKneeExCon = ExpDataIsokKneeExCon/np.max(ExpDataIsokKneeExCon)
#        NExpDataIsokKneeFlexCon = ExpDataIsokKneeFlexCon/np.max(ExpDataIsokKneeFlexCon)
#        NExpDataIsokHipExCon = ExpDataIsokHipExCon/np.max(ExpDataIsokHipExCon)
#        NExpDataIsokHipFlexCon = ExpDataIsokHipFlexCon/np.max(ExpDataIsokHipFlexCon)        
#        
#        ExpDataIsokDFEcc = np.array([1])
#        ExpDataIsokPFEcc = np.array([1])
#        ExpDataIsokKneeExEcc = np.array([1])
#        ExpDataIsokKneeFlexEcc = np.array([1])
#        ExpDataIsokHipExEcc = np.array([1])
#        ExpDataIsokHipFlexEcc = np.array([1])
#        
#        NExpDataIsokDFEcc = ExpDataIsokDFEcc/np.max(ExpDataIsokDFEcc)
#        NExpDataIsokPFEcc = ExpDataIsokPFEcc/np.max(ExpDataIsokPFEcc)
#        NExpDataIsokKneeExEcc = ExpDataIsokKneeExEcc/np.max(ExpDataIsokKneeExEcc)
#        NExpDataIsokKneeFlexEcc = ExpDataIsokKneeFlexEcc/np.max(ExpDataIsokKneeFlexEcc)
#        NExpDataIsokHipExEcc = ExpDataIsokHipExEcc/np.max(ExpDataIsokHipExEcc)
#        NExpDataIsokHipFlexEcc = ExpDataIsokHipFlexEcc/np.max(ExpDataIsokHipFlexEcc)

        
    elif S ==2:
        ExpDataIsomDF = np.array([17.006, 49.299, 45.18, 40.913, 47.769, 40.186, 40.419])
        ExpDataIsomPF = np.array([194.479, 187.138, 131.577, 112.997, 98.601, 72.783, 63.773]) 
        ExpDataIsomKneeEx = np.array([183,2259775, 242,3303549, 293,865679, 334,4246372, 327,6299895, 281,4626879, 224,9562244])
        ExpDataIsomKneeFlex = np.array([131.9209856, 142.7318921, 123.62114, 117.281537, 95.17888944, 95.39809413, 71.15866108])
        ExpDataIsomHipEx = np.array([75.48071293, 153.6428117, 214.6432782, 239.7050942, 277.4362731, 333.3740434, 432.7521735])
        ExpDataIsomHipFlex = np.array([192.7577494, 180.0526135, 147.1078867, 120.3034693, 103.6438652, 89.73144944, 92.08897619])

        NExpDataIsomDF = ExpDataIsomDF/np.max(ExpDataIsomDF)
        NExpDataIsomPF = ExpDataIsomPF/np.max(ExpDataIsomPF)
        NExpDataIsomKneeEx = ExpDataIsomKneeEx/np.max(ExpDataIsomKneeEx)
        NExpDataIsomKneeFlex = ExpDataIsomKneeFlex/np.max(ExpDataIsomKneeFlex)
        NExpDataIsomHipEx = ExpDataIsomHipEx/np.max(ExpDataIsomHipEx)
        NExpDataIsomHipFlex = ExpDataIsomHipFlex/np.max(ExpDataIsomHipFlex)
        
#        ExpDataIsokDFCon = np.array([])
#        ExpDataIsokPFCon = np.array([])
#        ExpDataIsokKneeExCon = np.array([])
#        ExpDataIsokKneeFlexCon = np.array([])
#        ExpDataIsokHipExCon = np.array([])
#        ExpDataIsokHipFlexCon = np.array([])
#        
#        NExpDataIsokDFCon = ExpDataIsokDFCon/np.max(ExpDataIsokDFCon)
#        NExpDataIsokPFCon = ExpDataIsokPFCon/np.max(ExpDataIsokPFCon)
#        NExpDataIsokKneeExCon = ExpDataIsokKneeExCon/np.max(ExpDataIsokKneeExCon)
#        NExpDataIsokKneeFlexCon = ExpDataIsokKneeFlexCon/np.max(ExpDataIsokKneeFlexCon)
#        NExpDataIsokHipExCon = ExpDataIsokHipExCon/np.max(ExpDataIsokHipExCon)
#        NExpDataIsokHipFlexCon = ExpDataIsokHipFlexCon/np.max(ExpDataIsokHipFlexCon)        
#        
#        ExpDataIsokDFEcc = np.array([])
#        ExpDataIsokPFEcc = np.array([])
#        ExpDataIsokKneeExEcc = np.array([])
#        ExpDataIsokKneeFlexEcc = np.array([])
#        ExpDataIsokHipExEcc = np.array([])
#        ExpDataIsokHipFlexEcc = np.array([])
#        
#        NExpDataIsokDFEcc = ExpDataIsokDFEcc/np.max(ExpDataIsokDFEcc)
#        NExpDataIsokPFEcc = ExpDataIsokPFEcc/np.max(ExpDataIsokPFEcc)
#        NExpDataIsokKneeExEcc = ExpDataIsokKneeExEcc/np.max(ExpDataIsokKneeExEcc)
#        NExpDataIsokKneeFlexEcc = ExpDataIsokKneeFlexEcc/np.max(ExpDataIsokKneeFlexEcc)
#        NExpDataIsokHipExEcc = ExpDataIsokHipExEcc/np.max(ExpDataIsokHipExEcc)
#        NExpDataIsokHipFlexEcc = ExpDataIsokHipFlexEcc/np.max(ExpDataIsokHipFlexEcc)
            
    elif S ==3:
        ExpDataIsomDF = np.array([23.584, 32.331, 38.896, 40.667, 40.544, 37.723, 33.382])
        ExpDataIsomPF = np.array([160.841, 148.471, 108.377, 78.513, 58.373, 38.242, 18.815])
        ExpDataIsomKneeEx = np.array([40.5249628, 104.3250875, 182.3757841, 203.7302233,  217.7314217, 183.2865153, 141.1914118])
        ExpDataIsomKneeFlex = np.array([111.2159886, 118.2582084, 120.3486625, 98.62648716, 99.45867213, 86.01389072, 67.96893362])
        ExpDataIsomHipEx = np.array([89.51358704, 138.1933754, 140.2202003, 161.5722999, 239.2612601, 296.2512821, 322.5223848])
        ExpDataIsomHipFlex = np.array([153.7329748, 125.7049923, 116.5234537, 95.11366048, 96.98133807, 72.87270368, 55.94988186])
        
        NExpDataIsomDF = ExpDataIsomDF/np.max(ExpDataIsomDF)
        NExpDataIsomPF = ExpDataIsomPF/np.max(ExpDataIsomPF)
        NExpDataIsomKneeEx = ExpDataIsomKneeEx/np.max(ExpDataIsomKneeEx)
        NExpDataIsomKneeFlex = ExpDataIsomKneeFlex/np.max(ExpDataIsomKneeFlex)
        NExpDataIsomHipEx = ExpDataIsomHipEx/np.max(ExpDataIsomHipEx)
        NExpDataIsomHipFlex = ExpDataIsomHipFlex/np.max(ExpDataIsomHipFlex)
        
#        ExpDataIsokDFCon = np.array([])
#        ExpDataIsokPFCon = np.array([])
#        ExpDataIsokKneeExCon = np.array([])
#        ExpDataIsokKneeFlexCon = np.array([])
#        ExpDataIsokHipExCon = np.array([])
#        ExpDataIsokHipFlexCon = np.array([])
#        
#        NExpDataIsokDFCon = ExpDataIsokDFCon/np.max(ExpDataIsokDFCon)
#        NExpDataIsokPFCon = ExpDataIsokPFCon/np.max(ExpDataIsokPFCon)
#        NExpDataIsokKneeExCon = ExpDataIsokKneeExCon/np.max(ExpDataIsokKneeExCon)
#        NExpDataIsokKneeFlexCon = ExpDataIsokKneeFlexCon/np.max(ExpDataIsokKneeFlexCon)
#        NExpDataIsokHipExCon = ExpDataIsokHipExCon/np.max(ExpDataIsokHipExCon)
#        NExpDataIsokHipFlexCon = ExpDataIsokHipFlexCon/np.max(ExpDataIsokHipFlexCon)        
#        
#        ExpDataIsokDFEcc = np.array([])
#        ExpDataIsokPFEcc = np.array([])
#        ExpDataIsokKneeExEcc = np.array([])
#        ExpDataIsokKneeFlexEcc = np.array([])
#        ExpDataIsokHipExEcc = np.array([])
#        ExpDataIsokHipFlexEcc = np.array([])
#        
#        NExpDataIsokDFEcc = ExpDataIsokDFEcc/np.max(ExpDataIsokDFEcc)
#        NExpDataIsokPFEcc = ExpDataIsokPFEcc/np.max(ExpDataIsokPFEcc)
#        NExpDataIsokKneeExEcc = ExpDataIsokKneeExEcc/np.max(ExpDataIsokKneeExEcc)
#        NExpDataIsokKneeFlexEcc = ExpDataIsokKneeFlexEcc/np.max(ExpDataIsokKneeFlexEcc)
#        NExpDataIsokHipExEcc = ExpDataIsokHipExEcc/np.max(ExpDataIsokHipExEcc)
#        NExpDataIsokHipFlexEcc = ExpDataIsokHipFlexEcc/np.max(ExpDataIsokHipFlexEcc)

    elif S ==4:
        ExpDataIsomDF = np.array([28.577999999999900, 34.451999999999900, 35.981999999999900, 33.462000000000000, 32.619999999999900, 28.594000000000000])
        ExpDataIsomPF = np.array([72.085999999999900, 69.272000000000000, 69.224999999999900, 58.389000000000000, 42.430999999999900, 33.606999999999900])
        ExpDataIsomKneeEx = np.array([94.17841233, 128.6461692, 146.2296151, 165.2537596, 147.060925, 126.7744886, 107.7727066])
        ExpDataIsomKneeFlex = np.array([96.34111514, 102.0508518, 92.37011483, 90.2007155, 71.03587034, 61.01892538, 46.61337362])
        ExpDataIsomHipEx = np.array([74.73905805, 98.95982078, 119.6197801, 142.2137026, 169.089779, 189.613512, 188.6042206])
        ExpDataIsomHipFlex = np.array([121.7851437, 111.3843144, 111.570059, 91.25869226, 90.16802962, 75.15804894, 66.68170891])

        NExpDataIsomDF = ExpDataIsomDF/np.max(ExpDataIsomDF)
        NExpDataIsomPF = ExpDataIsomPF/np.max(ExpDataIsomPF)
        NExpDataIsomKneeEx = ExpDataIsomKneeEx/np.max(ExpDataIsomKneeEx)
        NExpDataIsomKneeFlex = ExpDataIsomKneeFlex/np.max(ExpDataIsomKneeFlex)
        NExpDataIsomHipEx = ExpDataIsomHipEx/np.max(ExpDataIsomHipEx)
        NExpDataIsomHipFlex = ExpDataIsomHipFlex/np.max(ExpDataIsomHipFlex)
        
#        ExpDataIsokDFCon = np.array([]) 96.34111514, 102.0508518, 92.37011483, 90.2007155, 71.03587034, 61.01892538, 46.61337362
#        ExpDataIsokPFCon = np.array([])
#        ExpDataIsokKneeExCon = np.array([])
#        ExpDataIsokKneeFlexCon = np.array([])
#        ExpDataIsokHipExCon = np.array([])
#        ExpDataIsokHipFlexCon = np.array([])
#        
#        NExpDataIsokDFCon = ExpDataIsokDFCon/np.max(ExpDataIsokDFCon)
#        NExpDataIsokPFCon = ExpDataIsokPFCon/np.max(ExpDataIsokPFCon)
#        NExpDataIsokKneeExCon = ExpDataIsokKneeExCon/np.max(ExpDataIsokKneeExCon)
#        NExpDataIsokKneeFlexCon = ExpDataIsokKneeFlexCon/np.max(ExpDataIsokKneeFlexCon)
#        NExpDataIsokHipExCon = ExpDataIsokHipExCon/np.max(ExpDataIsokHipExCon)
#        NExpDataIsokHipFlexCon = ExpDataIsokHipFlexCon/np.max(ExpDataIsokHipFlexCon)        
#        
#        ExpDataIsokDFEcc = np.array([])
#        ExpDataIsokPFEcc = np.array([])
#        ExpDataIsokKneeExEcc = np.array([])
#        ExpDataIsokKneeFlexEcc = np.array([])
#        ExpDataIsokHipExEcc = np.array([])
#        ExpDataIsokHipFlexEcc = np.array([])
#        
#        NExpDataIsokDFEcc = ExpDataIsokDFEcc/np.max(ExpDataIsokDFEcc)
#        NExpDataIsokPFEcc = ExpDataIsokPFEcc/np.max(ExpDataIsokPFEcc)
#        NExpDataIsokKneeExEcc = ExpDataIsokKneeExEcc/np.max(ExpDataIsokKneeExEcc)
#        NExpDataIsokKneeFlexEcc = ExpDataIsokKneeFlexEcc/np.max(ExpDataIsokKneeFlexEcc)
#        NExpDataIsokHipExEcc = ExpDataIsokHipExEcc/np.max(ExpDataIsokHipExEcc)
#        NExpDataIsokHipFlexEcc = ExpDataIsokHipFlexEcc/np.max(ExpDataIsokHipFlexEcc)
    elif S ==10:
        ExpDataIsomDF = np.array([2.13E+01, 2.55E+01, 2.89E+01, 3.49E+01, 4.41E+01, 4.47E+01])
        ExpDataIsomPF = np.array([1,1,1,1,1,1])
        ExpDataIsomKneeEx = np.array([1,1,1,1,1,1])
        ExpDataIsomKneeFlex = np.array([1,1,1,1,1,1])
        ExpDataIsomHipEx = np.array([1,1,1,1,1,1])
        ExpDataIsomHipFlex = np.array([1,1,1,1,1,1])
#        
#        NExpDataIsomDF = ExpDataIsomDF/np.max(ExpDataIsomDF)
#        NExpDataIsomPF = ExpDataIsomPF/np.max(ExpDataIsomPF)
#        NExpDataIsomKneeEx = ExpDataIsomKneeEx/np.max(ExpDataIsomKneeEx)
#        NExpDataIsomKneeFlex = ExpDataIsomKneeFlex/np.max(ExpDataIsomKneeFlex)
#        NExpDataIsomHipEx = ExpDataIsomHipEx/np.max(ExpDataIsomHipEx)
#        NExpDataIsomHipFlex = ExpDataIsomHipFlex/np.max(ExpDataIsomHipFlex)
        
#        ExpDataIsokDFCon = np.array([])
#        ExpDataIsokPFCon = np.array([])
#        ExpDataIsokKneeExCon = np.array([])
#        ExpDataIsokKneeFlexCon = np.array([])
#        ExpDataIsokHipExCon = np.array([])
#        ExpDataIsokHipFlexCon = np.array([])
#        
#        NExpDataIsokDFCon = ExpDataIsokDFCon/np.max(ExpDataIsokDFCon)
#        NExpDataIsokPFCon = ExpDataIsokPFCon/np.max(ExpDataIsokPFCon)
#        NExpDataIsokKneeExCon = ExpDataIsokKneeExCon/np.max(ExpDataIsokKneeExCon)
#        NExpDataIsokKneeFlexCon = ExpDataIsokKneeFlexCon/np.max(ExpDataIsokKneeFlexCon)
#        NExpDataIsokHipExCon = ExpDataIsokHipExCon/np.max(ExpDataIsokHipExCon)
#        NExpDataIsokHipFlexCon = ExpDataIsokHipFlexCon/np.max(ExpDataIsokHipFlexCon)        
#        
#        ExpDataIsokDFEcc = np.array([])
#        ExpDataIsokPFEcc = np.array([])
#        ExpDataIsokKneeExEcc = np.array([])
#        ExpDataIsokKneeFlexEcc = np.array([])
#        ExpDataIsokHipExEcc = np.array([])
#        ExpDataIsokHipFlexEcc = np.array([])
#        
#        NExpDataIsokDFEcc = ExpDataIsokDFEcc/np.max(ExpDataIsokDFEcc)
#        NExpDataIsokPFEcc = ExpDataIsokPFEcc/np.max(ExpDataIsokPFEcc)
#        NExpDataIsokKneeExEcc = ExpDataIsokKneeExEcc/np.max(ExpDataIsokKneeExEcc)
#        NExpDataIsokKneeFlexEcc = ExpDataIsokKneeFlexEcc/np.max(ExpDataIsokKneeFlexEcc)
#        NExpDataIsokHipExEcc = ExpDataIsokHipExEcc/np.max(ExpDataIsokHipExEcc)
#        NExpDataIsokHipFlexEcc = ExpDataIsokHipFlexEcc/np.max(ExpDataIsokHipFlexEcc)
    else: 
        print('No experimental data on subject')
    return(ExpDataIsomDF, ExpDataIsomPF, ExpDataIsomKneeEx, ExpDataIsomKneeFlex, ExpDataIsomHipEx, ExpDataIsomHipFlex) 
#           ExpDataIsokDFCon,
#    ExpDataIsokPFCon,ExpDataIsokKneeExCon,ExpDataIsokKneeFlexCon,ExpDataIsokHipExCon,ExpDataIsokHipFlexCon,ExpDataIsokDFEcc,ExpDataIsokPFEcc,
#    ExpDataIsokKneeExEcc,ExpDataIsokKneeFlexEcc,ExpDataIsokHipExEcc,ExpDataIsokHipFlexEcc)