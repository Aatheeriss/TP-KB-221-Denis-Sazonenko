def dSearching(a, b, c):
    res = b**2-4*a*c
    return res

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = dSearching(a, b, c)
print(D)

