class Circle:
	def __init__(self, radius):
		self.radius = radius
	def circumferecence(self):
		pi = 3.14
		circumferecenceValue = 2*pi*self.radius
		return circumferecenceValue
	def printCircumference (self):
		myCircumference = self.circumferecence()
		print(" Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

circle1 = Circle(2)		
circle1.printCircumference()

circle2 = Circle(5)
circle2.printCircumference()

circle3 = Circle(7)
circle3.printCircumference()