def prime(n):
    if(n<2):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
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
    print(a-num)
else:
    print(num-b)