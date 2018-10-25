#!/bin/env python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print("Finding GCD of two numbers")

a = int(input("Enter a number a\t"))
b = int(input("Enter a number \t"))

print("GCD of two(" ,a,b,") is )",gcd(a,b))
