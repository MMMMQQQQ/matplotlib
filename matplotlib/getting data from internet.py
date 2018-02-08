import matplotlib.pyplot as plt
import numpy as np
import urllib
from urllib.request import urlopen
import datetime

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
                                                   unpack=True,
                                                   # %Y full year 2015
                                                   # %y partial year 15
                                                   # %m month
                                                   # %M minute
                                                   # %d number day
                                                   # %H hours
                                                   # %S seconds
                                                   # 12-06-2015 %m-%d-%Y
                                                   converters={0:bytespdate2num('%Y-%m-%d')})


    plt.plot_date(date,closep,'-',label='Price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('stack plot')
    plt.legend()
    plt.show()

graph_data('TSLA')
