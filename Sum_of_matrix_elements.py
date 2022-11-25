a=int(input())
b=int(input())
s=0
for i in range(0,a):
    arr=list(map(int,input().split()))
    s+=sum(arr)
print(s)