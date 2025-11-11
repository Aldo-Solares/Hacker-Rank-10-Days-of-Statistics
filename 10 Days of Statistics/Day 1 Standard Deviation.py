
#LINK https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=true

def stdDev(arr):
    n = len(arr)
    mean = sum(arr)/n
    sd = 0
    for x in arr:
        sd +=(x-mean)**2
    print((sd/n)**(1/2))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
