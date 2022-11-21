def displayNum(x):
    if x > 0:
        return " + "+str(x)
    elif x == 0:
        return ""
    else:
        return " - "+str(abs(x))
print("please enter your variable values assuming the form ax^2+bx+c")   
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

def gcdCalc(a,b):
    while b:
        temp = a
        a = b
        b = temp % b
    return abs(a)

gcdTemp=gcdCalc(a,b)
gcd=gcdCalc(gcdTemp,c)

if c==0:
    print(str(gcd)+"x("+str(a/gcd)+"x"+displayNum(b/gcd)+")")

else:
    sol1Numerator = -b + (b**2 - 4*a*c)**(1/2)
    sol2Numerator = -b - (b**2 - 4*a*c)**(1/2)
    denom = 2 * a
    if not (sol1Numerator.is_integer() and sol2Numerator.is_integer()) or not denom.is_integer():
        print("no clean factorization")
    else:
        sol1Gcd=gcdCalc(sol1Numerator,denom)
        sol2Gcd=gcdCalc(sol2Numerator,denom)
        sol1Numerator=-sol1Numerator/sol1Gcd
        sol1Denominator=denom/sol1Gcd
        sol2Numerator=-sol2Numerator/sol2Gcd
        sol2Denominator=denom/sol2Gcd
        print(str(gcd*a/abs(a))+"("+str(sol1Denominator)+"x"+displayNum(sol1Numerator)+")("+str(sol2Denominator)+"x"+displayNum(sol2Numerator)+")")