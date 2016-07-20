import matplotlib.pyplot as plt

def showFixation(markerSymbol, markerSize, markerColor):
    ## load break.jpg (will make this jpg)
    ## after 15 seconds elapsed or key press continue to fixation.jpg
    fig, ax = plt.subplots()
    global points
    points, = ax.plot(0, 0, marker=markerSymbol, markersize=markerSize, linestyle='None',
                      color=markerColor)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    fig.set_facecolor('0.50')
    plt.axis('off')
    #plt.show()
    ## full screen here

    # F = gcf()
    # Size = F.get_size_inches()
    # F.set_size_inches(Size[0] * 2, Size[1] * 2, forward=True)






