#!/bin/env python

import math
import gmpy2

"""
    A -----  msg = a --------> B
    
    A: semi-prime   m = p * q    Phi_A = p-1 * q-1
    B:              n = r * s    Phi_B  = r-1 * q-1

    e =  coprime Phi_A , d * e mod(Phi_A) = 1    d = priv
    h =  coprime Phi_B , g * h mod(Phi_B) = 1   g = priv



    Sender:
    ------------------------------------
    X = a ^d mod(m)    // m =  pq , d =private key A
    Y = X ^h mod(n)    // n = rs     h = public key B

                    A--------Y---------->B

    Decrypt & verification :
    ---------------------------------------------
    z = y ^ g mod(n)  // n = rs , g =priv key of B
    u = z ^ e mod(m)  // m = pq , e = public key of A


    Veification 
    a == u
"""

p = int(input("Enter p: "))
q = int(input("Enter q: "))
r = int(input("Enter r: "))
s = int(input("Enter s: "))

m = p*q
n = r*s

Phi_A = (p-1) * (q-1)
Phi_B = (r-1) * (s-1)
print("m , n == ", m,n)
print("Phi_A , Phi_B",Phi_A,Phi_B)
for i in range(2,20):
     print(i,math.gcd(i,Phi_A)) 
    
for j in range(2,20):
    print(j,math.gcd(j,Phi_B))

e = int(input("select e such that gcd(e,Phi_A) = 1 :  "))
h = int(input("select e such that gcd(h,Phi_B) = 1:  "))
print("e, h", e, h)

d = gmpy2.invert(e,Phi_A)
g = gmpy2.invert(h,Phi_B)

print("Private keys ( d, g) ",d,g)

a = int(input("msg in numerical rep "))

X = pow(a,d,m)
Y = pow(X,h,n)

print("Sender sends not X, only Y to B", X,Y)

print("Decrypting")

Z = pow(Y,g,n) 
U = pow(Z,e,m)


print("Z , U" , Z,U)


print("Verification of sign ")

print("a == U", a, U)

