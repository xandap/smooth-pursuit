## use to show break or fixation page based on marker symbol
## break page: markerColor = bgColor = 0.5
## fixation page: '+', 25, 'r'

import matplotlib.pyplot as plt


def showFixation(markerSymbol, markerSize, markerColor):
    fig, ax = plt.subplots()
    global points
    points, = ax.plot(0, 0, marker=markerSymbol, markersize=markerSize, linestyle='None',
                      color=markerColor)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    fig.set_facecolor('0.50')
    plt.axis('off')
    F = gcf()
    Size = F.get_size_inches()
    F.set_size_inches(Size[0] * 2, Size[1] * 2, forward=True)






