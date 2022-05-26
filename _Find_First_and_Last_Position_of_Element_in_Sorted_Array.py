n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=-1
d=-1
for i in range(n):
    if a[i]==b:
        c=i
        break
for i in range(n-1,-1,-1):
    if a[i]==b:
        d=i
        break
print(c,d)