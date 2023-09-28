#calculating D
def dSearching(a, b, c):
    res = b**2 - 4*a*c
    return res

#variables input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

#D output
D = dSearching(a, b, c)
print("\nD =", D)

#topic_02
#D conditions check, roots calculating and output 
if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print("\nEquation has 2 roots: ")
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("\nEquation has 1 root: ")
    print("x =", x)
else:
    print("\nEquation has no roots.")
