''' Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:
Marked Price       Discount
>10000              20%
>7000 and <=10000   15%
<=7000              10%

'''
m=int(input("enter a marked price"))
if m>10000:
    amount=(m*20)/100
    netamount=m-amount
    print(netamount)
elif m>7000 and m<=10000:
    amount=(m*15)/100
    netamount=m-amount
    print(netamount)

elif m<=7000:
    amount=(m*10)/100
    netamount=m-amount
    print(netamount)
