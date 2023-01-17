#1.1fel
'''
szo = str(input("szo:"))

print(szo.upper())

'''

#1.2fel

'''
list1 = ["alma", "korte", "szilva", ]

list2 = [szo.upper() for szo in list1]

print(list1)
print(list2)

'''
#1.3

'''
list1 = ["alma", "korte", "szilva","asd"]

list2 = [szo.upper() for szo in list1 if len(szo) > 3]


print(list1)
print(list2)




'''

#fel1.4
'''
list1 = ["Alma", "Korte", "Szilva"]

list2 = [szo.swapcase() for szo in list1]

print(list1)
print(list2)

'''

#fel1.1

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
  

