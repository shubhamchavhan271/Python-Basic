#Write a program to find the largest number out of three numbers excepted from use
a=int(input("enter a 1st no"))
b=int(input("enter a 2nd no"))
c=int(input("enter a 3rd no"))
if a>b and a>c:
    print(a)
if b>a and b>c:
    print(b)
else:
    print(c)



