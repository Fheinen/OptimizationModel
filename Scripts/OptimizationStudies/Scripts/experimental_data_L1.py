# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:18:27 2013

@author: RIGAUD Thomas
"""
from numpy import array

isoplantarflexor = array([
[41.98],
[69.20],
[84.18],
[107.79],
[140.37]
])
conplantarflexor = array([
[112.40],
[95.48],
[81.10],
[30.89]
])
eccplantarflexor = array([
[123.47],
[127.10],
[114.47],
[133.80]
])
isodorsiflexor = array([
[27.23],
[24.02],
[22.28],
[19.70],
[13.90]
])
condorsiflexor = array([
[24.28],
[23.21],
[18.28],
[15.87]
])
eccdorsiflexor = array([
[37.23],
[37.47],
[38.42],
[39.05]
])


norm_factor = isoplantarflexor[4,:]

isoplantarflexor_normalized = isoplantarflexor/norm_factor
conplantarflexor_normalized = conplantarflexor/norm_factor
eccplantarflexor_normalized = eccplantarflexor/norm_factor
isodorsiflexor_normalized = isodorsiflexor/norm_factor
condorsiflexor_normalized = condorsiflexor/norm_factor
eccdorsiflexor_normalized = eccdorsiflexor/norm_factor