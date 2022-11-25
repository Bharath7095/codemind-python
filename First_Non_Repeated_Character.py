n=int(input())
for j in range(n):
    a=int(input())
    s=input()
    c=0
    for i in s:
        if s.count(i)==1:
            print(i)
            c=1 
            break
    if c==0:
        print('-1')