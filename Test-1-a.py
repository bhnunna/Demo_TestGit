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
without fun & class is
"""
a=input("Enter first Number :")
a=int(a)
b=input("Enter second num:")
b=int(b)
print("sum of {} and {} is :{}".format(a,b,a+b))
print("Sub of {} and {} is :{}".format(a,b,a-b))
print("Mul of {} and {} is :{}".format(a,b,a*b))
if b!=0:
    print("division of {} and {} is: {}".format(a,b,a/b))
else:
    print('divisor cant be {}'.format(b))
