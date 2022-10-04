a=input()
a=a.lower()
b=input()
b=b.lower()
arr=list(a.split(' '))
brr=list(b.split(' '))
for i in brr:
    if i in arr:
        print(i,end=" ")