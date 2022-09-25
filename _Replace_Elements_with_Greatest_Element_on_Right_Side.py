n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    m=0
    for j in range(i+1,n):
        if m<arr[j]:
            m=arr[j]
    arr[i]=m
arr[n-1]=-1
print(*arr)