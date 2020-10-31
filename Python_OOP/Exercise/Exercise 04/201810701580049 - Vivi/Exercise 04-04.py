#Exercise 04-04
'''
class:net182
name:vivi
id:201810701580049
'''

i = 3   # counter for number of logins
done = False

print("Program to Change Password");
print("Your password has expired and you have " + str(i) + " chances left to change your password")

# While password is not entered correctly AND more than 0 chances
while not done and i > 0:
    newPsw = input("Please enter your new password: ")
    pswEntered = input("Please enter your new password again: ")

    # change password correct
    if newPsw == pswEntered:
        done = True
    else:
        print("Error in entering password, please try again")
        i -= 1
        print("Your password has expired and you have " + str(i) + " chances left to change your password")


if i <=0:
    print("Password not changed") # password accepted
else:
    print("Password accepted!")
