
#LINK https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem?isFullScreen=true

from math import factorial

def binomial(boy_ratio, girl_ratio):
    total = boy_ratio + girl_ratio
    p = boy_ratio / total
    q = 1 - p

    n = 6
    k = 3

    prob_total = 0
    for k in range(3, n+1):
        comb = factorial(n) / (factorial(k) * factorial(n - k))
        prob_total += comb * (p ** k) * (q ** (n - k))

    print(f"{prob_total:.3f}")

if __name__ == "__main__":
    boy_ratio, girl_ratio = map(float, input().split())
    binomial(boy_ratio, girl_ratio)