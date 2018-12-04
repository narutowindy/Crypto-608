#!/bin/env python
"""
    square root   r^2  = a    {  mod(p) }

    finding r: , p is a prime number


"""
#import math
#import gmpy2

def check_sq_exist(a,p):
    exp= (p-1)//2
    eval = pow(a,exp,p)
    return(eval)

a = int(input("Enter base number: "))
p = int(input("Enter a modulo: "))

exst = check_sq_exist(a,p)

if(exst == 1 and pow(p,1,4) == 3 ):
    exp = ( (p+1) // 4 )
    r = pow(a,exp,p) 
    print(r,-r+p)
elif(exst == 1 and pow(p,1,8) == 5 ):
    exp = (p-5)//8
    v = pow(2*a ,exp,p)
    i = pow(2*a*v*v, 1,p)
    r = pow(a*v*(i-1),1,p)
    print(r,-r+p)
elif(exst == 1 and pow(p,1,8) == 1 ):
    print("NOT implemented yet\n")
else:
    print("sqrt Doesn't exsit")


