#!/bin/env python
import sq_root 
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
        r = sq_root.tonelli(n,p)
        if(r != -1 ):
            roots.append( ( X , r )  )
            roots.append( ( X , p-r)  )
    #assert (r * r - n) % p == 0
    print("no of roots: ",len(roots)+1)
    print(roots[:10])




## POINT multiplication 
##
##      select a point = G ( Gx , Gy )
##      G + G  =
#           its a tangent:
#           alpha = slope = [  3 * Gx*Gx + A ] / 2 *Gy ;
#           
#           Xp + Xq + Xr  = alpha ** 2 ;
#           Xr = ( alpha **2 - (Xp+Xq) )
#           
#           Yr = alpha * Xr + ( Yp - alpha * Xp );
##
#####


def Addition(xp,yp,xq,yq):
    alpha = (yq-yp) * inv_mod(xq-xp , p);
    beta =  yp - alpha * xp;
    print("equation: y =",alpha,"x+",beta);
    xr = alpha **2 - (xp+xq);
    yr = alpha*xr+beta;
    return (xr,-yr);




def multiplication(xq,yq):
     s1 = ( [ 3 * yq* xq + A ] * inv_mod(2 * yq, p) );
     b1 = yq- s1 * xq;
     print("equation: y =",s1,"x+",b1);
     xp = s1 **2 - (2*xq);
     yp = -b1 * xq - b1;
     points = [];
     for i in range(1,k):
         (xr,yr) = Addition(xq,yq,xp,yp)
         points.append((xr,yr))
         xp,yp =xr,yr;

     print(point[k-2:])
     return point[k]






