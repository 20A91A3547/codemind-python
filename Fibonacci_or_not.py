n=int(input())
if n==0 or n==1:
    print("True")
else:
    a=0
    b=1
    while (True):
        c=a+b
        a=b
        b=c
        if b==n:
            print("True")
            break
        elif b>n:
            print("False")
            break
