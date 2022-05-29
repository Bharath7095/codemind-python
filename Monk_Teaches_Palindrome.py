n=int(input())
for j in range(n):
    a=input()
    c=0
    if a==a[::-1]:
        c+=1
        print('YES',end=' ')
    else:
        print('NO')
    if c==1:
        if len(a)%2==0:
            print('EVEN')
        else:
            print('ODD')