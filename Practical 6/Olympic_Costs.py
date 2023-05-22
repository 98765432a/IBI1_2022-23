import numpy as np
import matplotlib.pyplot as plt

Olympic_Games=['Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens   2003','Beijing  2008','London 2012']
costs=[1,8,15,7,5,14,43,40]

#we use this method by the instruction of Hugo Carlos Samano Sanchez
Olympic_Games=np.array(Olympic_Games)#import the list as array
costs=np.array(costs)#put the lists into array    
order=costs.argsort()
sortedcosts=sorted(costs)#sorting lists
print(sortedcosts)
ordered_Olympic_Games=Olympic_Games[order]#connect the data in Olympic_Games with costs after sorting
print(ordered_Olympic_Games)

N=8#the number of groups
ind=np.arange(N)#the locations for the groups on the x axis
width=0.7#the width between bars are 0.7 
pl=plt.bar(ind,sortedcosts,width,edgecolor="r",color="gold")#plot a histogram and define its style
plt.ylabel('costs')#the index of y axis
plt.title('Olympic Costs',color="gold")#add a title and define the color of the title
plt.xticks(ind,ordered_Olympic_Games,rotation=30)#define the style of indes in x axis 
plt.yticks(np.arange(0,60,5))#the range of y axis is from 0 to 80,the space between each numbers on the Y axis is 5
plt.show()#show the plot
