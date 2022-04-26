a=int(input())
s=0
while a!=0:
    r=a%10
    a=a//10
    s=s*10+r
print(s)