#program to find sum of natural numbers from 1 to n
n = int(input("  Enter the  Value : "))
sum = 0
for x in range(1, n+1):
        sum= sum + x
print(sum)