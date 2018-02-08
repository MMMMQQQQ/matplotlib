import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime

fh=open("finance_data/CLS-IDH.csv")
reader=csv.reader(fh,delimiter='\t')
entete=next(reader)
data=[data for data in reader]
data_array=np.asarray(data)

# x1=[]
dataCollect=[]
# print(data_array[1])
# print(len(data_array))
# x1=data_array[0][0].split(',')
# print(x1)
for i in range(len(data_array)):
    dataCollect.append(data_array[i][0].split(','))

print(dataCollect)

customdate = datetime.date(2017, 7, 3)
x = [customdate + datetime.timedelta(day=i) for i in range(len(y1))]



#
# y1=[]
# y2=[]
#
#
#
# for i in range(len(data_array[:,2])):
#     # data_array[i][7]=float(data_array[i][7])
#     y1.append(data_array[i][2])
#
# for i in range(len(data_array[:,5])):
#     y2.append(data_array[i][5])
#
#
#
# for i in range(len(y1)):
#     y1[i]=float(y1[i].replace(',','.'))
#
#
# for i in range(len(y2)):
#     y2[i]=float(y2[i].replace(',','.'))
#
#
# # this is the function to change the integer that i have got using the "0+10*(i-1)" to the datetime
# def newTime(customdate,seconde):
#     sdelta=datetime.timedelta(seconds=seconde)
#     return customdate+sdelta
#
#
#
#
# y1=y1[6164:40327]
# y2=y2[6164:40327]
# customdate = datetime.datetime(2017, 8, 25, 11, 33, 33)
# x = [customdate + datetime.timedelta(seconds=i*10) for i in range(len(y1))]
#
#
# fig = plt.figure()
#
# ax = plt.subplot(111)
# ax.plot(x, y1, color='b', label='Niveau Mer')
# # [6164:40327]
# ax.plot(x, y2, color='r',label='Niveau Estuaire')
# plt.title('Niveau Mer et Niveau Estuaire du 2017-08-24 au 2017-08-30')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)
#
#
# plt.xlabel('temps')
# plt.ylabel('niveau')
#
# xcoords = [102000-61640, 103551-61640, 146215-61640, 147699-61640, 190128-61640, 191398-61640, 234818-61640, 235651-61640, 278418-61640, 279269-61640, 323340-61640, 323459-61640, 366756-61640, 367000-61640]
# tIn=[]
# for i in range(len(xcoords)):
#     tIn.append(newTime(customdate,xcoords[i]))
#
# for xc in tIn:
#     plt.axvline(x=xc,color="r",linestyle='--')
#
# plt.grid()
# plt.show()

