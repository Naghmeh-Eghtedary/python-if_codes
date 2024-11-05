print("enter first side of triangle:")
a=float(input())
print("enter second side of triangle:")
b=float(input())
print("enter third side of triangle:")
c=float(input())
if (a>b+c) and (b>a+c) and (c>a+b) :
    print("yes")
else :
    print("no")

