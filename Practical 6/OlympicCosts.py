import numpy as np
import matplotlib.pyplot as plt
costs=[1,8,15,7,5,14,43,40]
costs1=sorted(costs)
print(costs1)#print a list of sorted values for the cost	of hosting the Summer Olympic Games

N=8
costs=[1,8,15,7,5,14,43,40]
ind=np.arange(N)#the locations for the groups on the x axis
width=0.7#the width between bars are 0.7 
pl=plt.bar(ind,costs,width,edgecolor="r",color="gold")#plot a histogram and define its style
plt.ylabel('Cost')#the index of y axis
plt.title('Olympic Costs',color="gold")
plt.xticks(ind,('Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney	2000','Athens	2003','Beijing	2008','London 2012'),rotation=30)#define the style of x axis
plt.yticks(np.arange(0,81,5))#the range of y axis is from 0 to 80,the space between each numbers on the Y axis is 5
plt.show()
