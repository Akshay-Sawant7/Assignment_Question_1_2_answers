
import math                      #import math function


def findRoots(a, b, c):          #def function

    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b / (2 * a))
    else:  # d<0
        print("Roots are complex")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


findRoots(2,10,8)                                     #call function







