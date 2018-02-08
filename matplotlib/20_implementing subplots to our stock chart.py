import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style

import numpy as np
import urllib
import datetime as dt

style.use('ggplot')
print(plt.style.available)



def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 1), (0, 0),rowspan=1,colspan=1)
    plt.title(stock)
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)


    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})

    x=0
    y=len(date)
    ohlc=[]

    while x<y:
        append_me=date[x], closep[x], highp[x], lowp[x], openp[x], adj_closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    candlestick_ohlc(ax2,ohlc,width=0.4,colorup='g',colordown='r')
    # ax1.plot(date,closep)
    # ax1.plot(date, openp)

    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # set how many point to show in the x label
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.grid(True)
    # xytext=date[-1]+4 means that we will move the text outside the graphe
    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    ax2.annotate(str(closep[10]), (date[12], closep[12]),
                 xytext = (date[12], closep[12]), bbox=bbox_props)

    # # Annotation example with arrow
    # # add annotation
    # ax1.annotate('Big News!',(date[11],highp[11]),
    #              xytext=(0.8,0.9),textcoords='axes fraction',
    #              arrowprops=dict(facecolor='grey',color='grey'))
    #
    # # font dict example
    # # add the texts on the plot
    # font_dict={'family':'serif',
    #            'color':'darkred',
    #            'size':15}
    # ax1.text(date[10],closep[1],'Text Example',fontdict=font_dict)


    # plt.title(stock)
    # plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')