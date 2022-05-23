n=int(input())
a=list(map(int,input().split()))
count=0
for i in a:
    c=0
    while(i):
        i=i//10
        c+=1
    if c%2==0:
        count+=1
print(count)