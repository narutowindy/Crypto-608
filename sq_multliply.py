#!/bin/env python

def pow_modm(x,e,m):
    base = x
    expo = e
    i = 1
    while i > 0:
        if i % 2 == 0:
            base = (base * base) % m
            expo = expo/2
        else:
            i = (base * i) % m
            expo = expo - 1
    return i

print("Square and multiply alogorithm \t\n")

b = int(input("Enter base value b:\t"))
p = int(input("Enter power value p:\t"))
m = int(input("Enter mod value m:\t"))

print(pow_modm(b,p,m))

