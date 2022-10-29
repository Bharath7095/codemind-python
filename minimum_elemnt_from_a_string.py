s=input()
m=list(s.split(" "))
l=len(m)
s=m[l-1]
n=min(s)
if n.lower() in s:
    print(n.lower())
else:
    print(n)