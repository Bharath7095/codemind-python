n=int(input())
a=list(map(int,input().split()))
sa=0
sb=0
for i in range(0,n//2):
    sa+=a[i]
for i in range(n//2,n):
    sb+=a[i]
b=abs(sa-sb)
if b%4==0:
    print('X')
else:
    print('Y')