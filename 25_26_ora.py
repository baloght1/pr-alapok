lista = ["alma","banán","cseresznye"]
print(lista)

###########################################

lista = ["alma","banán","cseresznye"]
print(len(lista))

###########################################

lista1 = ["alma", "banán", "cseresznye"] #string
lista2 = [1, 5 ,7 , 9, 3] #int
lista3 = [True, False, False] # bool

###########################################

lista1 = ["abc", 34, True, 40, "férfi"]
print(lista1)

###########################################

lista = ["alma", "banán","cseresznye"]
print(lista[1])

###########################################

lista = ["alma", "banán","cseresznye"]
print(lista[-1])

###########################################

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[2:5])

print(lista[1:6])

###########################################

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[-4:])

###########################################

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
if "banán-1" in lista:
    print ("igen a banán benne van a listában")

###########################################

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista[1:3] = ["körte", "szilva"]
print (lista)

###########################################

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista[1:2] = ["körte", "szilva"]
print (lista)

###########################################

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista.insert(2,"körte")
print (lista)

###########################################

lista = ["alma", "banán", "cseresznye",]
lista.append("körte")
print (lista)