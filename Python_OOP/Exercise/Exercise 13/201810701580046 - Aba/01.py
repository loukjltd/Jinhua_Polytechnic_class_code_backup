#exercise 13-01
'''
studentname:Aba
studentid:201810701580046
class:net182
'''



def countdown(n):

    if n > 10:
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
