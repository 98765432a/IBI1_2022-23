def calculate(house,salary):
	"""calculate how many times the price of house is higher than the annual salary
        if the calculation is bigger than 5
        then we can buy the house"""
	print('whether buy a house in the UK')
	if (house/salary)<5:#calculate if the price of house is less than five times of salary
		print('Yes')
	else:
		print('No')
c=calculate(180000,3500)#input house price and salary.for example,house price=180000,salary=35000,he/she can't bind the house
#housep=input('please enter the house price here:')#input data
#salarym=input('please enter your annual salary here:')#input data
#c=Coordinate(int(housep),int(salarym))#change the input into intergers
