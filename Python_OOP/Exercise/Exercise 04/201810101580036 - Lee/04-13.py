#exercise 04-13
'''
name:Lee
class:net182
'''

flag = True
t = 0
c = 0
while flag is True:
    n = str(input('Enter a number: '))
    t += int(n)
    c += 1
    w = str(input('Do you want to enter another number?: '))
    if w == 'y':
        flag = True
    elif w == 'n':
        flag = False
print('Sum:' + str(t))
print('Average: ' + str(t / c))