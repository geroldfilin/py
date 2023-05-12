print ("Hello world")
print ("hi!"*3) # повторли строку 3 раза.
str1 = "Mana"
str2 = "Rise"
str3 = "Permanent"
space =" "
print (str1 +space+str2+space+str3)
print (str1,str2,str3) #по умолчанию  ставит символ сепаратор. В данном случае пробел. 

x = 999
print ("My manna is ", x)
print ("My manna is " +str(x)) #преобразование числа в строку при конкотинации иначе ошибка.
x=str(x) # преобразовали х в строку.

num = 22/7
print(f"The value of num is {num}") #Базовый синтаксис f-строк Синтаксис форматированных строк 
pi = "{:.2f}".format(num)#обрезание вывода. в данном случае до 2х символов. 
print ("\n",pi) 

hostnames = ["R1", "R2", "R3", "S1", "S2"] #сосиски по спискам. В списке элементы пронумерованы с 0. Обращаться по номеру
print ("\n",type (hostnames))
print ("\n", hostnames)
print ("\n","len  hostname = ", len(hostnames)) #нумерация с нуля!!!
print ("\n", "first [0] element = ", hostnames[0]) #первый элемент
print ("\n", "last[-1] element = ",hostnames[-1]) #последний элемент
hostnames[0] ="RTR1"
print ("\n", hostnames)

ipAddress={"R1":"10.10.1.1", "R2":"10.10.2.2", "R3":"10.10.3.3"} #Cловарь - дикшинари. элемент каждый со своим именем.
print ("\n","Slovar = ", ipAddress, "type = ", type(ipAddress))
print ("\n", "R2 unit of slovar ipAddress  = ", ipAddress["R2"])
ipAddress["R3"]=["10.3.3.1", "10.3.3.2", "10.3.3.3"] #список внутри словаря на позиции элемента R3
print (ipAddress, "\n")

firstName = input ("What is your name? ") #просит ввести данные
lastName = input ("What is your lastname? ") 
location = input ( "Where are you from? ")
age = input ("How old are you? ")
print ("\n","Hello, " + firstName + " "+ lastName + "!" + " Your age " + age + " and you are from "+ location)




