import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig=plt.figure()
# add an axis
ax1=fig.add_subplot(1,1,1)

def animate(i):
    graph_data=open('example.txt','r').read()
    # the character of separation is if the text is separated by the new line
    lines=graph_data.split('\n')
    xs=[]
    ys=[]

    for line in lines:
        # to ensure that the line is not totally empty
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs,ys)


ani=animation.FuncAnimation(fig, animate,interval=1000)
plt.show()