n=int(input())
for k in range(0,n):
    arr=[]
    brr=[]
    a=int(input())
    while a:
        r=a%2
        arr.append(r)
        a=a//2
    for i in range(len(arr)-1,-1,-1):
        brr.append(arr[i])
    for i in range(0,len(brr)):
        print(brr[i],end='')
    print()