# Exercise 03-03
'''
name : Clark
class: net182
I D  : 201810701580047
'''
print("Welcome to programming in Python")
print("This program shows IF and logical operators")

print("Enter a number between 0 and 100: ")
num = int(input("Enter a number between 0 and 100: "))

# Test the numbers using relationship and logical operators
if num < 0 or num > 100:
    print("Number " + str(num) + " is not between 0 and 100")

if num >= 0 and num < 50:
    print("Number " + num + "is between 0 and 50")

if num >= 50 and num <=100:
    print("Number " + str(num) + " is between 50 and 100")

else:
    print("Number " + str(num) + " Number num is in the middle")
