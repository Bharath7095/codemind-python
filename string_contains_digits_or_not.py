n=int(input())
for i in range(n):
    a=input()
    c=0
    for j in range(len(a)):
        if a[j]>='0' and a[j]<='9':
            c+=1
    if c==0:
        print('No')
    else:
        print('Yes')