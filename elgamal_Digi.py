#!/bin/env python
import math
import gmpy2

"""
Sender :
-----------------------
Key Gen
    prime       = P
    Generator   = g

key r :
        1 < r  < p-1

    K  =  g ^ r mod(p)
(K , g ,p ) are publicly avialable

Signing:
----------------------------
    Sender selects another int R;   1< R < p-1
        gcd(R,p-1) = 1

        X = g^ R mod(p)

        sender finds Y such that  M =rX+RY mod(p-1)

    A----( X,Y ,M) is signature of M: --------> B
_________________________________________
Verification:
    B gets (M,X,Y) , avaialble K ,g, p

    A = (K ^X )  * (X ^Y) mod(p)

    IFF A = g^M mod(p)
then verified :
"""



p = int(input("Enter prime p "))
g  = int((input("Enter a generator g ")))

r = int(input("ENter a rand.secrt.key for Gen sign r "))

K = pow(g,r,p)

print("A----->publishes ( K,p,g )---",K ,p,g)

M = int(input("Enter a msg in numeric rep"))

print("\nSelect a random R such that gcd(R,p-1) = 1\n")
"""
for i in range(2,p):
    if(math.gcd(i,p-1)==1):
        R = i
      break
      """
R = int(input("Enter Random R:"))

X = pow(g,R,p)
print("X=",X)

print("Find Y, in M = rX+RY")
print("r=",r)
print("R=",R)

Rhs= (M - r * X)
Rhs2 = Rhs * (gmpy2.invert(R,p-1))
Y = pow(Rhs2,1,p-1)
print("Value of Y is :" ,Y)
#Y = int(input("VAlue of Y: "))
print("--"*10)
print("Decryption")
print("--"*10)
print("B has (M,X,Y)",M,X,Y)
print("B has (K,g,p)",K,g,p)


v1 = K**X
v2 = X**Y
v = v1 * v2

A1 = pow(v,1,p)
A2 = pow(g,M,p)

print(A1,"==?",A2)































