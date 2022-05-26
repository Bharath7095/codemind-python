n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
for i in range(0,n):
    if a[i]>=x and a[i]<=y:
        pass
    else:
        c.append(a[i])
if len(c)==0:
    print('-1')
else:
    print(max(c))