''' 5. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
Note :
-- An equilateral triangle is a triangle in which all three sides are equal.
-- A scalene triangle is a triangle that has three unequal sides.
-- An isosceles triangle is a triangle with (at least) two equal sides.'''
a=int(input("enter a 1st side"))
b=int(input("enter a 2nd side"))
c=int(input("enter a 3rd side"))
if a==b and b==c and c==a:
    print("it is an eqilateral triangle")
if a!=b and b!=c and c!=a:
    print("it is an scalene triangle")
if a==b and b==c and a!=c or b==c and  c==a and a!=b:
    print("it is an isosceles triangle")


