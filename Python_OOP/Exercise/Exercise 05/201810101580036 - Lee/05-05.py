'''
class:net182
name:Lee
ID:201810101580036
'''
price = {'Banana' : 4,'Apple' : 2,'Orange' : 1.5,'pear' : 3}
quantity = {'Banana' : 1,'Apple' : 0,'Orange' : 3,'pear' : 2}

sum = 0

for i in price:
    sum += (price[i] * quantity[i])
print('Total cost: ',sum)