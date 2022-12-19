def prime(n):
    if(n<2):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
def palin(n):
    rev=0
    a=n
    while(a):
        r=a%10
        a//=10
        rev=rev*10+r
    if(rev==n):
        return 1
    return 0
n=int(input())
while(1):
    n+=1
    if(palin(n) and prime(n)):
        break
print(n)