gcd=1
print("enter first number:",end=" ")
n1=int(input())
print("enter second number:",end=" ")
n2=int(input())

#greater number in n1 and smaler number in n2
if(n2>n1):
    a=n1
    n1=n2
    n2=a

for i in range(1,n2 +1 ):
    if n2 % i ==0 and n1 % i ==0:
        gcd=i


print("GCD = " , gcd)
print("LCM = ",n1*n2/gcd)


