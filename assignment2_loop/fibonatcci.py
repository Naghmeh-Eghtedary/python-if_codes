num1=0
num2=1
print("enter numbers of series: ",end=" ")
n=int(input())
print(num1,end=" ")
while(n>1):
    print(num2,end=" ")
    s=num1+num2
    num1=num2
    num2=s
    n-=1
