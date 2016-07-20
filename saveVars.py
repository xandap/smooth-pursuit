# saves variables as csv
import numpy as np
import pandas as pd


def saveVars(block, trial, timestamp, lefteye, righteye, starttime):
    timestamp = np.array(timestamp)  # make numpy array
    lefteye = np.array(lefteye)
    righteye = np.array(righteye)
    starttime = np.array(starttime)  # make numpy array
    df = pd.DataFrame({'Time': timestamp,
                       'LeftEye': lefteye,
                       'RightEye': righteye,
                       'StartTime': starttime})
    df.to_csv('block' + str(block) + 'trial' + str(trial) + '.csv')


