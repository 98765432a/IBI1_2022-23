costs=[1,8,15,7,5,14,43,40]
print(costs)

import numpy as np
import matplotlib.pyplot as plt

N=8
costs=[1,8,15,7,5,14,43,40]
ind=np.arange(N)#the locations for the groups on the x axis
width=0.7#the width between bars are 0.7
ax.hist(df['petal width'], width=[0.1],color='blue')
pl=plt.bar(ind,costs,width)
plt.ylabel('Cost')
plt.title('Olympic Costs')
plt.xticks(ind,('Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney	2000','Athens	2003','Beijing	2008','London 2012'))
plt.yticks(np.arange(0,81,10))

plt.show()
