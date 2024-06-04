d={}
d1={}
n=int(input())
for i in range(n):
    k=input()
    v=input()
    d[k]=v
for i in range(n):
    k=input()
    v=input()
    d1[k]=v
d2=d.copy()
d2.update(d1)
print(d2)