# Add each character, and it's ordinal, of user's text input, to two lists
s = input("Enter value: ")  # this line requires Python 3.x, use raw_input() instead of input() in Python 2.x

#while

r = int(input("ENter block size "))
NN = int(input("ENter a Numerical rep: 126 ==> ascii 25 for Naive "))
i = 0

while i <= len(s):
    t = s[i:i+r] 
    i = i+r
    print(t, end = "\t")
    asc_rep=  [ord(c) for c in t]
    print(asc_rep, end="\t")
    T= asc_rep[::-1]
    sum =0
    l = 0


    while l <= r-1:
        sum = sum + int(T[l]) * (NN ** l)
        l=l+1
    print(sum)


##

