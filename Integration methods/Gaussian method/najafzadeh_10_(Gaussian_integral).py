# mohammad sadegh najafzadeh
# 982042031
# a program to calculate the integral of a matheatical function using 2 points Gaussian method


import math
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))

def f(x):
    return 1/(math.sqrt(1-x**2))

int = ((b-a)/2)*(f((1/2)*((-b+a)*(math.sqrt(3)/3)+(b+a)))+f((1/2)*((b-a)*(math.sqrt(3)/3)+(b+a))))
with open ("najafzadeh_10_(Gaussian_integral).txt", "w") as file:
    intro = "mohammad sadegh najafzadeh\n982042031\na program to calculate the integral of a matheatical function using 2 points Gaussian method\n\n" 
    file.write(intro)
    file.write(f"integral for this function is {int}")
