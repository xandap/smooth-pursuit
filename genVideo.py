import numpy as np

spf = 1./60
numCycles = 5
ballFreq = 0.4# Hz
periodTime = 1 / ballFreq# 2.5 seconds
totalTime = 1000 * periodTime * numCycles # in msec



for t in xrange(12500):
    time = np.linspace(t - 2 * spf, t, num=2)
    new_x = np.sin(2 * ballFreq * time)