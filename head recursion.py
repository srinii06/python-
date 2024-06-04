def fun(n):
    if n>0:
        fun(n-1)
        print(n)
        
    

num=int(input())
fun(num)
