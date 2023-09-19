# importing essentials for this example's mathematical function
import math as math

# taking inputs
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
h = float(input('how accurate? (less number = more accuracy)\n'))

# defenitions
def f(x):
    return ((x-1)**2)/((math.e)**x)
sum = 0
iterations = int((b-a)/h)

# the actual algorithm
# we start the iteration from 1 because we don't want to include the first and the last trapezoid in the calculation
for i in range(1,iterations):
    sum += 2*f(a+(h*i))

integral = (h/2)*(sum+f(a)+f(b))

#result
print(f"integral of currunt mathematical function is {integral}")