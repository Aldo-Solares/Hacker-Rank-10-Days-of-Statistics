
#LINK https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem?isFullScreen=true

from math import factorial

def binomial(n, k, p):
    return factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * ((1 - p) ** (n - k))

if __name__ == "__main__":
    p, n = map(int, input().split())
    p = p/100
    prob_at_most_2 = sum(binomial(n, k, p) for k in range(0, 3))
    print(f"{prob_at_most_2:.3f}")
    
    prob_at_least_2 = sum(binomial(n, k, p) for k in range(2, n + 1))
    print(f"{prob_at_least_2:.3f}")
