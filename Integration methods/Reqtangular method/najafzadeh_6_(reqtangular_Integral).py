# Mohammad Sadegh Najafzadeh
# 982042031
# a program to calculate the integral of a mathematical function using reqtangular method (right, left and middle points)
# importing requirements
import math

# inputs
b = 5
a = 0.2

# defining the mathematical function
def F(x):
    return ((x-1)**2)/((math.e)**x)


# left point method
def Left(n):
    integral = 0
    h = (b-a)/n
    for i in range(0,n):
        integral += F((a+(h*i)))
    return integral*h

# right point method
def Right(n):
    integral = 0
    h = (b-a)/n
    for i in range(1,n+1):
        integral += F((a+(h*i)))
    return integral*h

# middle point method
def Middle(n):
    integral = 0
    h = (b-a)/n
    for i in range(0,n):
        integral += F(((a+(h*i))+((a+(h*(1+i)))))/2)
    return integral*h

# resunts
with open ("najafzadeh_6_(reqtangular_Integral).txt", "w") as file:
    intro = "Mohammad Sadegh Najafzadeh\n982042031\na program to calculate the integral of a mathematical function using reqtangular method (right, left and middle points)\n\n"
    file.write(intro)

    file.write(f'with left reqtangle method, result for n = 10 is: \n {Left(10)}\n and for n = 100 is \n{Left(100)}\n')
    file.write(f'with right reqtangle method, result for n = 10 is: \n {Right(10)}\n and for n = 100 is \n{Right(100)}\n')
    file.write(f'with middle reqtangle method, result for n = 10 is: \n {Middle(10)}\n and for n = 100 is \n{Middle(100)}\n')
    file.write('And the absolute magnitude of this integral is: 0.67629...\n\n')