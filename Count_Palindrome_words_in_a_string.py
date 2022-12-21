a=input()
a=a.lower()
a=a.split(" ")
c=0
for i in a:
    if i==i[::-1]:
        c+=1
print(c)