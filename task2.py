def findDiff(x):
    return abs(x - 5**0.5)

def f(x):
    return x ** 2 - 5

def oneTangentMethod():
    x = 3 - f(3)/6
    return x - f(x)/6

def secantMethod():
    x = 3 - f(3)/6
    return x  - f(x) * (x - 3) / (f(x) - f(3))

def newtonMethod():
    x = 3 - f(3)/6
    return x - f(x)/ (x*2)

def main():
    print("Метод одной касательной {} ошибка {}".format(oneTangentMethod(), findDiff(oneTangentMethod())))
    print("Метод секущих {} ошибка {}".format(secantMethod(), findDiff(secantMethod())))
    print("Метод Ньютона {} ошибка {}".format(newtonMethod(), findDiff(newtonMethod())))

if __name__ == "__main__":
    main()