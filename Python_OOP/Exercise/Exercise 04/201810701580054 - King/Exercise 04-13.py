#Exercise 04-13
'''
name: King
idnumber: 201810701580054
class: net182
'''

yn='y'
i=[]
z=0
while yn !='n' and yn!='N':
    num=int(input('Enter a number:'))
    i.append(num)
    z+=1
    yn=input('Do you want to enter another number?:')
print('Sum = '+str(sum(i)))
print('Average = '+str(sum(i)/z))