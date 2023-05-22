#calculate the first 5 numbers of distinct dots in a pattern of dots consisting of the outlines of regular hexagons over the increasing number of regular hexagons 
n=0#n=the number of regular hexagons
for i in range (1,6): #the for loop was repeated 5 times
	n=n+1#let the number of regular hexagons ascend from 1 to 5
	h=2*n*(2*n-1)/2  #calculate the number of distinct dots in a pattern of dots consisting of the outlines of regular hexagons
	print(h)  #print out the outcomes
