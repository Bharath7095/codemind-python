a=input()
s=0
for i in range(len(a)):
    if a[i]>='0' and a[i]<='9':
        s+=int(a[i])
print(s)