'''The Paschim Gujarat Vij Company Ltd. computes the electricity bill based on the following matrix:
Units Consumed	    Charges
0-100	                    0.50 per unit
101-200	                    Rs. 50 plus Rs. 1 per unit over 100 units
201-300	                    Rs. 150 plus 1.50 per unit over 200 units
> 300              	            Rs. 300 plus Rs.2 per unit over 300 units
1. Ask user to enter the Past meter reading and current meter     reading.
2. Find the units consumed.
3. Compute the bill according to given matrix.'''

past=int(input("enter a number"))
current=int(input("enter a unit in a current"))
consumed=current-past
if 0<=consumed and consumed<=100:
    bill=consumed*0.5
elif 100<consumed and consumed<=200:
    bill=consumed+50
elif 200<consumed and consumed<=300:
    bill=(consumed*1.5)+150
elif consumed>=300:
    bill=(consumed*2)+300
else:
    print("invalid input")
    exit()
print(bill)





   

   3. Compute the bill according to given matrix.