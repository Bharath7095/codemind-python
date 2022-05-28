a=input()
v=0
c=0
d=0
s=0
for i in range(len(a)):
    if a[i] in 'AEIOUaeiou':
        v+=1
    elif a[i]>='0' and a[i]<='9':
        d+=1
    elif a[i]==' ':
        s+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',s)