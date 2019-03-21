#Enclosing function local
#Funciones anidadas

name = "This is a global name"

def greet():
    name = "Sammy"

    def hello():
        print("Hello "+name)

    hello()

greet()


################################
x = 50
def func():
    x = 1000
    return x

print("Before function call, x is:", x)
x = func()
print("After function call, x is: ", x)
