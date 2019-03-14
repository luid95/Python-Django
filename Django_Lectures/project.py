#Problem 1

s = 'django'

#Use de indexing to print out the following
#'d'
a = s[0]
print(a)
#'o'
b = s[5]
print(b)
#'djan'
c = s[:4]
print(c)
#'jan'
d = s[1:4]
print(d)
#'go'
e = s[4:]
print(e)
#Bonus
#use indexing  to reverse the string

f = s[::-1]
print(f)

##############################################33
#Problem 2
#Given this nested list

l = [3, 7, [1, 4, 'hello']]
print(l)
#Reassing 'hello' to be 'goodbye'
l[2][2] = 'goodbye'
print(l)

##################################3
#using keys and indexing
#Problem 3, grab th 'hello' from the following dictionaries:

d1 = {'simple_key' : 'hello'}
x = d1['simple_key']
print(x)
d2 = {'k1' : {'k2' : 'hello'}}
y = d2['k1']['k2']
print(y)
#este es el mas dificil
#primero es seleccionar la llave 'k1'
# como sigue un corchete despues, es la declarcion de una lista entonces se elige la posicion [0]
#seleccionamos la llave que se encuentra en esa posicion
#nos encontramos con otra lista; seleccionamos la posicion [1]
#y como hello esta dentro de otra lista ; seleccionamos la posicion
d3 = {'k1' : [{'nest_key' : ['this_is_deep', ['hello']]}]}
z = d3['k1'][0]['nest_key'][1][0]
print(z)
#######################################################################
#Problem 4
#Use a set to find the unique of the list below
my_list = [1,1,1,1,1,2,2,2,2,2,3,3,3,3]
a = set(my_list)
print(a)

#########################################################################3
#Problema 5
#You are fiven two variables:

age = 4
name = "Sammy"

#Use print formatting to print the following string
#"Hello my dog's  name is Sammy and he is 4 years old"

print("Hello my dog's name is {a} and he is {b} yeras old." .format(a=name, b=age))
