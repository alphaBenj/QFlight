#!/usr/bin/python

import matplotlib.pyplot as plt

def plot2Axes(X,Y1,Y2,Y3,date,title,showName="Blank", c ="k-"):
    plt.figure(figsize=(16,6), dpi=125);
    fig, ax1 = plt.subplots();
    ax1.grid(linewidth=0.1) ;
    ax1.plot(X, Y1,  c, label="Close Data")
    ax1.plot(X, Y3,  'g-' ,label="VWAP")
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Period Data', color='k')
    ax1.tick_params(axis='x', labelrotation=90)
    ax1.xaxis.set_major_locator(plt.MaxNLocator(30))
    
    ax2 = ax1.twinx()
    ax2.plot(X, Y2, 'b:',label="NN Mean Close Prices")
    ax2.set_ylabel('Period Mean Data', color='b')
    ax1.legend(loc='upper right')
    ax2.legend(loc='lower right')
    title += " for %s" %  (date)
    plt.title(title)
    return plt.show();
