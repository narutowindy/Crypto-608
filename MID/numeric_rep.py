#!/bin/env python
import string
l = list(string.ascii_lowercase)
for i in range(0,len(l)):
    print(i,"==>",l[i])


s = input("Enter string: ")

r = int((input("Enter block size: ")))

i = 0 
while i <= len(l):
    t = s[i:i+r]
    i=i+r
    print(t,end="\t")
    j = 0
    n_t=[0,1,2,3]
    while j < r:
        n_t[j] = l.index(t[j])
        j=j+1
    print(n_t)
        

