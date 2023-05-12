nativeVlan = 1
dataVlan = 100

nativeVlan = int(input ("Please insert native vlan: ")) #input возвращает строку - преобразуем в число
dataVlan = int(input("Please insert data vlan: "))
if nativeVlan == dataVlan:
	print ("The native and data vlan are the same.")
else: 
	print ("the native and the data clan are different." )
