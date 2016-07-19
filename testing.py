# import numpy as np
#
#
# totalTime = 15
# targetFrequency = 0.4
#
# t_arr = np.linspace(0, totalTime, 100) # totalTime/1
# x = np.sin(targetFrequency*np.asarray(t_arr))
# y = 7*np.sin(targetFrequency*np.asarray(t_arr))
# print ('x:', x)
# print ('y:', y)
#
import matplotlib.pyplot as plt
from showFixation import showFixation as showFix

showFix('+', 25, 'r')

plt.show()