def max_num(num1,num2,num3):
    if num1 > num2 :
        largest = num1
    else:
        largest = num2
    if num3 > largest:
        largest = num3


    return largest

a = 3
b = 5
c = 9
print('Maximun number is ' + str(max_num(a,b,c)))
