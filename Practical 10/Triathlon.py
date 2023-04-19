class Triathlon (object):#import a class
	def __init__(self, name, location, swim, cycle, run):#import a function
		self.name=name
		self.location=location
		self.swim=swim
		self.cycle=cycle
		self.run=run
		total=self.swim+self.cycle+self.run
		print(self.name, self.location, self.swim, self.cycle, self.run, total)
		
c=Triathlon ('Chris·White','Edinburgh', 30, 10, 8)
