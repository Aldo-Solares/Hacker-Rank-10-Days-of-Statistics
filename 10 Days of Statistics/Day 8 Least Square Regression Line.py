
#LINK https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem?isFullScreen=true

from statistics import mean, covariance, variance

def LSRL(X,Y):
    cov_xy = covariance(X,Y)
    var_x = variance(X)
    b = cov_xy/var_x
    a = mean(Y)-b*mean(X)
    result = a + b*80
    print(cov_xy, var_x)
    
    print(f"{(result):.3f}")

if __name__ == "__main__":
    n = 5
    X = []
    Y = []
    for i in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    LSRL(X,Y)