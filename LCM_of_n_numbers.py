n=int(input())
arr=list(map(int,input().split()))
m=max(arr)
while 1:
    c=0
    for i in arr:
        if m%i==0:
            c+=1
    if(c==n):
        break
    m+=1;
print(m)