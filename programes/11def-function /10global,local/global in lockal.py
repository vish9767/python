a=10
print(a)
def something():
    global a
    a=15
    print("this is the gloal vaiable",a)
something()
print("this is global variable",a)


