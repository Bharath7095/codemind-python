a=list(map(int,input().split()))
b=list(map(int,input().split()))
al=0
bo=0
if a[0]>b[0]:
    al+=1
elif a[0]<b[0]:
    bo+=1
if a[1]>b[1]:
    al+=1
elif a[1]<b[1]:
    bo+=1
if a[2]>b[2]:
    al+=1
elif a[2]<b[2]:
    bo+=1
print(al,bo)