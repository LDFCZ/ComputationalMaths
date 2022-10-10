import math

def f(x):
    return math.sin(x)

def findSBySimpsonMethod(a, b):
    return (f(a) + f(b) + 4 * f((b + a)/2)) * (b - a) / 6

def findSByTrapeziodMethod(a, b):
    return (f(a) + f(b)) / 2 * (b - a)

def findIntegrallBySimpsonMethod(a, b, n):
    h = abs(b - a) / n
    res = 0
    for i in range(0, math.trunc(n/2)):
        #res += findSBySimpsonMethod(a, a + 2 * h)
        res += (f(a) + f(a + 2 * h) + 4 * f(h + a)) * h / 3
        a += 2 * h
    return res

def findIntegrallByTrapezoidMethod(a, b, n):
    h = abs(b - a) / n
    res = 0
    for i in range(0, n):
        res += findSByTrapeziodMethod(a, a + h)
        a += h
    return res

def main():
    #try:
    #    a = float(input())
    #    b = float(input())
    #    n = int(input())
    #except:
    #    print("bad input")
    #    exit(0)

    ShT100 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 100)
    ShT200 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 200)

    ShT1000 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 1000)
    ShT2000 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 2000)
    
    
    ShS50 = findIntegrallBySimpsonMethod(0, math.pi / 2, 50)
    ShS100 = findIntegrallBySimpsonMethod(0, math.pi / 2, 100)
    
    ShS1000 = findIntegrallBySimpsonMethod(0, math.pi / 2, 1000)
    ShS2000 = findIntegrallBySimpsonMethod(0, math.pi / 2, 2000)

    ShS200 = findIntegrallBySimpsonMethod(0, math.pi / 2, 200)
    ShS400 = findIntegrallBySimpsonMethod(0, math.pi / 2, 400)

    print("Sh (T) 1/100 = ", ShT100)
    print("Sh (T) 1/200 = ", ShT200)

    print("Sh (T) 1/1000 = ", ShT1000)
    print("Sh (T) 1/2000 = ", ShT2000)

    print("Sh (S) 1/50 = ", ShS50)
    print("Sh (S) 1/100 = ", ShS100)

    print("Sh (S) 1/1000 = ", ShS1000)
    print("Sh (S) 1/2000 = ", ShS2000)

    print("Sh (S) 1/200 = ", ShS200)
    print("Sh (S) 1/400 = ", ShS400)

    print("k trapezoid1, h = 2pi/50, 2pi/100 =", math.log2(abs(ShT100 - 1) / abs(ShT200 - 1)))
    
    print("k trapezoid2, h = 2pi/1000, 2pi/2000 =", math.log2(abs(ShT1000 - 1) / abs(ShT2000 - 1)))

    print("k simpson1, h = 2pi/50, 2pi/100 =", math.log2(abs(ShS50 - 1) / abs(ShS100 - 1)))
    
    print("k simpson2, h = 2pi/1000, 2pi/2000 =", math.log2(abs(ShS1000 - 1) / abs(ShS2000 - 1)))
    
    print("k simpson3, h = 2pi/200, 2pi/400 =", math.log2(abs(ShS200 - 1) / abs(ShS400 - 1)))

if __name__ == '__main__':
   main()