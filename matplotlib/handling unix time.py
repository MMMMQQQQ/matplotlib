import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
from urllib.request import urlopen


import matplotlib.dates as mdates

def bytespdate2num(fmt,encoding='utf-8'):
    # this number means byte
    strconverter=mdates.strpdate2num(fmt)
    # this function decode byte to the number(utf-8)
    def bytesconverter(b):
        # b is the byte, s is the string
        s=b.decode(encoding)
        return strconverter(s)
    # il will return the s
    return bytesconverter


def graph_data(stock):

    #
    fig=plt.figure()
    # this make ue can have many subplots
    ax1=plt.subplot2grid((1,1),(0,0))

    # the stock is the place where we install the dynamic stock
    stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'

    source_code=urllib.request.urlopen(stock_price_url).read().decode()

    stock_data=[]
    # separate the source by the new line
    split_source=source_code.split('\n')
    for line in split_source[1:]:
        split_line=line.split(',')
        if len(split_line)==7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date,closep,highp,lowp,openp,adj_closep,volume=np.loadtxt(stock_data,
                                                   delimiter=',',
                                                   unpack=True
                                                   )
    # now we need convert the date time
    dateconv=np.vectorize(dt.datetime.fromtimestamp)
    date=dateconv(date)
    # date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
    #                                                                   delimiter=',',
    #                                                                   unpack=True,
    #                                                                   converters={0: bytespdate2num('%Y-%m-%d')})


    ax1.plot_date(date,closep,'-',label='Price')
    for label in ax1.xaxis.get_ticklabels():
        # make the a label rotate 45 degree
        label.set_rotation(45)

    ax1.grid(True)#,color='g',linestyle='-',linewidth=5)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('stack plot')
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.16,right=0.9,top=0.95,wspace=0.2,hspace=0)
    plt.show()

graph_data('TSLA')
