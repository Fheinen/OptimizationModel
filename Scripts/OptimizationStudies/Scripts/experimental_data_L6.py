# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:18:27 2013

@author: RIGAUD Thomas
"""
from numpy import array

isoplantarflexor = array([
[61.66],
[108.24],
[118.10],
[126.12],
[170.32]
])
conplantarflexor = array([
[133.10],
[91.16],
[101.69],
[83.77]
])
eccplantarflexor = array([
[143.37],
[117.13],
[119.10],
[127.33]
])
isodorsiflexor = array([
[38.73],
[32.09],
[27.17],
[25.87],
[18.09]
])
condorsiflexor = array([
[32.29],
[31.31],
[24.12],
[19.31]
])
eccdorsiflexor = array([
[53.06],
[55.81],
[53.58],
[57.32]
])


norm_factor = isoplantarflexor[4,:]

isoplantarflexor_normalized = isoplantarflexor/norm_factor
conplantarflexor_normalized = conplantarflexor/norm_factor
eccplantarflexor_normalized = eccplantarflexor/norm_factor
isodorsiflexor_normalized = isodorsiflexor/norm_factor
condorsiflexor_normalized = condorsiflexor/norm_factor
eccdorsiflexor_normalized = eccdorsiflexor/norm_factor