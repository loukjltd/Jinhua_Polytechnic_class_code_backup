#exercise 12-02
'''
studentname:faker
studentid:201810701580048
class:net182
'''



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,student_id):
        Person.__init__(self,name,age)
        self.student_id = student_id
class Teacher(Person):
    def __init__(self,name,age,subject):
        Person.__init__(self,name,age)
        self.subject = subject
people = [Person('Alice',23),Student('Carl',19,'2017A121'),Teacher('Tom',32,'IT')]
sum_ages=0
for age in people:
    sum_ages+= age.age
print('Sum of ages: '+ str(sum_ages))

