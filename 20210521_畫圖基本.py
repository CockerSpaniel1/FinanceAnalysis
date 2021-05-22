import matplotlib.pyplot as plt

# ax=plt.subplot(111)
# ax.plot([1,2,3,4,5,6],[1,2,3,4,5,6])

ax1=plt.subplot(211)
ax1.plot([1,2,3,4,5,6],[1,2,3,4,5,6],'r--')

ax2=plt.subplot(212)
ax2.plot([1,2,3,4,5,6],[6,5,4,3,2,1],'g-')

plt.show()
