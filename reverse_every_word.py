a=input()
a=a.split(" ")
for i in range(len(a)):
    a[i]=(a[i])[::-1]
    print(a[i],end=" ")