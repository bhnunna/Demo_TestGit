"""
******************
Write calculator program (in below 3 approaches) that does addition, substraction, multiplication and division
    Approach-1: As a script without any functions and classes 
    Approach-2: as functions but not classes
    Approach-3: As a class and functions inside it

Sample Input:
Enter first number: 32
Enter second number: 5

Sample output:
Addition of 32 and 5 is: 37
Substraction of 32 and 5 is: 27
multiplication of 32 and 5 is: 160
division of 32 and 5 is: 6.4


******************

"""
'''
definition to add 2 num
'''

def sum (a,b):
    #c=a+b
    print("Addition of {} and {} is: {}".format(a,b,a+b))
    
'''
definition to sub 2 num
'''

def sub (a,b):
    print("subtraction of {} and {} is: {}".format(a,b,a-b))

'''
definition to mul of 2 num
'''

def mul (a,b):
    print("multiplication of {} and {} is: {}".format(a,b,a*b))

'''
definition to division 2 num
'''

def div (a,b):
    if b!=0:
        print("division of {} and {} is: {}".format(a,b,a/b))
    else:
        print('divisor cant be {}'.format(b))

a=input("Enter first Number :")
a=int(a)
print(a)
b=input("Enter second num:")
b=int(b)
sum(a,b)
sub(a,b)
mul(a,b)
div(a,b)
