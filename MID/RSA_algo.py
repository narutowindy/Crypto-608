#!/bin/env python

import math
import gmpy2
"""
    let p,q be a large prime numbers 
    n = pq
    phi(n) = (p-1) (q-1)

    choose small e , coprime phi(n)

    d =? 
        >> d*e mod(phi(n)) = 1
    publish e, n 
    keep d,p,q secret 

    d, n are private keys:
    
    Encrypt = m ^ e mod(n)

    Decrypt  = c ^ d mod(n)



"""

p = int(input("ENter a prime p:"))
q = int(input("ENter a prime q:"))
n = p *q
print( "n = p*q =",n)
Phi_n = (p-1) * (q-1) 
print("phi(n) = p-1 * q-1 = ", Phi_n )
e = 0

for i in range(2,Phi_n):
    if(math.gcd(i,Phi_n) == 1):
        e = i
        print("e coprime to phi_n is e:",e)
        break

d = gmpy2.invert(e,Phi_n)
print("Finding inverse module e^-1 mod(phi_n):d ==> ", d)




print("public key  n ,e " , n ,e )
print("private key  n ,d " , n ,d )


print("Use msg m = '6' to calculate cipher C C = pow(m,e,n) ,D = pow(C,d,n) ")





