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
iterations = (b-a)/h

# the actual algorithm
for i in range(1,int(iterations)+1):
    sum += 2*f(a+(h*i))

integral = (h/2)*(sum-f(a)-f(b))

#result
print(f"integral of currunt mathematical function is {integral}")