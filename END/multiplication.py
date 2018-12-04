#!/bin/env python
import gmpy2

def m(a):
      return pow(a,1,3571);


def Addition(xp,yp,xq,yq):
    an = (yq-yp)
    ad = gmpy2.invert(xq-xp,3571);

    alpha = m( an * ad)
    beta = m( yp - (alpha * xp));

    xr = m( (alpha **2) - (xp+xq));
    yr = m( (alpha*xr)+beta);

    return (xr,-yr);




def multiplication(xq,yq):
     A = int(input("Enter A : "))
     s1n =  m( (3 * xq* xq) + A)  
     s1d = gmpy2.invert(2 * yq,3571)

     s1 =  m(s1n * s1d)
     b1 = m(yq- (s1 * xq))

     xp = m( (s1 **2) - (2*xq ) )
     yp = m( ((-b1) * xq) - (b1))

     points = [];
     k = int(input("Enter scalar number: "))
     for i in range(1,k+1):
         (xr,yr) = Addition( xq,yq,xp,yp)
         points.append((xr,yr))
         xp,yp =xr,yr;

     print(points[k-5:])
     #return points[k-1]

gx= int(input("ENter a  point x : "))
gy= int(input("ENter a  point y : "))

multiplication(gx,gy);
