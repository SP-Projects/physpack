'''
The GraphPlotting submodule of the Physics-Analysis-Pack package.
Contains simple functions for plotting
'''
import matplotlib.pyplot as plt

def SinglePlot(x, y):
    '''
    SinglePlot(xData, yData):
    A simple pyplot based graphing tool to create a plot of a single piece of data
    '''

    #Create a figure to contain the plot and get the axes
    singleFig = plt.figure(0)
    singleAxe = singleFig.gca()
    singleAxe.plot(x, y)
    singleFig.show()
    return singleAxe