'''Accept the percentage from the user and display the  grade according to the following criteria:
•	    Below 25 —- D
•	    25 to 45 —- C
•	    45 to 50 —- B
•	    50 to 60 –– B+
•	    60 to 80 — A
•	    Above 80 –- A+'''
n=int(input("enter a percentage"))
if n<25:
    print("D grade")
elif n>25 and n<45:
    print("C grade")
elif n>45 and n<50:
    print("B grade")
elif n>50 and n<60:
    print("B+ grade")
elif n>60 and n<80:
    print("A grade")
else:
    print("+A gread")
    

