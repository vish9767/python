def fibonacci(n):
    if(n<=0):
        print("user given input is wrong")
    else:
       a=0
       b=1
       if 1==n:
           print(a)
       else:
           print(a)
           print(b)
       for i in range(3,n):
           c=a+b
           a=b
           b=c
           print(a+b)
fibonacci(10)
