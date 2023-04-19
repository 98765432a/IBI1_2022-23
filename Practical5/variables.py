#calculate distances between Edinburgh to Los Angeles and Edinburgh to Haining

a=-3.19#the longitude of Edinburgh
b=-118.24#the longitude of Los Angeles
c=116.39#the longitude of Haining
d=a-b #Calculate	the	longitude	distance	that	Rob	travelled	to	Los	Angeles
e=c-a #Calculate	the	longitude	distance	that	Rob	travelled	to	Haining
x=d>e#whether or not the longitude distance that Rob travels to Los Angeles is longer than to Haining
print("Is the longitude distance that Rob travels to Los Angeles longer than to Haining?")
print(x)#the output will be true or false


#another practical for boolean

x=1>=1#1>=1 is true
y=5>6#5>6 is false
w=x and y#true and false = false
z=x or y#true or false=true
print(w)#print false
print(z)#print true

