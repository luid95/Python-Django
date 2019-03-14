#comentarios
print((2+10)*(2+10))

#asignaciones
a = 100
b = 0.1

c= a*b

print(c)

#Strings

#Basics
my_string = "abcdefg"
print(my_string)
print(my_string[0])
print(my_string[4:])
print(my_string[:3])
print(my_string[2:5])
print(my_string[::2])

x = my_string.upper()
print(x)

x = my_string.lower()
print(x)

y = my_string.capitalize()
print(y)

cadena = "Hello World"
a = cadena.split('e')
print(a)

x = "Iteam One: {}, Iteam two : {}".format("dog", "cat")
print(x)

x = "Iteam One: {x}, Iteam two : {y}".format(x = "dog1", y = "cat1")
print(x)
