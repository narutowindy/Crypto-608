# p-1  factors q1,q2,q3.....qm
#   g = generator =    1 <g< p-1
#   g = 2
#   pow(g,(p-1/qi) , p) == 1
# try with next g+1

p = int(input("Enter a prime number p:\t"))
q = input("Enter list of factors:\t")
q= q.split(",")
q = list(map(int,q))
print(q,len(q))




for g in range(2,10):
    for i in range(0,len(q)):
        print( g,i,"==" ,pow( g, int((p-1)/q[i]),p )   )
    print("\n")
