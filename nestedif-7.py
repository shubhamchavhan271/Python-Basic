'''  Write a Python program to convert month name to a number of days.
Expected Output:
List of months: January, February, March, April, May, June, July, August , September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days '''

a=input("name of Month")
if a=="February":
	print("28 or 29 days")
elif a in ("April", "June", "September", "November"):
	print("30 days")
elif a in ("January", "March", "May", "July", "August", "October", "December"):
	print("31 day")
else:
	print("Wrong month name")

