# importing essentials for this example's mathematical function
import math as math

# taking inputs
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
h = float(input('how accurate? (less number = more accuracy)\n'))



# defenitions
# this is a simple example
def f(x):
    return ((x-1)**2)/((math.e)**x)
iterations = (b-a)/h
sum = 0

# the actual algorithm
for i in range(1,int(iterations)):
    if i%2 == 0:
        sum += 2*f(a+(i*h))
    else:
        sum += 4*f(a+(i*h))
sum += f(a)+f(b)
integral = ((h/3)*sum)

print(f'integral is {round(integral,3)}')