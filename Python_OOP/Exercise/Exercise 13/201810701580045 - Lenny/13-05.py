#
'''
class:net182
name:lenny
ID:201810701580045
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 20
for i in range(0,n):
    print(fibonacci(i),end=',')



