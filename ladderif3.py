''' Write a program to accept percentage and display the Category according to the  following criteria :
Percentage	Category
< 40        Failed
>=40 & <55	Pass
>=55 & <65	Good
>=65        Excellent '''

a=int(input("enter a no"))
if a<40:
    print("failed")
elif a>=40 and a<55:
    print("pass")
elif a>=55 and a<65:
    print("good")
elif a>=65:
    print("Excellent")
else:
    print()









