print("enter your weight (kg) :")
w=int(input())
print("enter your height (cm) :")
h=int(input())
bmi=w/((h/100) ** 2)
print(bmi)
if bmi <18.5:
    print("under weight")
elif bmi >=18.5 and bmi <= 24.9:
    print("normal weight")    
elif bmi >=25 and bmi <= 29.9:
    print("over weight")
elif bmi >=30 and bmi <= 34.9:
    print("obesity")
elif bmi >=35 and bmi <= 39.9:
    print("extrem obesity")