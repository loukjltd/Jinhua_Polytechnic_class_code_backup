# Exercise 08-03
'''
name: King
idnumber: 201810701580054
class: net182
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def message(self):
        print('Hello')
    def details(self):
        print('My name is ' +str(self.name)+ ' and I am {0} years old.'.format(self.age))
sam=Person('Sam',20)
sam.message()
sam.details()
james=Person('James',21)
james.message()
james.details()