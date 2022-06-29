a=input()
c=0
for i in a:
    if i in 'a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        continue
    else:
        c+=1
print(c)