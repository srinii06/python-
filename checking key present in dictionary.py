import operator
d={}
n=int(input())
for i in range(n):
    k=input()
    v=input()
    d[k]=v
k=input()
if k in d:
    print("key is present in the dictionary")
else:
    print("key is not present in the dictionary")