from peyetribe import EyeTribe
import math
import time
import matplotlib.pyplot as plt # For ploting
from matplotlib import animation
import numpy as np # to work with numerical data efficiently
import pickle

## will use this incorporate key presses to advance screen
# def press(event):
#     global on
#     print('press', event.key)
#     if event.key == 'esc':
#         on = 0
#     if event.key == 'enter':
#         on = 1
#     return on

fig, ax = plt.subplots()
fps = 60
spf = 1. / fps #Seconds Per Frame
cont = False
on = 1
fig.set_facecolor('0.50')
plt.axis('off')
cid = plt.gcf().canvas.mpl_connect('key_press_event', press)

tracker = EyeTribe() #create object tracker for connection
tracker.connect()
n = tracker.next()

numberoftrials = 6
targetFrequency = 0.4 #Hz

#initialize empty arrays
timestamp = [] #time in msec
lefteye = [] #left in rawx, rawy, avgx, avgy
righteye = [] #right eye in rawx, rawy, avgx, avgy
starttime = [] #timestamp (msec) for sync beginnning
endtime =[] # " " for ending

## format of eyetribe server output
#print("eT;dT;aT;Fix;State;Rwx;Rwy;Avx;Avy;LRwx;LRwy;LAvx;LAvy;LPSz;LCx;LCy;RRwx;RRwy;RAvx;RAvy;RPSz;RCx;RCy")

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
    ## horizontal
    if block == 1:
        #wait ON break screen until keypress OR 15 seconds
        t0 = time.time() #where is best to put this?
        points, = ax.plot(0, 0, marker='o', markersize=1, linestyle='None', color='0.50')
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        if press.event() == 'enter' or time.time()-t0 > 15: #check this too for key press
            # show fixation cross
            points, = ax.plot(0, 0, marker='+', markersize=25, markeredgewidth=2, linestyle='None', color='b')
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            # stimulus 1
            starttime.append(n.time)
            for t in xrange(200): #gotta work on timing to make sure accurate/reliable
                print cont
                print on
                if t == 0:
                    points, = ax.plot(0, 0, marker='o', markersize=5, linestyle='None', color='r')
                    ax.set_xlim(-1.1, 1.1)
                    ax.set_ylim(-1.1, 1.1)
                else:
                    t /= 10.
                    t_arr = np.linspace(t - 2 * spf, t, num=2)  # Makes a trail
                    new_x = np.sin(targetFrequency*np.asarray(t_arr))
                    new_y = np.zeros(len(t_arr))
                    points.set_data(new_x, new_y)
                plt.pause(spf)
            endtime.append(n.time)
            #advance to break screen
            if trial > numberoftrials:#if over number of trials
                block = 2 #move on to next block of stimuli
                trial = 1 #reset trial
            else:
                timestamp = np.array(timestamp)  # make numpy array
                lefteye = np.array(lefteye)
                righteye = np.array(righteye)
                starttime = np.array(starttime)  # make numpy array
                endtime = np.array(endtime)
                with open(('firstBlock_'+str(trial)+'.pickle'), 'w') as f:
                    pickle.dump([timestamp, lefteye, righteye, starttime, endtime], f)
                timestamp, lefteye, righteye, starttime, endtime = ([] for i in range(5))
                trial += 1  # repeat another trial
    ## vertical
    if block == 2:
        # wait ON break screen until keypress OR 15 seconds
        t0 = time.time()  # where is best to put this?
        points, = ax.plot(0, 0, marker='o', markersize=1, linestyle='None', color='0.50')
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        if press.event() == 'enter' or time.time() - t0 > 15:  # check this too for key press
            # show fixation cross
            points, = ax.plot(0, 0, marker='+', markersize=25, markeredgewidth=2, linestyle='None', color='b')
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            # stimulus 1
            starttime.append(n.time)
            for t in xrange(150):  # gotta work on timing to make sure accurate/reliable
                print cont
                print on
                if t == 0:
                    points, = ax.plot(0, 0, marker='o', markersize=5, linestyle='None', color='r')
                    ax.set_xlim(-1.1, 1.1)
                    ax.set_ylim(-1.1, 1.1)
                else:
                    t /= 10.
                    t_arr = np.linspace(t - 2 * spf, t, num=2)  # Makes a trail
                    new_x = np.zeros(len(t_arr))
                    new_y = np.sin(targetFrequency*np.asarray(t_arr))
                    points.set_data(new_x, new_y)
                plt.pause(spf)
            endtime.append(n.time)
            # advance to break screen
            if trial > numberoftrials:  # if over number of trials
                block = 3  # move on to next block of stimuli
                trial = 1  # reset trial
            else:
                timestamp = np.array(timestamp)  # make numpy array
                lefteye = np.array(lefteye)
                righteye = np.array(righteye)
                starttime = np.array(starttime)  # make numpy array
                endtime = np.array(endtime)
                with open(('secondBlock_' + str(trial) + '.pickle'), 'w') as f:
                    pickle.dump([timestamp, lefteye, righteye, starttime, endtime], f)
                timestamp, lefteye, righteye, starttime, endtime = ([] for i in range(5))
                trial += 1  # repeat another trial
    ## diagonal
    if block == 3:
        # wait ON break screen until keypress OR 15 seconds
        t0 = time.time()  # where is best to put this?
        points, = ax.plot(0, 0, marker='o', markersize=1, linestyle='None', color='0.50')
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        if press.event() == 'enter' or time.time() - t0 > 15:  # check this too for key press
            # show fixation cross
            points, = ax.plot(0, 0, marker='+', markersize=25, markeredgewidth=2, linestyle='None', color='b')
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            # stimulus 1
            starttime.append(n.time)
            for t in xrange(150):  # gotta work on timing to make sure accurate/reliable
                print cont
                print on
                if t == 0:
                    points, = ax.plot(0, 0, marker='o', markersize=5, linestyle='None', color='r')
                    ax.set_xlim(-1.1, 1.1)
                    ax.set_ylim(-1.1, 1.1)
                else:
                    t /= 10.
                    t_arr = np.linspace(t - 2 * spf, t, num=2)  # Makes a trail
                    new_x = np.cos(targetFrequency*np.asarray(t_arr))
                    new_y = np.sin(targetFrequency*np.asarray(t_arr))
                    points.set_data(new_x, new_y)
                plt.pause(spf)
            endtime.append(n.time)
            # advance to break screen
            if trial > numberoftrials:  # if over number of trials
                block = 4  # move on to next block of stimuli
                trial = 1  # reset trial
            else:
                timestamp = np.array(timestamp)  # make numpy array
                lefteye = np.array(lefteye)
                righteye = np.array(righteye)
                starttime = np.array(starttime)  # make numpy array
                endtime = np.array(endtime)
                with open(('thirdBlock_' + str(trial) + '.pickle'), 'w') as f:
                    pickle.dump([timestamp, lefteye, righteye, starttime, endtime], f)
                timestamp, lefteye, righteye, starttime, endtime = ([] for i in range(5))
                trial += 1  # repeat another trial
    ## elliptical
    if block == 4:
            # wait ON break screen until keypress OR 15 seconds
            t0 = time.time()  # where is best to put this?
            points, = ax.plot(0, 0, marker='o', markersize=1, linestyle='None', color='0.50')
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            if press.event() == 'enter' or time.time() - t0 > 15:  # check this too for key press
                # show fixation cross
                points, = ax.plot(0, 0, marker='+', markersize=25, markeredgewidth=2, linestyle='None', color='b')
                ax.set_xlim(-1.1, 1.1)
                ax.set_ylim(-1.1, 1.1)
                # stimulus 1
                starttime.append(n.time)
                for t in xrange(150):  # gotta work on timing to make sure accurate/reliable
                    print cont
                    print on
                    if t == 0:
                        points, = ax.plot(0, 0, marker='o', markersize=5, linestyle='None', color='r')
                        ax.set_xlim(-1.1, 1.1)
                        ax.set_ylim(-1.1, 1.1)
                    else:
                        t /= 10.
                        t_arr = np.linspace(t - 2 * spf, t, num=2)  # Makes a trail
                        new_x = np.cos(t_arr)
                        new_y = np.sin(t_arr)
                        points.set_data(new_x, new_y)
                    plt.pause(spf)
                endtime.append(n.time)
                # advance to break screen
                if trial > numberoftrials:  # if over number of trials
                    on = 0  # break out of while loop
                    print('All blocks have been presented. Experiment complete.')
                else:
                    timestamp = np.array(timestamp)  # make numpy array
                    lefteye = np.array(lefteye)
                    righteye = np.array(righteye)
                    starttime = np.array(starttime)  # make numpy array
                    endtime = np.array(endtime)
                    with open(('fourthBlock_' + str(trial) + '.pickle'), 'w') as f:
                        pickle.dump([timestamp, lefteye, righteye, starttime, endtime], f)
                    timestamp, lefteye, righteye, starttime, endtime = ([] for i in range(5))
                    trial += 1  # repeat another trial

tracker.pullmode()
tracker.close() # close connection with server

# with open('objs.pickle') as f:  # Python 3: open(..., 'rb')
#     #obj0, obj1, obj2 = pickle.load(f)





