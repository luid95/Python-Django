class Dog():

    #Class object attribute
    species = "mammal"

    def __init__(self,breed, name):#Metodo que se ejecuta al instanciar
        #Definimos atribuitos
        self.breed = breed
        self.name = name


mydog = Dog("Dalmata", "Sammy")
print(type(mydog))
print(mydog.breed, mydog.name)
print(mydog.species)

class Circle():

    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle(3) #Definimos una instancia a la clase Circle()
myc.set_radius(999)
print("El radio del circulo es: ", myc.radius)
print("El area del circulo es: ", myc.area())
