# importing essentials for this example's mathematical functio
import math as math

# taking inputs
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
h = (b-a)/3

# defining the mathematical function
def f(x):
    return ((x-1)**2)/((math.e)**x)

# this is newton's method:
int = (3*(h/8))*(f(a)+3*f(a+h)+3*f(a+(2*h))+f(b))

#result
print(f'\nintegral is {int}')