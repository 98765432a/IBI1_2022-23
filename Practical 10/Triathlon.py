class Triathlon (object):#import a class
	def __init__(self, name, location, swim, cycle, run):#import a function
		"""define the name, location,of athlete and their record of swim, cycle and run(assume them in the same unit)
		add the scores together
		print out the outcome"""
		self.name=name
		self.location=location
		self.swim=swim
		self.cycle=cycle
		self.run=run
	def output(self):
		total=self.swim+self.cycle+self.run#calculate the totol time cost of swim, cycle and run
		return self.name, self.location, self.swim, self.cycle, self.run, total		
c=Triathlon('Chris·White','Edinburgh', 30, 10, 8)#input data as an example
print(c.output())
