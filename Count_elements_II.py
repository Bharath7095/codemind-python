a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
crr=[]
c=0
for i in arr:
    if i not in brr:
        if i not in crr:
            crr.append(i)
            c+=1
for i in brr:
    if i not in arr:
        if i not in crr:
            crr.append(i)
            c+=1
print(c)