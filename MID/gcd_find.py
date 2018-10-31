#!/bin/env python
import math
p = int(input("prime number p not p-1: "))

for i in range(2,20):
    print(i,math.gcd(i,p-1))

