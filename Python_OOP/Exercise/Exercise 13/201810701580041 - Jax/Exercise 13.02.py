# Exercise 013-02
'''
Student Name: Jax
ID: 201810701580041
Class: Network 182
'''
def get_sum(my_list):

    if len(my_list) == 0:
        return 1 # stop
    else:
        new_list = my_list[1:len(my_list)]
        return my_list[0] * get_sum(new_list)


numbers = [1.2, 2.0, 3.5, 5.3]
sum_list = get_sum(numbers)
print(sum_list)