arr=input()
arr=arr.upper()
c=0
n=[]
for i in arr:
    n.append(i)
for i in range(0,len(n)):
    if n.count(n[i])==1 and n[i]!=' ':
        c+=1;
print(c)