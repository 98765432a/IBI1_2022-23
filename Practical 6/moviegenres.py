movie={'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
#creat a dictionary,movie genre as index,No.	students	for	which	this genre	is	their	favourite as element
import numpy as np
import matplotlib.pyplot as plt #import python packages
labels='Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'#import the labels
sizes=[73,42,38,28,22,19,18,12,8,7]#import the value of the labels accordingly
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)#make a pie chart,and define the style of the pie chart
plt.axis('equal')#ensure that pie is drawn as a circle.
plt.show()#print the pie chart
x='Comedy'
print(movie[x])#the number of students who prefer Comedy(a movie genre) from the list

