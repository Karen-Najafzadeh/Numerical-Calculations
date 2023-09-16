# importing requirements
import math

# inputs
a = float(input("what is the begining of your range?\n"))
b = float(input("what is the end of your range?\n"))
n = int(input("how many parts do you want to slice the integration range into? (more parts = more accurate answer)\n"))

# defining the mathematical function
# this is my example
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
print(f'with left reqtangle method, result for {n} slices is: \n {Left(n)}\n and for {n*10} slices is \n{Left(n*10)} see the difference? \n')
print(f'with right reqtangle method, result for {n} slices is: \n {Right(n)}\n and for {n*10} slices is \n{Right(n*10)} see the difference? \n')
print(f'with middle reqtangle method, result for {n} slices is: \n {Middle(n)}\n and for {n*10} slices is \n{Middle(n*10)} see the difference? \n')