'''
Student Name: Eden
ID: 201810701580060
Class: Network 182
'''
i = 3
done = False
print("Program to Change Password");
print("Your password has expired and you have " + str(i) + " chances left to change your password")
newPsw = int(input("Please enter your new password"))
pswEntered = int(input("Enter another password"))
while done and i > 0:
    if newPsw == pswEntered:
        done = True
    else:
        print("Error in entering password, please try again")
    i = i - 1
    print("You have " + str(i) + " chances left")
    continue
if i <= 0:
        print("Password not changed")
else:
        print("Password accepted!")