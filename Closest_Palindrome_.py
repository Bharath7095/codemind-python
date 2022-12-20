def palin(n):
    a=n
    rev=0
    while(a!=0):
        r=a%10
        a//=10
        rev=rev*10+r
    if(rev==n):
        return 1
    return 0
num=int(input())
a=num
b=num
while(1):
    a+=1
    if(palin(a)):
        break
while(1):
    b-=1
    if(palin(b)):
        break
if(a-num<num-b):
    print(a)
elif(a-num>num-b):
    print(b)
else:
    print(b,a)