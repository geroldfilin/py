file = open("passwd.txt", "r")
for item in file:
	item=item.strip()
	print(item)
file.close