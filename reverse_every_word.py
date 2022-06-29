a=input()
b=list(a.split( ))
for i in b:
    c=''
    for j in range(len(i)-1,-1,-1):
        c+=i[j]
    print(c,end=' ')
    