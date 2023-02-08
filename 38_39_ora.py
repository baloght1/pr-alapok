'''
szamoklista = list=[3,21,7,63,9,27]

min = list[0]
max = list[0]

for szam in szamoklista 
    if szam < min:
        min =szam
    if szam > min:
        max = szam


'''

#osszegzes tetele
szamoklista = list=[3,21,7,63,9,27]
osszeg = 0

for resz in szamoklista:
    osszeg = osszeg + resz
    
print(f"a lista teljes osszege")
print(osszeg)

#a lista elemeinek atlaga kiszamitasa
atlag = None
print(f"lista elemeinek atlaga: {atlag}")
atlag = osszeg /len 
print(osszeg)