# exercise14-05
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
try:
    x = int(input("Please enter a number: "))
except:
    print("That was not valid number.  Try again...")
    exit(0)

try:
    f=open('my_numbers.txt','r')
except:
    print("Cannot find file")
    exit(0)


line=f.readlines()
line_list=line[0].split(' ')
y=int(line_list[1])


try:
    z = x/y
except:
    print("You cannot divide by zero")
    exit(0)
