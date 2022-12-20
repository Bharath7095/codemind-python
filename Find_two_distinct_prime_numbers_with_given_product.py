def prime(n):
    if(n<2):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=0
for i in range(2,n//2+1):
    for j in range(2,n//2+1):
        if(i*j==n and prime(i) and prime(j)):
            print(i,j)
            c=1
            break
    if(c==1):
        break
if(c==0):
    print("-1")