import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,6,7]

# 's' is used to change the size of marker
plt.scatter(x,y,label='skitscat',color='k',marker='*',s=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()