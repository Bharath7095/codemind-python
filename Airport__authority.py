n=int(input())
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
b=int(input())
s=0
for i in range(0,n):
    if arr[i]<=b:
        s+=1
    else:
        s+=2
print(s)