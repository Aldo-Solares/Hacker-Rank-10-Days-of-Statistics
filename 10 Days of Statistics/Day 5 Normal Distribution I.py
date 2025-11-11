
#LINK https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem?isFullScreen=true

from math import erf, sqrt
    
def normal_q1(mean, sd, value):
    result = 0.5 * (1 + erf((value - mean) / (sd * sqrt(2))))
    print(f"{result:.3f}")
    
def normal_q2(mean, sd, value_1, value_2):
    result = 0.5 * (1 + erf((value_1 - mean) / (sd * sqrt(2))))
    result_2 = 0.5 * (1 + erf((value_2 - mean) / (sd * sqrt(2))))
    print(f"{result_2-result:.3f}")

if __name__ == "__main__":
    mean, sd = map(int, input().split())
    q1 = float(input())
    lower, upper = map(int, input().split())
    normal_q1(mean, sd, q1)
    normal_q2(mean, sd, lower, upper)