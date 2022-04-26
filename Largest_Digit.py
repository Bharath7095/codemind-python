a=int(input())
ans=0
while a!=0:
    r=a%10
    a=a//10
    if ans<r:
        ans=r
print(ans)