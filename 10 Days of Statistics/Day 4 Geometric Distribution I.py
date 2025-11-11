
#LINK https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem?isFullScreen=true

def geometric(num, den, n_inspections):
    p = num / den
    q = 1 - p
    result = ((q)**(n_inspections-1))*p
    print(f"{result:.3f}")

if __name__ == "__main__":
    num, den = map(int, input().split())
    n = int(input().strip())
    geometric(num, den, n)