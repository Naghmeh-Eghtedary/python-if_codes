import random
pre=0
while True:

    #play again
    print("Do you want to play (y/n) ?", end=" ")
    if(input() != "y" ):
        break

    #for repetitive guessing
    r=random.randint(1,100)
    while(r==pre):
        r=random.randint(1,100)
    pre=r

    #guess and compare
    t=0
    while True:
        print("guess a number :",end=" ")
        n=int(input())
        t+=1
        if n>r :
            print("Tray again! You gess too high")
        elif n<r :
            print("Tray again! You gess too small")
        else:
            print("Congratulation !! , you guess " , t , " times" )
            break

