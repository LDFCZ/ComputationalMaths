import math

def f(x):
    return math.sin(x)

def findSBySimpsonMethod(a, b):
    return (f(a) + f(b) + 4 * f((b + a)/2)) * (b - a) / 6

def findSByTrapeziodMethod(a, b):
    return (f(a) + f(b)) / 2 * (b - a)

def findIntegrallBySimpsonMetod(a, b, n):
    h = abs(b - a) / n
    res = 0
    for i in range(0, n):
        res += findSBySimpsonMethod(a, a + h)
        a += h
    return res

def findIntegrallByTrapezoidMethod(a, b, n):
    h = abs(b - a) / n
    res = 0
    for i in range(0, n):
        res += findSByTrapeziodMethod(a, a + h)
        a += h
    return res

def main():
    try:
        a = float(input())
        b = float(input())
        n = int(input())
    except:
        print("bad input")
        exit(0)

    print("trapezoid = ", findIntegrallByTrapezoidMethod(a, b, n))
    print("Simpson = ", findIntegrallBySimpsonMetod(a, b, n))

    sh100 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 100)
    sh200 = findIntegrallBySimpsonMetod(0, math.pi / 2, 200)
    sh1000 = findIntegrallByTrapezoidMethod(0, math.pi / 2, 1000)
    sh2000 = findIntegrallBySimpsonMetod(0, math.pi / 2, 2000)

    print("Sh 1/100 = ", sh100)
    print("Sh 1/200 = ", sh200)
    print("Sh 1/1000 = ", sh1000)
    print("Sh 1/2000 = ", sh2000)
    print("k =", math.log2((sh100 - findSByTrapeziodMethod(0, math.pi / 2)) / (sh200 - findSByTrapeziodMethod(0, math.pi / 2))))
    print("k =", math.log2((sh1000 - findSByTrapeziodMethod(0, math.pi / 2)) / (sh2000 - findSByTrapeziodMethod(0, math.pi / 2))))

if __name__ == '__main__':
   main()