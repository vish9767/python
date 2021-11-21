def sub(a,*b):
    c=a
    for i in b:
        c=c-i
    d=a
    for j in b:
        d=d+j
    e=a
    for k in b:
        e=e*k
    return c,d,e

result1,result2,result3=sub(2,5,4,1)
print(result3)
