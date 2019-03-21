#INHERITANCE

class Animal():
    def __init__(self):
        print("Animal created")

    def WhoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        print("Dog created")

    def bark(self):
        print("Woof")

myd = Dog()
myd.WhoAmI()
myd.eat()
myd.bark()
#SPECIAL METHODS
class Book():
    def __init__(self, tittle, author, pages):
        self.tittle = tittle
        self.author = author
        self.pages = pages

    def __str__(self):

        return "Tittle: {}, Author: {}, Pages: {}".format(self.tittle, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed!")

b = Book("Python", "Luis", 200)
print(b)
print(len(b))
del b

list = [1,2,3,4]
print(list)
