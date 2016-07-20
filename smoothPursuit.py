from peyetribe import EyeTribe
import time
import matplotlib.pyplot as plt # For ploting
import numpy as np # to work with numerical data efficiently
from showFixation import showFixation
from saveVars import saveVars
from keyListen import *

## format of eyetribe server output
#print("eT;dT;aT;Fix;State;Rwx;Rwy;Avx;Avy;LRwx;LRwy;LAvx;LAvy;LPSz;LCx;LCy;RRwx;RRwy;RAvx;RAvy;RPSz;RCx;RCy")

def runSimulation(block):
    if block == 1:
        #wait ON break screen until keypress OR 15 seconds
        t0 = time.time() #where is best to put this?
        showFixation('o', 1, '0.5')
        if ANYKEY or time.time()-t0 > 15: #check this too for key press
            showFixation('+', 25, 'b') #show fixation cross
            # TRIED EXPERIMENTING HERE
            ## load('block1.avi') ##
            t1 = time.time()
            if time.time() - t1 > 5:
                starttime.append(n.time)
    ## vertical
    if block == 2:
        t0 = time.time()
        showFixation('o', 1, '0.5')
        if press.event() == 'enter' or time.time() - t0 > 15:
            showFixation('+', 25, 'b')
            starttime.append(n.time)
            ## load('block2.avi') ##
            t1 = time.time()
            if time.time() - t1 > 5:
                starttime.append(n.time)
    ## diagonal
    if block == 3:
        t0 = time.time()
        showFixation('o', 25, '0.5')
        if press.event() == 'enter' or time.time() - t0 > 15:
            showFixation('+', 25, 'b')
            ## load('block3.avi') ##
            t1 = time.time()
            if time.time() - t1 > 5:
                starttime.append(n.time)

    if block == 4: ## elliptical
        t0 = time.time()
        showFixation('o', 25, '0.5')
        if press.event() == 'enter' or time.time() - t0 > 15:
            showFixation('+', 25, 'b')
            ## load('block4.avi') ##
            t1 = time.time()
            if time.time() - t1 > 5:
                starttime.append(n.time)

tracker = EyeTribe() #create object tracker for connection
tracker.connect()
n = tracker.next()

numberoftrials = 6
fps = 60
spf = 1. / fps #Seconds Per Frame
targetFrequency = 0.4 #Hz

#initialize empty arrays <-- this is process i found necessary to read in the data from the eye tracker heart beat
timestamp = [] #time in msec
lefteye = [] #left in rawx, rawy, avgx, avgy
righteye = [] #right eye in rawx, rawy, avgx, avgy
starttime = [] #timestamp (msec) for sync beginnning

tracker.pushmode() #begin pushing
on = 1 #variable to exit while loop. always 1 until 'esc' or end of block 4
block = 1 #stimulus block advancement variable - added to after finishing a block
trial = 1 #trial number for each block. resets to 1 when subject advances to next block


while on == 1:
    # should this go here?
    n = tracker.next()
    timestamp.append(n.time) #append time
    lefteye.append(n.lefteye) #append left eye in rawx, rawy, avgx, avgy
    righteye.append(n.righteye) #append right eye in rawx, rawy, avgx, avgy
    runSimulation(block)
    if trial > numberoftrials:  # if over number of trials
        block += 1  # move on to next block of stimuli
        trial = 1  # reset trial
    else:
        saveVars(block, trial, timestamp, lefteye, righteye, starttime)
        timestamp, lefteye, righteye, starttime = ([] for i in range(4))
        trial += 1  # repeat another trial
    if block == 5:
        print('All blocks have been presented. Experiment complete.')
        on = 0

tracker.pullmode()
tracker.close() # close connection with server

# with open('objs.pickle') as f:  # Python 3: open(..., 'rb')
#     #obj0, obj1, obj2 = pickle.load(f)





