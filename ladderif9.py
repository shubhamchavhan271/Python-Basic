#The given number is of one digited or two digited or three digited or more than three digited.
n=int(input("enter a no"))
if n<10:
    print("one digited no")
elif n<100:
    print("two digited no")
elif n<1000:
    print("three digited no")
else:
    print("more than three digited no")
