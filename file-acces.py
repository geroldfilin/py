users = []
file = open("passwd.txt","r") #только чтение "r" открывает функцией open

for item in file:
	item=item.strip() #метод strip обрезает пустые строки.
	users.append(item)

file.close() #обязательно закрыть
print (users)