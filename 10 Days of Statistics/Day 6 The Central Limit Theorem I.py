
#LINK https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem?isFullScreen=true

from math import sqrt, erf

def TCL(w,b,mean,sd):
    max_w = w/b
    sd = (sd/sqrt(b))
    result = 0.5 * (1 + erf((max_w - mean) / (sd * sqrt(2))))
    print(f"{(result):.4f}")

if __name__ == "__main__":
    weigth = int(input())
    boxes = int(input())
    mean = int(input())
    sd = int(input())
    TCL(weigth,boxes, mean, sd)