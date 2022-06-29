def megaprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    else:
        d=0
        p=0
        while n:
            r=n%10
            n=n//10
            d+=1
            if r==2 or r==3 or r==5 or r==7:
                p+=1
        if p==d:
            return 1
        else:
            return 0
n=int(input())
if megaprime(n):
    print('Mega Prime')
else:
    print('Not Mega Prime')
