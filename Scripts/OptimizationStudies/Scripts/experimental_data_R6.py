# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:18:27 2013

@author: RIGAUD Thomas
"""
from numpy import array

isoplantarflexor = array([
[58.22],
[92.96],
[129.27],
[158.22],
[147.25]
])
conplantarflexor = array([
[184.97],
[169.73],
[116.90],
[103.10]
])
eccplantarflexor = array([
[197.97],
[181.63],
[157.17],
[154.60]
])
isodorsiflexor = array([
[38.60],
[34.94],
[32.33],
[30.00],
[22.01]
])
condorsiflexor = array([
[28.11],
[24.51],
[19.34],
[13.98]
])
eccdorsiflexor = array([
[45.78],
[48.21],
[48.29],
[44.76]
])


norm_factor = eccplantarflexor[0,:]

isoplantarflexor_normalized = isoplantarflexor/norm_factor
conplantarflexor_normalized = conplantarflexor/norm_factor
eccplantarflexor_normalized = eccplantarflexor/norm_factor
isodorsiflexor_normalized = isodorsiflexor/norm_factor
condorsiflexor_normalized = condorsiflexor/norm_factor
eccdorsiflexor_normalized = eccdorsiflexor/norm_factor