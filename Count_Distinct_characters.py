a=input()
a=a.lower()
brr=[]
count=0
for i in a:
    if i not in brr and i not in ' ':
        brr.append(i)
        count+=1
print(count)