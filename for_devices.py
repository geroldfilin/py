devices = ["R1","R2","R3","S1","S2"]

for item in devices: #служебная item   - обозначающая элемент.
	if  "R" in item:
		print("Router#",devices.index(item)+1," ",item, sep="")	
switches = [] #объявление пустого списка
print ("\n")
for item in devices:
	if "S" in item:
		switches.append(item) #метод append добавляет элемент в список
print (switches)