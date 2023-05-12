class Location:
	def __init__(self,name,country):
		self.name = name
		self.country = country
	def myLocation(self):
		print("Hello, my name is " + self.name + " and i live in " + self.country + ".")

loc1 = Location("Sabito","Mexico")
loc1.myLocation()

loc2 = Location("Gerold","Rivia")
loc2.myLocation()

loc3 = Location("Yang", "Huang")
loc3.myLocation()