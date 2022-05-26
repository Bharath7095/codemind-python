n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    s=1
    for j in range(n):
       if i!=j:
           s*=a[j]
    b.append(s)
print(*b)