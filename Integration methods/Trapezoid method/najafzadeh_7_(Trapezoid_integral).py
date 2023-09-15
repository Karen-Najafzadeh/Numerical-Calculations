# mohammad sadegh najafzadeh
# 982042031
# a program to calculate the integral of a matheatical function using trapezoid method

import math as math
a = float(input('beginning of the range?\n'))
b = float(input('end of the range?\n'))
h = float(input('accuracy?\n'))


iterations = (b-a)/h

def f(x):
    return ((x-1)**2)/((math.e)**x)


sum = 0
for i in range(1,int(iterations)+1):
    sum += 2*f(a+(h*i))

integral = (h/2)*(sum-f(a)-f(b))

with open ("najafzadeh_7_(Trapezoid_integral).txt", "w") as file:
    intro = "mohammad sadegh najafzadeh\n982042031\na program to calculate the integral of a matheatical function using trapezoid method\n\n"
    file.write(f"integral of currunt mathematical function is {integral}")