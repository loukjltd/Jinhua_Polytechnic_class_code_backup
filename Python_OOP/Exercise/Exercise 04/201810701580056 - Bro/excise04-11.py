# exercise 04 11
'''
Bro
201810701580056
network 182
'''
print('M\tT\tM\tW\tF\tS\tSu')
a=-6
b=1
for i in range(0,5):
    a+=7
    b+=7
    for j in range(a,b):
        if j <= 31:
            print(j,end='\t')
        else:
            break
    print()

