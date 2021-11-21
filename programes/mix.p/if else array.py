print("vishal how are you \"i think youare happy\"")
print(r"vishal are  you happy yes\no ")
print("ok friends lets start programing")
b=1
a=int(input("if you are ready  you can type 1 if no type 0"))
if(b==a):
    print("lets take the value for array")
    from array import *
    array=array('i',[])
    c=int(input("enter the length for array"))
    d=0
    while(d<c):
        e=int(input("enter the value for array"))
        d=d+1
        array.append(e)
    print(array)
else:
    print("we will take the program next time ")
    print("T/A/T/A")
