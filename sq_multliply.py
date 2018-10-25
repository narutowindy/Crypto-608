def pow_modm(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

print("Square and multiply alogorithm \t\n")

b = int(input("Enter base value b:\t"))
p = int(input("Enter power value p:\t"))
m = int(input("Enter mod value m:\t"))

print(pow_modm(b,p,m))
