def eldontes():

    lista = [2, 5, 4, 8, 9, 11, 10, 12]
    
talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
            talalat = True
    index = index + 1
    
    if talalat:
        print('Van a listában hárommal osztható szám.')
    else:
        print('Nincs a listában hárommal osztható szám.')


def kereses():


    lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index < len(lista) and not talalat:
	 if lista[index] % 3 == 0:
	    talalat = True
index = index + 1

if talalat:
	print('Van a listában hárommal osztható szám.')
else:
	print('Nincs a listában hárommal osztható szám.')


def kivalasztas ():


    lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
	if lista[index] == 'piros':
		talalat = True
	index = index + 1

if talalat:
	print('Van a listában piros szín, az indexe: ', index-1)
else:
	print('Nincs a listában piros szín.')



def szamlalas():
     
    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

darab = 0
for szam in lista:
    if szam %3  == 0:
        darab = darab + 1
        print("a listaban levo harommal osztahato szamok szama:", darab)




def osszegzes():
    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    min = lista[0]
    max = lista[0]
    for szam in lista:
	    if szam < min:
		    min = szam
	    if szam > max:
	        max = szam

    print('A legkisebb szám a listában: ', min)
    print('A legnagyobb szám a listában: ', max)  
