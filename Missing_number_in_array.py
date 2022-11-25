n=int(input())
for i in range(n):
    a=int(input())
    arr=list(map(int,input().split()))
    k=sum(arr)
    s=(a*(a+1))//2
    print(s-k)