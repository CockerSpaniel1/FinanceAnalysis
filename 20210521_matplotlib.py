# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:46:45 2021

@author: w
"""

import matplotlib.pyplot as plt

#ax = plt.subplot(111)
#ax.plot([1,2,3,4,5,6] , [1,2,3,4,5,6])


# ax1 = plt.subplot(211)
# ax1.plot([1,2,3,4,5,6] , [1,2,3,4,5,6])

# ax2 = plt.subplot(212)
# ax2.plot([1,2,3,4,5,6] , [6,5,4,3,2,1])

# ax1 = plt.subplot(121)
# ax1.plot([1,2,3,4,5,6] , [1,2,3,4,5,6])

# ax2 = plt.subplot(122)
# ax2.plot([1,2,3,4,5,6] , [6,5,4,3,2,1])



ax1 = plt.subplot(221)
ax1.plot([1,2,3,4,5,6] , [1,2,3,4,5,6], 'ro')

ax2 = plt.subplot(222)
ax2.plot([1,2,3,4,5,6] , [6,5,4,3,2,1], 'g-')


ax3 = plt.subplot(223)
ax3.plot([1,2,3,4,5,6] , [1,2,3,4,5,6], 'b--')

ax4 = plt.subplot(224)
ax4.plot([1,2,3,4,5,6] , [6,5,4,3,2,1])

plt.show()