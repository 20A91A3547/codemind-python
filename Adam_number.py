n=int(input())
s=n*n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
s2=rev*rev
rev2=0
while s2>0:
    r1=s2%10
    rev2=rev2*10+r1
    s2=s2//10
if rev2==s:
    print(True)
else:
    print(False)
    

