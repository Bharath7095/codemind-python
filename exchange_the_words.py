a=input()
b=list(a.split( ))
c=[]
for i in range(len(b)-1,-1,-1):
    c.append(b[i])
print(*c)