a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
crr=[]
for i in arr:
    if i not in brr:
        if i not in crr:
            crr.append(i)
for i in brr:
    if i not in arr:
        if i not in crr:
            crr.append(i)
print(*crr)