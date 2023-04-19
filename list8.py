#Python program to multiply all values in the list using traversal
a=[1,3,5,6]
def multiply(numbers):  
    total = 1
    for x in a:
        total *= x  
    return total  
print(multiply((a)))




