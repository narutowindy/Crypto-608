#!/bin/env python
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)
 
def tonelli(n, p):
    if( legendre(n, p) != 1 ):
        return -1;
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r
 
# ECC curve :
#    E(x) = y ^2 = x ^ 3 + A* x + B    ::: mod( p )  
#   Generator Point ? Gx,Gy 
#   
#   generate all points :    using x = 0,1,2,3,....p-1 
#                               n = X^3 + A *x + B
#                               p = p
#                            y and -y with y = tonelli(n,y) 
#   
#   
#   
#   

######


if __name__ =="__main__":
    print("ECC E(X) = Y^2 = X ^ 3 + A * X + B :   mod(p)")
    print(" Need A and B     ")
    A = int(input("ENter A:"))
    B = int(input("ENter B:"))
    p = int(input("Enter PRime: "))
    roots = []
    for X in range(0,p):
        n = X ** 3+ A *X + B;
        r = tonelli(n,p)
        if(r != -1 ):
            roots.append( ( X , r )  )
            roots.append( ( X , p-r)  )
    #assert (r * r - n) % p == 0
    print("no of roots: ",len(roots)+1)
    print(roots[:25])


