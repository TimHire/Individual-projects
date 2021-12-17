import numpy as py
import math

def derivative(f, a):
    h = 0.00000000001
    return (f(a+h) - f(a-h)) / (2*h)

def sign_change(f, first, second, interval):
    iterations = int(((second-first)/interval) - 1)
    solutions = 0
    out = []
    for iter in range(iterations):
        fo1 = f(first + iter*interval)
        fo2 = f(first + (iter+1)*interval)
        if fo1 >= 0 and fo2 <= 0 or fo1 <= 0 and fo2 >= 0:
            out.append([round((first + iter*interval), 4), round((first + (iter+1)*interval), 4)])
            solutions += 1
    if solutions != 0:
        #print(out)
        print("There are {} roots between {} and {}".format(solutions, first, second))
        return out
    else:
        return "There are no roots between {} and {}".format(first, second)

def newton(f, x0):
    xn = x0
    epsilon = 10**-10
    max_iter = 20
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print("Found solution after {} iterations: {}".format(n, round(xn, 10)))
            return round(xn, 10)
        Dfxn = derivative(f, xn)
        if Dfxn == 0:
            print("Zero derivative. No solution found as this is a turning point")
            return None
        xn = xn - fxn/Dfxn
    print("Exceeded maximum iterations. No solution found.")
    return None

def auto_root(f, start, end):
    solutions = sign_change(f, start, end, 0.0005)
    out = []
    for y in range(len(solutions)):
        x0 = solutions[y][0]
        x1 = solutions[y][1]
        sol = newton(f, x0)
        if sol is None:
            sol = newton(f, x1)
        out.append(sol)
    return "The solutions between {} and {} are {}".format(start, end, out)

p = lambda x: x**8 - 4*x**6 + x**5 + x + 2
#print(newton(p, 1))
#print(sign_change(p, -1, 2, 0.005))
print(auto_root(p, -10, 10))
