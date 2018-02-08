import matplotlib.pyplot as plt
import numpy as np

# Part 1
'''
import csv
# using csv to open the txt file

x=[]
y=[]

with open('example.txt','r') as csvfile:
    # delimiter means separate by
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='Loaded from file')
'''

x,y=np.loadtxt('example.txt',delimiter=',',unpack=True)

plt.plot(x,y,label='Load file using numpy')

plt.xlabel('x')
plt.ylabel('y')
plt.title('stack plot')
plt.legend()
plt.show()