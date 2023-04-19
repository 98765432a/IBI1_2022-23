#use function
#print:whether buy a house in the UK

class Coordinate (object):#import a class
	def __init__(self,house,salary):#import a function
		print('whether buy a house in the UK')
		self.house=house
		self.salary=salary
		buy=self.house/self.salary#calculate how many times the price of house higher than annual salary
		if buy<5:
			print('Yes')
		else:
			print('No')
c=Coordinate(180000, 35000)	
housep=input('please enter the house price here:')#input data
salarym=input('please enter your annual salary here:')#input data
c=Coordinate(int(housep),int(salarym))#change the input into intergers
