def star():
    name=('vishal','akshay','rohan','somnath')
    for e in name:
     print("\n")
     print(e)
     a=int(input("enter the value for star how star you want"))
     i=0
     while(i<a):
         print("*",end="")
         i=i+1

star()
