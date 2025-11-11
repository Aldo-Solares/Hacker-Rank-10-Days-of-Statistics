
#LINK https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem?isFullScreen=true

from math import e, factorial

def poisson(x, p):
    num = (x**p)*(e**-x)
    den = factorial(p)
    result = num/den
    print(f"{result:.3f}")

if __name__ == "__main__":
    x = float(input())
    p = int(input())
    poisson(x, p)