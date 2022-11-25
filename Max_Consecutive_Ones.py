n=int(input())
arr=list(map(int,input().split()))
m=0
for i in range(n):
    if arr[i]==1:
        c=0
        for j in range(i,n):
            if arr[j]==0:
                break
            else:
                c+=1
        if c>m:
            m=c
print(m)