# saves variables in pickle object

import numpy as np
import pickle
import pandas as pd

def saveVars(block, trial, timestamp, lefteye, righteye, starttime, endtime):
    timestamp = np.array(timestamp)  # make numpy array
    lefteye = np.array(lefteye)
    righteye = np.array(righteye)
    starttime = np.array(starttime)  # make numpy array
    endtime = np.array(endtime)
    df = pd.DataFrame({'Time'    : timestamp,
                       'LeftEye' : lefteye,
                       'RightEye' : righteye,
                       'StartTime' : starttime,
                       'EndTime' : endtime})
    df.to_csv('block' + str(block) + 'trial' + str(trial) + '.csv')

    #with open(('block' + str(block) + 'trial' + str(trial) + '.pickle'), 'w') as f:
    #    pickle.dump([timestamp, lefteye, righteye, starttime, endtime], f)

