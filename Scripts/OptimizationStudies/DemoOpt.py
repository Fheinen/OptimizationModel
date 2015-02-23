import numpy as np
import re
import copy
sens_type = 'fd,function'
Nfd = '6'

if (sens_type == 'fd,function'):
    mydvs = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11]
    d = re.findall(r'\d+', Nfd)
    q = max(d)
    mydvsq = len(mydvs)
    dmeo = mydvsq-int(float(q))
    b = [0]*mydvsq

for i in xrange(int(float(q))):
    b[i]= 0+i
for i in xrange(dmeo):
    c = int(float(q))+i
    b[c] = int(float(q))+i


sens_step = float(1e-06)
x = np.array([0.5, 1.2, 1.0])

if (sens_type == 'fd'):
    
    # Finite Differences
    dh = sens_step            
    xs = x
    k = 0
    for i in mydvs:
        xh = copy.copy(xs)
        xh[i] += dh
        
        # Variables Groups Handling
#        if opt_problem.use_groups:
#            xhg = {}
#            for group in group_ids.keys():
#                if (group_ids[group][1]-group_ids[group][0] == 1):
#                    xhg[group] = xh[group_ids[group][0]]
#                else:
#                    xhg[group] = xh[group_ids[group][0]:group_ids[group][1]]
#                #end
#            #end
#            xh = xhg
#        #end
        
        [fph,gph,fail] = opt_problem.obj_fun(xh, *args, **kwargs)
        if isinstance(fph,float):
            fph = [fph]
        #end
        
        for j in xrange(len(opt_problem._objectives.keys())):
            dfi[j,k] = (fph[j] - f[j])/dh
        #end
        for j in xrange(len(opt_problem._constraints.keys())):
            dgi[j,k] = (gph[j] - g[j])/dh
        #end
        k += 1
    #end