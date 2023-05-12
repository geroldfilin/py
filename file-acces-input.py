
file = open("passwd.txt","a") #для дозаписи "a" открывает функцией open

while True:
	user = input("Enter a user name: ")
	if user == 'exit':
		break
	file.write("\n" + user +"\n")

file.close() #обязательно закрыть
