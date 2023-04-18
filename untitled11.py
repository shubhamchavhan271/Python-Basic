#program to check whether a number is palindrome or not
a=int(input("enter a no"))
a=str(a)
b=a[::-1]
a,b=int(a),int(b)
if (a==b):
    print("palindrome")
else:
    print("not palindrome")