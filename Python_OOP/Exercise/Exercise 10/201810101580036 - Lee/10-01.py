'''
Student Name: Lee
ID: 201810101580036
Class: Network 182
'''
class Person:

    def __init__(self, name):
        self.name = name

    def greeting():
        print('Hello')

    def display_info(self):
        print('Name: '+str(self.name))


class Customer(Person):

    def __init__(self,name,age):
        Person.__init__(self,name)
        self.age=age

    def greeting(self):
        print('Dear customers, I am '+str(self.age) +' years old')
