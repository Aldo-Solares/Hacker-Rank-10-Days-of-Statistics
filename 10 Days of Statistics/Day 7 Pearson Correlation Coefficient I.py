
#LINK https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem?isFullScreen=true

from statistics import mean, covariance, stdev

def pearson(X, Y):
    sdx= stdev(X, mean(X))
    sdy= stdev(Y, mean(Y))
    cov = covariance(X, Y)
    print(f"{cov/(sdx*sdy):.3f}")


if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(int, input().split()))
    pearson(X, Y)