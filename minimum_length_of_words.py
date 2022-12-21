a=input()
a=a.split(" ")
c=99999
for i in a:
    l=len(i)
    if(l<c):
        c=l
print(c)