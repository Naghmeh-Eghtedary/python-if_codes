import math
while True:
    print("1- sqrt")
    print("2- sin")
    print("3- cos")
    print("4- tan")
    print("5- cot")
    print("6- factorial")
    print("7- exit")
    print("choose a number of menu :",end=" ")
    c=int(input())
    if c==7:
        break   

    print("enter a number for operation:",end=" ")
    a=float(input())

    if c ==1 :
        print("sqrt ", a, " is: " , math.sqrt(a))
    elif c==2 :
        print("sinus ", a, " is: " , math.sin(a*math.pi/180))
    elif c==3 :
        print("cosinus ", a, " is: " , math.cos(a*math.pi/180))
    elif c==4 :
        print("tangent ", a, " is: " , math.tan(a*math.pi/180))
    elif c==5 :
        print("cotangent ", a, " is: " , 1/math.tan(a*math.pi/180))
    elif c==6 :
        print("factorial ", a, " is: " , math.factorial(int(a)))     
    else :
        print("rong choice")    