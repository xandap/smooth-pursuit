# saves variables in pickle object

import numpy as np
import pickle


def saveVars(trial, timestamp, lefteye, righteye, starttime, endtime):
    timestamp = np.array(timestamp)  # make numpy array
    lefteye = np.array(lefteye)
    righteye = np.array(righteye)
    starttime = np.array(starttime)  # make numpy array
    endtime = np.array(endtime)
    with open(('fourthBlock_' + str(trial) + '.pickle'), 'w') as f:
        pickle.dump([timestamp, lefteye, righteye, starttime, endtime], f)
