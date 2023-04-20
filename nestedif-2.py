#Accept the age of 4 people and display the oldest one.
a=int(input("enter a 1st people age"))
b=int(input("enter a 2nd people age"))
c=int(input("enter a 3rd people age"))
d=int(input("enter a 4th people age"))
if a>b and a>c and a>d:
    print(a)
if b>a and b>c and b>d:
    print(b)
if c>a and c>b and c>d:
    print(c)
else:
    print(d)
