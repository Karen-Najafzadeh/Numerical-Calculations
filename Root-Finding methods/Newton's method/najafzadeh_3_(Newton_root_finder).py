#importing essentials
import sympy as sp

#definitions
x = sp.symbols("x")
precision = float(input("how accurate?\n"))
x_i = float(input("give me a random x\n"))

def f(x):
    return x**2

m = sp.diff(f(x),x)

#algorithm


while True:
    x_new = ((-f(x_i))/(m.subs(x,x_i)))+x_i
    if abs(f(x_new))<= precision:
        print(f"\n{x_new} is one of the possible roots\n")
        break
    else:
        x_i = x_new