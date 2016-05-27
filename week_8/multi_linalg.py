#
# An example stolen from the internet.  Not sure what the noted
# problems are all about.
#

import numpy as np
import multiprocessing as mp

def foo(x):
    print np.linalg.inv([[2,3],[2,2]]) #this causes the crash
    #print np.dot([[1,2],[3,4]],[[1,2],[3,4]]) # this works fine

def test():
    print "running..."
    print np.__version__
    print mp.__version__
    vals = [1,2,3,4]
    pool = mp.Pool(1) #This has an issue
    #pool = mp.Pool(mp.cpu_count()) #this has an issue
    pool.map(foo, vals)

if __name__ == "__main__":
    test()
    #foo(1) #this works fine
