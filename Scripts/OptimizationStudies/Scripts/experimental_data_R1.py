# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:18:27 2013

@author: RIGAUD Thomas
"""
from numpy import array

isoplantarflexor = array([
[38.85],
[66.08],
[78.21],
[107.03],
[138.53]
])
conplantarflexor = array([
[138.83],
[131.80],
[98.80],
[78.30]
])
eccplantarflexor = array([
[149.27],
[157.80],
[124.83],
[104.67]
])
isodorsiflexor = array([
[27.86],
[21.86],
[18.53],
[16.54],
[11.06]
])
condorsiflexor = array([
[23.59],
[22.00],
[15.68],
[12.84]
])
eccdorsiflexor = array([
[36.00],
[35.44],
[38.45],
[34.32]
])


norm_factor = eccplantarflexor[1,:]

isoplantarflexor_normalized = isoplantarflexor/norm_factor
conplantarflexor_normalized = conplantarflexor/norm_factor
eccplantarflexor_normalized = eccplantarflexor/norm_factor
isodorsiflexor_normalized = isodorsiflexor/norm_factor
condorsiflexor_normalized = condorsiflexor/norm_factor
eccdorsiflexor_normalized = eccdorsiflexor/norm_factor