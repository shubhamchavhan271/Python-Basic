#program to interchange first and last elements in a list.
list=[1,2,3,4,5,6]
length=len(list)
temp=list[0]
list[0]=list[length-1]
list[length-1]=temp
print(list)


