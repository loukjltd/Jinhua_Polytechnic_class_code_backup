#Exercise 03-03
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

print("Welcome to programming in Python")
print("This program shows IF and logical operators")

print("Enter a number between 0 and 100: ")
num = int(input("Enter a number between 0 and 100: "))

if num < 0 or num > 100:
    print("Number " + str(num) + " is not between 0 and 100")

if num >= 0 and num < 50:
    print("Number " + str(num) + " is between 0 and 50")
elif num >= 50 and num <= 100:
    print("Number " + str(num) + " is between 50 and 100")
else :
    print("Number num is in the middle")
