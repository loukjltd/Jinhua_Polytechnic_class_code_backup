# Exercise 12-03
'''
name: King
idnumber: 201810701580054
class: net182
'''
class Worker:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

workers=[]
workers=[Worker('Tim',65000),Worker('Jane',52000),Worker('Sam',48000)]

sum_salary=0

for i in workers:
    sum_salary+=i.salary
print('Sum of the salaries: '+str(sum_salary))
