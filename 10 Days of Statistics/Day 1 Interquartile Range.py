
#LINK https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true

def interQuartile(val, freq):
    
    n = len(freq)
    arr = []
    
    for i in range(n):
        arr.extend([val[i]]*freq[i])
    Q1, Q2, Q3 = quartiles(arr)
    print(f"{Q3-Q1:.1f}")

def quartiles(arr):
    n = len(arr)
    arr.sort()
    m = n//2
    
    if n%2 == 0:
        lower = arr[:m]
        higher = arr[m:]
        Q2 = (arr[m-1]+arr[m])//2
    else:
        lower = arr[:m]
        higher = arr[m+1:]
        Q2 = arr[m]
        
    Q1 = median(lower)
    Q3 = median(higher)
    
    return Q1, Q2, Q3

def median(arr):
    n = len(arr)
    m = n//2
    
    if n%2 == 0:
        return (arr[m-1]+arr[m])//2
    else:
        return arr[m]
        

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
