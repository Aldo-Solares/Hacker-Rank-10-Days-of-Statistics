
#LINK https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true

def median(a):
    n = len(a)
    a.sort()
    m = n//2
    if n % 2 == 1:
        return a[m]
    else:
        return (a[m-1] + a[m]) // 2

def quartiles(arr):
    arr.sort()
    n = len(arr)
    m = n//2

    if n % 2 == 0:
        lower = arr[:m]
        upper = arr[m:]
    else:
        lower = arr[:m]
        upper = arr[m+1:]

    Q1 = median(lower)
    Q2 = median(arr)
    Q3 = median(upper)

    return str(Q1), str(Q2), str(Q3)


if __name__ == '__main__':
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)
    print("\n".join(res))
