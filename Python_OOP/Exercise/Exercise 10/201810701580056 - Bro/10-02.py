# exercise 10 02
'''
Bro
201810701580056
network 182
'''
class Animal:
    def __init__(self,type):
        self.type = type
    def sound(self):
        print('No Sound')
    def display_info(self):
        print('Type: '+ str(self.type))

class Dog(Animal):
    def __init__(self,type,weight):
        Animal.__init__(self,type)
        self.weight = weight
    def sound(self):
        print('Woof')
class Cat(Animal):
    def __init__(self,type,colour):
        Animal.__init__(self,type)
        self.colour = colour
    def sound(self):
        print('Meow')
my_dog = Dog('Labrador',22)
my_dog.sound()
my_dog.display_info()
my_cat = Cat('Siamese','white')
my_cat.sound()
my_cat.display_info()
