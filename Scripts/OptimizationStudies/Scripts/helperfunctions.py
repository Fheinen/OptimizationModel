import numpy as np

string = """0.819  1.181  0.595  1.156  0.624  1.216  0.373  1.448  0.773  1.449
 0.59   1.034  0.77   1.039  0.585  1.108  0.791  1.396  0.373  1.034
 0.798  1.223  0.894  0.025
"""
arr = np.fromstring(string, sep = ' ')


print 'rmin', arr[:-2:2].__repr__()
print 'rmax', arr[1:-1:2].__repr__()
print 'scale', arr[-2].__repr__()
print 'm arm', arr[-1].__repr__()
