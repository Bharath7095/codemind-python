a=input()
b=list(a.split( ))
l=0
for i in b:
    if len(i)>l:
        l=len(i)
print(l)