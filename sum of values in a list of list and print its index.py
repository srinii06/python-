n=int(input())
a=[map(int,input().split()) for i in range(n)]
b=0
for i in a:
    s = sum(i)
    if s > b:
        b=s
        ind=a.index(i)
print(ind)


