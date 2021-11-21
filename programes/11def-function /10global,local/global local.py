a=10
def something():
    x=globals()['a']
    print(id(x))
    print("this is global variable",x)
    globals()['a']=15
    print("globale value is now canged")
    print(id(x))
    a=4
    print(a,id(a))
something()
print(a)

