n=int(input())
for k in range(0,n):
    s=0
    a=int(input())
    for i in range(0,100):
        r=a%10
        a=a//10
        s=s+r*(2**i)
        if a==0:
            break
    print(s)