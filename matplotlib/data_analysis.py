import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime

fh=open("2017-08-24 au 2017-08-30 Export Vannes et niveaux.txt")
reader=csv.reader(fh,delimiter='\t')
entete=next(reader)
data=[data for data in reader]
data_array=np.asarray(data)

# my_xticks=[]

y1=[]
y2=[]

# for i in range(len(data_array[:,1])):
#     my_xticks.append(data_array[i][1])

# x=np.arange(0,493500,10)
# x=list(x)

# plt.xticks(x,my_xticks)


for i in range(len(data_array[:,7])):
    # data_array[i][7]=float(data_array[i][7])
    y1.append(data_array[i][7])

for i in range(len(data_array[:,9])):
    y2.append(data_array[i][9])



for i in range(len(y1)):
    y1[i]=float(y1[i].replace(',','.'))


for i in range(len(y2)):
    y2[i]=float(y2[i].replace(',','.'))


# this is the function to change the integer that i have got using the "0+10*(i-1)" to the datetime
def newTime(customdate,seconde):
    sdelta=datetime.timedelta(seconds=seconde)
    return customdate+sdelta



# plt.plot(x,y1,'r')
# plt.plot(x,y2,'b')
# plt.show()
y1=y1[6164:40327]
y2=y2[6164:40327]
customdate = datetime.datetime(2017, 8, 25, 11, 33, 33)
x = [customdate + datetime.timedelta(seconds=i*10) for i in range(len(y1))]


fig = plt.figure()

ax = plt.subplot(111)
ax.plot(x, y1, color='b', label='Niveau Mer')
# [6164:40327]
ax.plot(x, y2, color='r',label='Niveau Estuaire')
plt.title('Niveau Mer et Niveau Estuaire du 2017-08-24 au 2017-08-30')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)


plt.xlabel('temps')
plt.ylabel('niveau')

xcoords = [102000-61640, 103551-61640, 146215-61640, 147699-61640, 190128-61640, 191398-61640, 234818-61640, 235651-61640, 278418-61640, 279269-61640, 323340-61640, 323459-61640, 366756-61640, 367000-61640]
tIn=[]
for i in range(len(xcoords)):
    tIn.append(newTime(customdate,xcoords[i]))

for xc in tIn:
    plt.axvline(x=xc,color="r",linestyle='--')

plt.grid()
plt.show()





# from the observation, we can know that the
# frst VD: "93440(2017-08-25 20:23:43): 102000(2017-08-25 22:46:23); OI 103551(2017-08-25 23:12:14)" --------->
# the second VD begins at "137796(2017-08-26 08:42:59)  146215(2017-08-26 11:03:18)", OI:147699(2017-08-26 11:28:02)"
# the third VD: 181941(2017-08-26 20:58:44) 190128(2017-08-26 23:15:11); OI: 191398(2017-08-26 23:36:21)
# forth: VD: 225766(2017-08-27 09:09:09)  234818(2017-08-27 11:40:01);  OI: 235651(2017-08-27 11:53:54)
# fifth VD: 269829(2017-08-27 21:23:32)   278418(2017-08-27 23:46:41);  OI: 279269(2017-08-28 00:00:52)
# sixth VD: 313963(2017-08-28 09:39:06)    323340(2017-08-28 12:15:23);  OI:323459(2017-08-28 12:17:22)
# seventh VD:358426(2017-08-28 22:00:09 )  366756(2017-08-29 00:18:59);  OI:367000(2017-08-29 00:23:03)