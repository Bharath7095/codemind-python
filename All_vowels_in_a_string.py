n=input()
b=[]
d=[]
a='aeiou'
count=0
for i in n:
    if i in 'aeiou' and i not in b:
        b.append(i)
c=''.join(b)
for i in a:
    if i not in c:
        count+=1
if count==0:
    print('True')
else:
    print('False')