
#LINK https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem?isFullScreen=true

from math import sqrt, erf

def TCL(t,s,mean,sd):
    max_t = t/s
    sd = (sd/sqrt(s))
    result = 0.5 * (1 + erf((max_t - mean) / (sd * sqrt(2))))
    print(f"{(result):.4f}")

if __name__ == "__main__":
    tickets = int(input())
    students = int(input())
    mean = float(input())
    sd = float(input())
    TCL(tickets,students, mean, sd)
