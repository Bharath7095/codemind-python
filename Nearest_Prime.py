def prime(n):
    if(n<2):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
for i in range(n):
    num=int(input())
    a=num
    b=num
    while(1):
        if(prime(a)):
            break
        a+=1
    while(1):
        if(prime(b)):
            break
        b-=1
    if(a-num<num-b):
        print(a)
    elif(a-num>num-b):
        print(b)
    else:
        if(a<b):
            print(a)
        else:
            print(b)