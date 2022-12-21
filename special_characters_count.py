a=input()
a=a.lower()
c=0
for i in a:
    if i in "1234567890qwertyuiopasdfghjklzxcvbnm ":
        continue
    else:
        c+=1
print(c)