a=input()
a=a.lower()
b=input()
b=b.lower()
count=0
a=list(a.split(" "))
b=list(b.split(" "))
for i in a:
    if i in b:
        count+=1
print(count)