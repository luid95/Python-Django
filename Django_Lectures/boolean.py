#tuples and boolean

#tuples
t = (1,2,3)

print(t[0])

#las tuplas y las cadenas son inmutables
#t[0] = 'New'
#print(t)

#Pero las listas si puedes reasignar elementos sin problema alguno
list = ['a', True, 123]
print(list)
list[0] = 'NEW'
print(list)

#############################################

#Los conjunt,os son colecciones desordenadas con elementos unicos
#declaracion de un conjuntos "X"
x = set()

x.add(1)
x.add(2)
x.add(3)
x.add(2.2)
x.add(3)
x.add(4)
x.add(4)
x.add(4)

print(x)

conv = set([9,8,5,6,3,7,8,2,4,1,10,9])
print(conv)
