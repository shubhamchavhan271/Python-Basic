#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100Judge and print total cost for user.
a=int(input("engter a number"))
cost=a*100
if a>10:
    discount=0.1*cost 
    total=cost-discount
    print("discount",discount)
    print("toatl",total)
else:
    print("no discount")
