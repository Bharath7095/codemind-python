a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if(j==i):
            print('0',end='')
        else:
            print('x',end='')
    print()