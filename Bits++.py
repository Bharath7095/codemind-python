n=int(input())
s=0
for j in range(n):
    b=input()
    a=list(b)
    if a[0]=='+':
        s+=1
    elif a[1]=='+':
        s+=1
    elif a[0]=='-':
        s-=1
    elif a[1]=='-':
        s-=1
print(s)