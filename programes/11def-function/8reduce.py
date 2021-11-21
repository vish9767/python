from functools import reduce
def red(a,b):
    return a+b
nums=(1,2,3,4,5,6,7,89)
add=reduce(red,nums)
print(add)

