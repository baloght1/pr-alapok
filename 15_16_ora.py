'''
print("Hello")

print('Hello')

a = 'Hello'

print(a)

a = """Lorem ipsum dolor sit amet,

consectetur adipiscing elit,

sed do eiusmod tempor incididunt

ut labore et dolore magna aliqua."""

print(a)


a = "Hello, World!"

print(a[0])

print(a[4])
for x in "banana":

  print(x)

for x in "banana":

  print(x,end='')


a = "Hello, World!"

szamlalo = 1
for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end="")
     szamlalo = szamlalo + 1

txt = "The best things in life are free!"

print("free" in txt)


txt = "The best things in life are free!"

if "expensive" not in txt:

  print("No, 'expensive' is NOT present.")


b = "Hello, World!"

print(b[2:7])


b = "Hello, World!"

print(b[1:5])

c = "H"+b[1:5]
print (c)


b = "Hello, World!"

print(b[2:]) # llo, World!


a = "Hello, World!"

print(a.upper())
nagybetu = a.upper()
print (nagybetu)


a = "Hello, World!"

print(a.lower())


a = " Hello, World! "

print(a.strip())

a = "Jello, Jorld!"
print (a)

print(a.replace("J", "W"))
'''

a = "Hello, World!,2222,3333"

print(a.split(",")) # returns ['Hello', ' World!']
lista = a.split(",")
print(lista[1])

b = "44;341;223;333;6465"
print(b.split(";"))
lista1 = b.split(";")
print(lista1)[3]