#erxercise 14-05
'''
class:net182
student id :201810101580038
studentnameshrek
'''
try:
    x = int(input("Please enter a number: "))
except:
    print("That was not valid number.  Try again...")
    exit(0)

try:
    f=open('C:\yourname\my_number','r')
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