print(" enter first name: ")
nam=input()
print(" enter last name: ")
family=input()
print(" enter first score: ")
s1=float(input())
print(" enter secoond score: ")
s2=float(input())
print(" enter third score: ")
s3=float(input())
avg=(s1+s2+s3)/3
if avg>=17 :
    print( nam + family , "دانشجوی ممتاز")
elif avg<17 and avg>=12 :
    print( nam + family , "دانشجوی عادی")
elif avg<12 :
    print( nam + family , "دانشجوی مشروط")
else :
    print("خطای ورود اطلاعات")