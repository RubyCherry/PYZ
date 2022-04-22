import sys

def decor(func):
   def wrap(*ars): 
    print("start")
    z= func(*args)
    print("end")
    return z
    return(wrap)

@decor
def add(a,b):
    sum= int(a) + int(b)
    print (sys.argv)
    return print(sum)

@decor
def add2(a, b, c):
    sum= int(a) + int(b) + int(c)
    print (sys.argv)
    return print(sum)

