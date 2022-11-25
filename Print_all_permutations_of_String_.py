from itertools import permutations 
perm = permutations(list(input()))
for i in list(perm): 
    a=''.join(i)
    print(a) 