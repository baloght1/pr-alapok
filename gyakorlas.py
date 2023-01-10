nev = input("keresztnev:")
kor = int(input("hany eves vagy:"))

if kor < 1:
    print("A kora alapjan", nev, "csecsemo")
elif kor < 6:
    print("A kora alapjan", nev,"kisgyerek")
elif kor < 12:
    print("A kora alapjan", nev,"gyerek")
elif kor < 16:
    print("A kora alapjan", nev,"serdulo")
elif kor < 25:
    print("A kora alapjan", nev,"ifju")
elif kor < 65:
    print("felnott")
else:
    print("A kora alapjan", nev,"nyugdijas")