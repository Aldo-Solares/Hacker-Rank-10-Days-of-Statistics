
#LINK https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem?isFullScreen=true

from math import erf, sqrt

def normal(mean, sd, value):
    result = 0.5 * (1 + erf((value - mean) / (sd * sqrt(2))))
    print(f"{(1-result)*100:.2f}")

def normal_q3(mean, sd, value):
    result = 0.5 * (1 + erf((value - mean) / (sd * sqrt(2))))
    print(f"{(result)*100:.2f}")

if __name__ == "__main__":
    mean, sd = map(int, input().split())
    q1 = int(input())
    q2= int(input())
    normal(mean, sd, q1)
    normal(mean, sd, q2)
    normal_q3(mean, sd, q2)