# Exercise 04-01
'''
Student Name: Tami
ID: 201810701580035
Class: Network 182
'''

correctPsw = 1111 # set password
pswEntered = 0
print("Program to Check Password")
# check password
while pswEntered != correctPsw:
    pswEntered = int(input( "Please enter password: "))
print("Password accepted!")