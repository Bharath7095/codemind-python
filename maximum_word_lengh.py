a=input()
a=a.split(" ")
c=-9
for i in a:
    l=len(i)
    if(l>c):
        c=l
print(c)