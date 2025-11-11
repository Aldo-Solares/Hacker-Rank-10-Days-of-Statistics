
#LINK https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem?isFullScreen=true

from math import sqrt

def TCL(n, mean, sd, z):
    sd = (sd/sqrt(n))
    ci = sd*z
    print(f"{(mean-ci):.4f}")
    print(f"{(mean+ci):.4f}")

if __name__ == "__main__":
    n = int(input())
    mean = int(input())
    sd = int(input())
    distribution = float(input())
    z = float(input())
    TCL(n, mean, sd, z)
