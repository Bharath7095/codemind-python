a=input()
c=0
for i in range(0,len(a)):
    if a[i]>='0' and a[i]<='9':
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print('Contains',c,'digit')