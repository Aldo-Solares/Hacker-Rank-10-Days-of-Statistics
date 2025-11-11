
#LINK https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true

from statistics import mean, median, multimode

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
data_mean = mean(arr)
data_median = median(arr)
data_mode = multimode(arr)
data_mode.sort()

print(mean(arr))
print(median(arr))
print(data_mode[0])