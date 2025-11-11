
#LINK https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem?isFullScreen=true

def MLR(x,y):
    pass

if __name__ == "__main__":
    m, n = map(int, input().split())
    f1, f2, f3 = [], [], []
    for i in range(n):
        x,y,z = map(float, input().split())
        f1.append(x)
        f2.append(y)
        f3.append(z)
    q = int(input())
    
    for i in range(m):
        a, b = map(float, input().split())
        MLR(a, b)