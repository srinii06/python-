def fun(n):
    if n>0:
        
        print(n)
         
        fun(n-1)
    

num=int(input())
fun(num)

