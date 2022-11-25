n=int(input())
arr=list(map(int,input().split()))
a=int(input())
brr=[]
m=max(arr)
for i in arr:
    if (i+a)>=m:
        brr.append('True')
    else:
        brr.append('False')
print(*brr)