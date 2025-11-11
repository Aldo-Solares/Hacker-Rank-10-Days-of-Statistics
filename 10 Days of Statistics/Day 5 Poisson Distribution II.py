
#LINK http://hackerrank.com/challenges/s10-poisson-distribution-2/problem?isFullScreen=true

def poisson(mean, base):
    result = base + 40 * (mean + mean**2)
    print(f"{result:.3f}")

if __name__ == "__main__":
    A, B = map(float, input().split())
    poisson(A, 160)
    poisson(B, 128)