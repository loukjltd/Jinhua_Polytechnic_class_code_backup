'''student name:Faker
ID number:201810701580048
class:net182'''



print("Welcome to programming in Python")
print("This program shows IF and logical operators")

print("Enter a number between 0 and 100: ")
num = int(input("Enter a number between 0 and 100: "))
if num < 0 or num > 100:
    print("Number " + str(num) + " is not between 0 and 100")
if num >= 0 and num < 50:
    print("Number " + str(num) + " is  between 0 and 50")
if num >= 50 and num <= 100:
    print("Number " + str(num) + " is  between 50 and 100")
else:
    print("Number " + str(num) + " is in the middle")
