#!/usr/bin/env python

"""

    CEO , President   =  p1 ,p2 , p3

     n vice_presidents  k'th Vp points are == ( p0 , pk )
     m mangers i'th manager        ==  (p0 , p(i+n))


    s = n + m   
    n = 3  
    m = 4 
    
    a,b,c   =  1,2,5

    for x = 0,1,2,3 .... 
    compute Y
    for x = -1,-2,-3 ....
    compute Y

    k =  0    1     2     3     4      5     6
    x =  0    1    -1     2    -2      3    -3
    Y =  

"""


n = int( input("Enter number  number of Vp's n: "))
m = int( input("Enter number  number of Vp's m: "))
print("Y = a X2 + bX +c ")

#a = int (input("ENter a: "))
#b = int (input("ENter b: "))
#c = int (input("ENter c: "))
a,b,c = 7,50,5
points=[]

for x in range(0,(n+m+4)//2):
    y = (x**3)+a * (x**2) + b * x + c
    points.append((x,y));


for x in range(-(n+m+4)//2,0):
    y = a * (x**2) + b * x + c
    points.append((x,y));


points.sort();
print(points)
