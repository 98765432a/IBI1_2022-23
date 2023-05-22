#each two rabbits generate 2 rabbits
#the first generation is a pair of rabbit
#count the total number of rabbits of each generation
#increase the generation
#loop
#if the total number of rabbits is bigger than 100
#exit loop
#print out the generation

n=1#the generation of rabbits
while 1==1:#to make a loop
        total=2**n #the total number of rabbits=2^n
        n=n+1#add a generation
        if total>100:
                print(n-1)
                break
