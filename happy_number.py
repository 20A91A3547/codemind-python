def chinna(n):
    s=0
    while(n):
        r=n%10
        s+=r*r
        n=n//10
    return s
n=int(input())
while(True):
    c=chinna(n)
    if c<10:
        if c==1 or c==7:
            print("True")
            break
        else:
            print("False")
            break
    else:
        n=c
