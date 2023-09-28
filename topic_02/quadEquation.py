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
#roots calculating function
def calculatingRoots(b, D, a):
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    if x1 == x2:
        return x1
    else: 
        return x1, x2
    
#D conditions check and roots output 
if D > 0:
    print("\nEquation has 2 roots: ")
    print("x =", calculatingRoots(b, D, a))   
elif D == 0:
    x = -b / (2*a)
    print("\nEquation has 1 root: ")
    print("x =", calculatingRoots(b, D, a))
else:
    print("\nEquation has no roots.")
