a = int(input("Enter a base:\t"))
N = int(input("Enter a MOD :\t"))
for i in range(1,10):
    print(i,"==>",a**i % N)

