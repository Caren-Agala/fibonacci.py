import math
def PerfectSquare(x) :
    s = int(math.sqrt(x))
    return s*s ==x

n = int(input("enter the number to be checked:"))
res1 = 5*(n*n)+4
res2 = 5*(n*n)-4

if PerfectSquare(res1) or PerfectSquare(res2) :
    print(n, "is fibonacci number")
else:
    print(n, "is not fibonacci number")

    #A number is fibonacci if one or both of the values of res1 and res2 is a perfect square
