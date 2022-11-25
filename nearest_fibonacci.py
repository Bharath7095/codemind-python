n=int(input())
a=0
b=1
while 1:
    c=a+b
    a=b
    b=c
    if(c>n):
        break
if(abs(n-a)<abs(n-b)):
    print(a)
elif(abs(n-a)>abs(n-b)):
    print(b)
else:
    print(a,b)