''' Accept the number of days from the user and calculate the charge for library according to following :
Till five days :     Rs 2/day.
Six to ten days  : Rs 3/day.
11 to 15 days  :   Rs 4/day
After 15 days    : Rs 5/day '''

n=int(input("enter a days"))
if n<=5:
    print("Rs 2/day")
elif n>6 and  n<=10:
    print("Rs 3/day")
elif n>10 and n<15:
    print("Rs 4/day")
else:
    print("Rs 5/day")
    
    

