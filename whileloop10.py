#Program to input a number from user and  find first and last digit of a number using while loop.

n=int(input("enter a number"))
l=n%10
a=n 
while(a>0):
    r=a%10
    a=a//10
print("first",r)
print("last",l)
    



