''' Program to input number from user and check whether number is palindrome or not using while loop.
Example:   
 Input:  121
Output:  Number is palindrome'''

num=int(input("Enter any number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("Not a palindrome!")
