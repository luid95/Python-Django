#if

if 1<2:
    print("First Block!")
    if 20<3:
        print("Second Block!")
#For loops

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)


d = {"Sam": 1, "Frank": 2, "Dan": 3}

for item in d:
    print(item)
    print(d[item])
#############
myparis = [(1,2), (3,4),(5,6)]

for item in myparis:
    print(item)
########################3
i=1

while i<5:
    print("i is: {}".format(i))
    i +=1

    ########################33
x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)

print(out)
