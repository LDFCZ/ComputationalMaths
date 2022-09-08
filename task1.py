
# f(x) = x^3 + ax^2 + bx + c = ????????????
def findFunctionValue(a, b, c, x):
    return x ** 3 + a * x ** 2 + b * x + c 

# Finding root in line segment
def findRoot(a, b, c, leftValue, rightValue, epsilon):
    value = (leftValue + rightValue) / 2

    while(abs(findFunctionValue(a, b, c, value)) > epsilon):

        if(findFunctionValue(a, b, c, leftValue) * findFunctionValue(a, b, c, value) < 0):
            rightValue = value
        elif(findFunctionValue(a, b, c, rightValue) * findFunctionValue(a, b, c, value) < 0):
            leftValue = value
        value = (leftValue + rightValue) / 2
    return value

def findRootByStepsPositive(a, b, c, epsilon, delta, leftValue):
    # Finding line segment
    while findFunctionValue(a, b, c, leftValue + delta) < 0:
        leftValue += delta
    rightValue = leftValue + delta

    # Finding root
    return findRoot(a, b, c, leftValue, rightValue, epsilon)



def findRootByStepsNegative(a, b, c, epsilon, delta, rightValue):
    # Finding line segment
    while findFunctionValue(a, b, c, rightValue - delta) > 0:
        rightValue -= delta
    leftValue = rightValue - delta

    # Finding root
    return findRoot(a, b, c, leftValue, rightValue, epsilon)

# Read params from STDIN
# f(x) = x^3 + ax^2 + bx + c
def readInputParams():
    epsilon = float(input("эпсилон - "))
    delta = float(input("дельта - "))
    a = float(input("a - "))
    b = float(input("b - "))
    c = float(input("c - "))
    return epsilon, delta, a, b, c

# Discriminant of 3x^2 + 2ax + b
def findDerivativeDiscriminant(a,b):
    return 4*a*a - 4*b*3

def findDerivativeRoots(a, discriminant):
    alpha = (-2 * a - discriminant ** 0.5) / 6
    beta = (-2 * a + discriminant ** 0.5) / 6
    return alpha, beta

def oneRootSearching(a, b, c, epsilon, delta):
    if abs(findFunctionValue(a, b, c, 0)) < epsilon:
        return findFunctionValue(a, b, c, 0)
    elif findFunctionValue(a, b, c, 0) < -epsilon:
        return findRootByStepsPositive(a, b, c, epsilon, delta, 0)
    elif findFunctionValue(a, b, c, 0) > epsilon:
        return findRootByStepsNegative(a, b, c, epsilon, delta, 0)

def moreThanOneOrOneRootSearching(a, b, c, epsilon, delta):
    alpha, beta = findDerivativeRoots(a, findDerivativeDiscriminant(a,b))
    if abs(findFunctionValue(a, b, c, alpha)) < epsilon and abs(findFunctionValue(a, b, c, beta)) < epsilon:
        return (alpha + beta) / 2
    elif findFunctionValue(a, b, c, beta) > epsilon:
        return findRootByStepsNegative(a, b, c, epsilon, delta, alpha)
    elif abs(findFunctionValue(a, b, c, beta)) < epsilon:
        return findRootByStepsNegative(a, b, c, epsilon, delta, alpha), beta
    elif findFunctionValue(a, b, c, alpha) > epsilon and findFunctionValue(a, b, c, beta) < -epsilon:
        return findRootByStepsNegative(a, b, c, epsilon, delta, alpha), findRoot(a, b, c, alpha, beta, epsilon) ,findRootByStepsPositive(a, b, c, epsilon, delta, beta)
    elif abs(findFunctionValue(a, b, c, alpha)) < epsilon:
        return alpha, findRootByStepsPositive(a, b, c, epsilon, delta, beta)
    elif findFunctionValue(a, b, c, alpha) < -epsilon:
        return findRootByStepsPositive(a, b, c, epsilon, delta, beta)
    
    

# Main function loop
def main():
    while True:
        try:
            epsilon, delta, a, b, c = readInputParams()
        except:
            print("bad data input!")
        
        derivativeDiscriminant = findDerivativeDiscriminant(a,b)

        if derivativeDiscriminant <= 0:
            print(oneRootSearching(a, b, c, epsilon, delta))
        else:
            print(moreThanOneOrOneRootSearching(a, b, c, epsilon, delta))





if __name__ == "__main__":
    main()
