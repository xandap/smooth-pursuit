import numpy as np
import pickle

spf = 1./60
numCycles = 5
ballFreq = 0.4# Hz
periodTime = 1 / ballFreq# 2.5 seconds
totalTime = 1000 * periodTime * numCycles # in msec
new_x = []
time = []

for t in xrange(12500):
    time = np.linspace(t - 2 * spf, t, num=2)
    new_x = np.sin(2 * ballFreq * time)
    t =
with open('time.pickle', 'w') as f:
    pickle.dump([time, new_x], f)