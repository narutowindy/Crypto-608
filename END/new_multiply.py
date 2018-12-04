#!/bin/env python

 from mod_inv import *

    Xp = int(input("Enter Xp"))
    Yp = int(input("Enter Yp"))
# Xq = int(input("Enter Xq"))
# Yq = int(input("Enter Yq"))
# equation y^2 = x^3+Ax+B 
    mN=(((3*Xp*Xp)+7)
    mD=(2*Yp))
    m = mN * modinv(mD,3571)
    c = Yp-m*Xp
    Xr=(m**2)-2*Xp  
    print(Xr , m ,c)


