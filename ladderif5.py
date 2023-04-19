''' Accept the kilometers covered and calculate the bill according to the following criteria:
First 10 Km              Rs11/km
Next 90Km              Rs 10/km
After that                 Rs9/km '''
n=int(input("enter a km"))
if n>11:
    print("Rs 11/km")
elif n>90:
    print("Rs 10/km")
else:
    print("Rs 9/km")
