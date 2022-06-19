n=int(input())
for i in range(0,n):
    a=input()
    ans=bin(int(a,8))
    print(ans[2:])