from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import style

style.use('fivethirtyeight')

fig=plt.figure()

ax1=fig.add_subplot(111,projection='3d')

x,y,z=axes3d.get_test_data()
# this prints the location of the file
print(axes3d.__file__)
# the distance between the lines
ax1.plot_wireframe(x,y,z,rstride=5,cstride=5)


ax1.set_xlabel('x_labels')
ax1.set_ylabel('y_labels')
ax1.set_zlabel('z_labels')
plt.show()