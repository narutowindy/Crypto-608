#!/usr/bin/env python
import mod_inv
# bluems prime  P mod4 = Q mod4 = 3 ;
# N = P * Q    
# N is known to all Users
# p ,q are secrets
#

#       N = 77 , p = 7 , q = 11 
#       Alice PRiv ID = s1,s2 = (9,10)
#       a =19, b= 23 ,c 51
#       computed  Priv ID   ALice = P1,P2 = 58,67 
#       
#       si ^2 * Pi  modN  = 1 Mod N
#
#
#
#   

p = int(input("Enter a prime p: "))
q = int(input("Enter a prime q: "))

N = p*q ;

print("Composite Number : ",N);

print("Now TA chooses two numbers < N : ")
s1 = int(input("Enter s1: "))
s2 = int(input("Enter s2: "))

p1 = mod_inv.inverse_mod(s1**2,N);
p2 = mod_inv.inverse_mod(s2**2,N);


print("Alice selects A,B,C random Numbers < N ")

a = int(input("ENter a: "))
b = int(input("ENter b: "))
c = int(input("ENter c: "))

A = a **2 % N;
B = b **2 % N;
C = c **2 % N;

print("ALice sends the proof  of ID to  BOb A,B,C: ",A,B,C)

print("Bobs challenge: selects a random Matrix: of 3 * 2")

Mt = [[0,1],
     [1,0],
     [1,1]]

print(Mt);


M = a * (s1**Mt[0][0]) * (s2** Mt[0][1]) % N ;
P = b * (s1**Mt[1][0]) * (s2** Mt[1][1]) % N ;
Q = c * (s1**Mt[2][0]) * (s2** Mt[2][1]) % N ;



print("alice computes  M,P,Q and sends to BOb ; ",M,P,Q)


print("Bob verifies ")

assert (M**2) *(p1**Mt[0][0] )* (p2 **Mt[0][1]) %N == A , "A is succes"
assert (P**2) *(p1**Mt[1][0] )* (p2 **Mt[1][1]) %N == B , "B is success"
assert (Q**2) *(p1**Mt[2][0] )* (p2 **Mt[2][1]) %N == C , "C is success"





