import random
 
posmotrel_Lekciyu = 0
def repeat(see_lekciya_Konstantina):
	global posmotrel_Lekciyu
	posmotrel_Lekciyu = posmotrel_Lekciyu + 1
	print ("Number of views: ", see_lekciya_Konstantina)
	
class Learn:
	def __init__(self,understand):
		self.understand = understand
	def by_doing (self):
		global ponimanie
		self.understand = self.understand + random.randint(1,40)
		print ("Current level of understand: ", self.understand)
		ponimanie = self.understand
		return ponimanie
		
ponimanie = 0
while True:
	repeat(posmotrel_Lekciyu)
	learning = Learn (ponimanie)
	learning.by_doing()
	if ponimanie >= 100:
		print("\n Well done! Go sleep, good boy!")
		break