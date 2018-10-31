#!/bin/env python

## ELgamal crypto
# users will have g , p
#P_a = A_pub = g ^a mod(P)   
#p_b = B_pub = g ^b mod(P)
# a and b are A,B 's respectively private key
"""
#protocol communication 
#Encryption by A:
____________________________________
A  -- m < p --- > B
  random selection k ;

 mask    M   =  pa ^ k mod(P)
Cipher   C = ( M * m ) mod(p)
Hint    H = (g^k) mod(P)

sends (C,H) ---- > B
______________________________________
# Decryption by B
    priv key b ,  q = p-1-b

  opener   R  =  H ^q  mod(P)
  Decrypted D = CR mod(P)
"""


p = int(input("  prime number p:"))
g = int(input("find generator:"))

a = int(input("A's private key a:"))
b = int(input("B's private key b:"))

msg = int(input("Enter a msg in numeric  rep msg:"))

k = int(input("Enter A's secret value K:"))

Pa = pow(g,a,p)
Pb = pow(g,b,p)
print("public keys of A = g^a , B is g^b ", Pa,Pb)

M  =  pow(Pb,k,p)
print("Mask = Pb ^k mod (p) ",M)


C =  pow(msg*M,1,p)
H = pow(g,k,p)

print("A-----(Cipher,Hint)---->B")
print("A------ (",C , H,")---->B")
q = p-1-b

print("q = p -1 - b", q)


R = pow(H,q,p)
D = pow(C*R,1,p)

print("Reduction R = H ^ q mod(p)" , R)
print("Decrypted msg C*R mod (P) ", D)












