#Python program to count Even and Odd numbers in a List
a=[8, 19, 2, 43, 64, 91, 1]
count=0
for x in a:
    if x%2==0:
        count+=x
        print("even number in a:",count)  
        
    else:
        count+=1
        print("Odd numbers in a:",count)   




