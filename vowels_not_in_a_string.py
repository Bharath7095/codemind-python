n=input()
b=[]
d=[]
a='aeiou'
count=0
for i in n:
    if i in 'aeiouAEIOU' and i not in b:
        b.append(i)
c=''.join(b)
for i in a:
    if i not in c:
        d.append(i)
        count+=1
if count==0:
    print('0')
else:
    e=''.join(d)
    print(*e)