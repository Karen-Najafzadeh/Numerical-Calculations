# polynomial fitting
# problem:
# in this problem we are given a list of x and a list of y and we are asked to fit a polinomial function on these points.

# the algorithm leads us to have n+1 equations consisting of n+1 unknown variables and n+1 answers for these equations
# for example if n=2 then like this:
# x11*a0 + x12*a1 + x13*a2 = r11
# x21*a0 + x22*a1 + x23*a2 = r21
# x31*a0 + x32*a1 + x33*a2 = r31

# we can calculate the values for r11 and r21 and r31 by the algorithm
# and we also can calculate all x coefficients aswell
# the goal is to determine the values for a0 and a1 and a2 so we can form the polynomial function that can fitt the given sequence of x and y which is:
# f(x) = sigma A[k]*(x**k)  where k = range(0,n+1)
# which in, A is a 3*1 matrix containing the coefficients a1 , a2 and a3

# solution?
# if we take a 3*3 matrix of x and name it, say B, and a 3*1 matrix for r and name it R, then:
# we can calculate A with the following method:
# B * A = R
# A = B_inverse * R


# importing shit
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#taking input
degree = 2#int(input("how many numbers you have?\n"))
x = [0,0.25,0.5,0.75,1]#[float(input(f"what is the x No.{i+1}?\n")) for i in range(n)]  # for example =  
#print("\n now turn for y\n")
y = [1.0000,1.2840,1.6487,2.1170,2.7183]#[float(input(f"what is the y No.{i+1}?\n")) for i in range(n)]  # for example =  
m = len(x)

# defining the coefficients and some essential variables
A = np.array([sp.Symbol(f"a{i}") for i in range(degree+1)])
right_side = 0
left_side = 0
sigma = 0
right_side_values = []
left_side_values = []

# forming the n equations, n variables
for n in range(degree+1):
    for i in range(m):  
        right_side += ((x[i]**n)*y[i])
    right_side_values.append(right_side)
    right_side=0
    # the code above would calculate the right side of 'n'th equation ( sigma((x[i]**n)*(y[i])) )

    for t in range(degree+1):
        for j in range(m):
            sigma += (x[j]**(t+n))
        sigma*=A[t]
        left_side += sigma
        sigma=0
    left_side_values.append(left_side)
    left_side=0
    # and the code above will calculate the left side of the equation

# now we have a ((n+1) * 1) matrix named A that contains the variables we want to find their values
# and we also have a ((n+1) * 1) matrix named right_side_values which contains the answer for each set of equations
# just for simplicity we take right_side_values as R (and we also turn it to a np array so we can work with it later)so:
R = np.array(right_side_values)
# and now we will seprate the coefficients of left_side_values into a (n+1 * n+1) matrix named B
# then we will have a matrix equation that can lead us to the answer like this:
# B * A = R
# A = B_inverse * R
# Tadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
B = np.array(np.zeros((degree+1,degree+1)))
for i in range(degree+1):
    for j in range(degree+1):
        B[i,j] = left_side_values[i].coeff(A[j])

# here we go
B_inv = np.linalg.inv(B)
answers = np.dot(B_inv,R)
# now we assighn the answers to corresponding variables
for i in range(len(answers)):
    A[i]=A[i].subs(A[i],answers[i])


# now that we have the constants (A), time to form up the polynomial equation:
# f(x) = sigma A[k]*(x**k)  where k = range(0,degree+1)

x_symbol = sp.symbols("x")
f_x = 0
for k in range(degree+1):
    f_x += A[k]*(x_symbol**k)

print(f_x)


def F(X):
    y = []
    for i in range(len(X)):
        y.append(f_x.subs(x_symbol,X[i]))
    return y

x_axis = np.linspace(min(x),max(x),100)
plt.scatter(x,y,c="red")
plt.plot(x_axis,F(x_axis))
plt.show()
