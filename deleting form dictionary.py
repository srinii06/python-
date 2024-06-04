import operator
d={}
n=int(input())
for i in range(n):
    k=int(input())
    v=int(input())
    d[k]=v
key=int(input())
if key in d:
    del d[key]
print(d)