def prime(n):
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if prime(i):
        count+=1
print(count)