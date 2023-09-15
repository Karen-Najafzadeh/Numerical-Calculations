# mohammad sadegh najafzadeh
# 982042031
# a program to calculate the integral of a matheatical function using 4 points Newton method


import numpy as np
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
h = (b-a)/3

def f(x):
    return 2*x+3
int = (3*(h/8))*(f(a)+3*f(a+h)+3*f(a+(2*h))+f(b))


with open ("najafzadeh_9_(newton_integral).txt", "w") as file:
    intro = "mohammad sadegh najafzadeh\n982042031\na program to calculate the integral of a matheatical function using 4 points Newton method\n\n"
    file.write(intro)
    file.write(f'\nintegral is {int}')