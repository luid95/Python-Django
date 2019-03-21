#lists
mylist = [1,2,3,4,5]
mylist2 = ["asdfg", 1, 2, 3, True, 22.3, 'asdfg', [7,8,9]]

print(mylist)
print(mylist2)

print(len(mylist2))

mylist3 = ['a', 'b', 'c', 'd', 'd', 'e']

print(mylist3[0])
print(mylist3[-1])
print(mylist3[:1])
print(mylist3[1:])

#reassignment
print("before assignment:")
print(mylist3)

mylist3[0] = "New Item"

print("After assignment:")
print(mylist3)

mylist3.append("f")
print(mylist3)

mylist4 = ['a', 'b', 'c', 'd', 'e']
mylist5 = ['x', 'y', 'z']

mylist4.extend(mylist5)
print(mylist4)

item = mylist4.pop()
print(item)

mylist4.reverse()
print(mylist4)

#Ordenar listas
list = [6,3,5,2,9,8,1,4,7]
list.sort()
print(list)

list2 = [1,2,['x', 'y', 'z']]
print(list2)
print(list2[2]) #imprime x, y, z
print(list2[2][1]) #imprime y

##########333
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
#lista de comprension
print(first_col) #imprime 1, 4, 7
