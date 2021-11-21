def fibonacci(n):

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
fibonacci(9)
