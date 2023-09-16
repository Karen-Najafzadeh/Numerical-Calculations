# importing essentials for this example's mathematical function
import math as math

# taking inputs
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))

# defining the mathematical function
def f(x):
    return 1/(math.sqrt(1-x**2))

# the method
int = ((b-a)/2)*(f((1/2)*((-b+a)*(math.sqrt(3)/3)+(b+a)))+f((1/2)*((b-a)*(math.sqrt(3)/3)+(b+a))))

#result
print(f"integral for this function is {int}")
