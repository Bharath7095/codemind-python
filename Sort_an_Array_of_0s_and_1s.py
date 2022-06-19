n=int(input())
l=list(map(int,input().split()))
z=[]
o=[]
for i in l:
    if i==0:
       z.append(0)
    else:
        o.append(1)
for i in range(0,len(z)):
    print('0',end=' ')
for i in range(0,len(o)):
    print('1',end=' ')