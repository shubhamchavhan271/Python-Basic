''' Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

       Cost price (in Rs)                                       Tax

       > 100000                                                   15 %

       > 50000 and <= 100000                                      10%

       <= 50000                                                    5%

'''

a=int(input("enter a number"))
if a>10000:
    t=(a*15)/100
    print("tax is",t)
else:
    if a>50000 and a<=100000:
        t=(a*10)/100000
        print("tax is",t)
    else:
        if a<=50000:
            t=(a*5)/100
            print("tax is",t)
            


