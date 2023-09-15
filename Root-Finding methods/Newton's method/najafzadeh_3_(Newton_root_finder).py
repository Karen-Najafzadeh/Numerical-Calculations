#a program to find the root of a mathematical function using Newton-Raphson method.
# mohammad sadegh najafzadeh
# 982042031
#importing essentials
import sympy as sp

#definitions
x = sp.symbols("x")
eps = float(input("how accurate?\n"))
x_i = float(input("give me a random x\n"))

def f(x):
    return x**2
m = sp.diff(f(x),x)

#algorithm

with open("najafzadeh_3_(Newton_root_finder).txt",'w') as file:
    intro = "a program to find the root of a mathematical function using Newton-Raphson method.\nmohammad sadegh najafzadeh\n982042031\n"
    file.write(intro)
    while True:
        x_new = ((-f(x_i))/(m.subs(x,x_i)))+x_i
        if abs(f(x_new))<=eps:
            file.write(f"\nroot is {x_new}\n")
            break
        else:
            x_i = x_new