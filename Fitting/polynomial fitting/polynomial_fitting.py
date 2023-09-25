# importing essentials
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#taking input
degree = int(input("what is the order of the function you want to fit?\n"))
m = int(input("how many numbers you have?\n"))
x = [float(input(f"what is x{i+1}?")) for i in range(m)]
print("\n now it's turn for y\n")
y = [float(input(f"what is f({x[i]})?")) for i in range(m)] 

# defining the coefficients and some essential variables
A = np.array([sp.Symbol(f"a{i}") for i in range(degree+1)])
left_side = 0
right_side = 0
sigma = 0
left_side_values = []
right_side_values = []

# forming the n equations, n variables
for n in range(degree+1):
    for i in range(m):  
        left_side += ((x[i]**n)*y[i])
    left_side_values.append(left_side)
    left_side=0
    # the code above would calculate the left side of 'n'th equation ( sigma((x[i]**n)*(y[i])) )

    for t in range(degree+1):
        for j in range(m):
            sigma += (x[j]**(t+n))
        sigma*=A[t]
        right_side += sigma
        sigma=0
    right_side_values.append(right_side)
    right_side=0
    # and the code above will calculate the right side of the equation

#forming up R and B
R = np.array(left_side_values)
B = np.array(np.zeros((degree+1,degree+1)))
for i in range(degree+1):
    for j in range(degree+1):
        B[i,j] = right_side_values[i].coeff(A[j])

# calculating inverse matrix of B and doing B_inverse * R 
B_inv = np.linalg.inv(B)
answers = np.dot(B_inv,R)

# now we assighn the answers to corresponding a_n variables
for i in range(len(answers)):
    A[i]=A[i].subs(A[i],answers[i])

# now that we have the constants (A), time to form up the polynomial equation:
# f(x) = sigma A[k]*(x**k)  where k = range(0,degree+1)
x_symbol = sp.symbols("x")
f_x = 0
for k in range(degree+1):
    f_x += A[k]*(x_symbol**k)

# trying to plot the result
def F(X):
    y = []
    for i in range(len(X)):
        y.append(f_x.subs(x_symbol,X[i]))
    return y

x_axis = np.linspace(min(x),max(x),100)
plt.scatter(x,y,c="red")
plt.plot(x_axis,F(x_axis))
plt.show()
