g = int(input("Enter a generator g: \t" ))
p = int(input("ENter a Prime number p: \t"))

a = int(input("ENter a Alice secret key a:\t"))

A_pub = pow(g,a,p)

b = int(input("ENter a Bob  secre key b:\t"))
B_pub = pow(g,b,p)

print("A_pub =",A_pub,"\nB_pub=",B_pub)
K1 = pow(A_pub,b,p)
K2= pow(B_pub,a,p)

print(K1,K2)

