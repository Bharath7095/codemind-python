n=int(input())
a=list(map(int,input().split()))
o=0
e=0
for i in range(0,n):
    if i%2==0:
        o+=a[i]
    else:
        e+=a[i]
if o==e:
    print('YES')
else:
    print('NO')