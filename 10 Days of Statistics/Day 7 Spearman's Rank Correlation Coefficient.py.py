
#LINK https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem?isFullScreen=true

def spearman(n,X, Y):
    rank_x = lambda X: [sorted(X).index(x) + 1 for x in X]
    rank_y = lambda Y: [sorted(Y).index(x) + 1 for x in Y]
    di = sum([(x-y)**2 for x,y in zip(rank_x(X),rank_x(Y))])
    result = 1-((6*di)/(n*((n**2)-1)))
    print(f"{result:.3f}")

if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(int, input().split()))
    spearman(n,X, Y)