import math
print("1- sqrt")
print("2- sin")
print("3- cos")
print("4- tan")
print("5- cot")
print("6- factorial")
print("choose a number of menu :")
c=int(input())
print("enter number:")
a=float(input())

if c ==1 :
    print(math.sqrt(a))
elif c==2 :
    print(math.sin(a*math.pi/180))
elif c==3 :
    print(math.cos(a*math.pi/180))
elif c==4 :
    print(math.tan(a*math.pi/180))
elif c==5 :
    print(1/math.tan(a*math.pi/180))
elif c==6 :
    print(math.factorial(int(a)))
else :
    print("rong choice")    