n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(n):
    if a.count(a[i])>1:
        print(a[i])
        break