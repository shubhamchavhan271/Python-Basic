#Accept three numbers from the user and display the second largest number.

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b:
    if b>c:
        print(b)
    else:
        print(c)
else:
    if a>c:
        print(a)
    else:
        print(b)



