
#LINK https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true

def weightedMean(X, W):
    n = len(X)
    arr = 0
    for i in range(n):
        arr += X[i]*W[i]
    print(f"{arr/sum(W):.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
