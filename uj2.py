#van 1 n elemu lista sorozat a sozrozatban van egy T tulajdonsag az algoritmusom megadja nekem a listaban van-e iylen t tulajdonsagu elem (yes or no)
'''
lista = [2, 5, 4, 8, 13, 10, 19]

talalat = False
index = 0
while index < len (lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print("Van a listaban harommal oszthato szam.")
else:
    print("Nincs harommal oszthato szam.")

'''

lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] == 'piros': talalat = True
index = index + 1

if talalat:
    print('Van a listában piros szín, az indexe: ', index-1)
else:
    print('Nincs a listában piros szín.')