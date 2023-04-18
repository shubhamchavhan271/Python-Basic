#program to find first and last digit of any number
a=input("enter a no")
first=int(a[0])
a=int(a)
last=a%10
print("first =",first)
print("last =",last)