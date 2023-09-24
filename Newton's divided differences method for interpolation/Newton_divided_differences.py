# importing essentials
import sympy as sp

#taking input
Range = int(input('how many numbers you want to enter?\n'))
x_list = [float(input(f"enter x number {i+1} : ")) for i in range(Range)]
f = [float(input(f"enter f({x_list[i]}) : ")) for i in range(Range)]

left_column = f
right_column = []
Coefficient = []

# trying to find the Coefficients of differences
for i in range(1,len(x_list)):
    for j in range(0,len(left_column)-1):
        right_column.append((left_column[j+1]-left_column[j])/(x_list[j+i]-x_list[j]))
    
    Coefficient.append(right_column[0])
    left_column = right_column
    right_column = []

print(f'\nfor this set of data, divided difference Coefficients are {Coefficient}\n')


# making P(X) and asking user to enter x to calculate P(x)
def interpolating(x_list = x_list, Coefficient = Coefficient, x = sp.symbols("x")):
    m = x-x_list[0]
    sum = f[0]+m*Coefficient[0]
    for i in range(1, len(Coefficient)):
        m *= (x-x_list[i])
        sum += m*Coefficient[i]
    print(f"\nP(x) = {sum}")
    x_i = float(input(f"give me x so i'll give you f(x):\n"))
    print(sum.subs(x,x_i))

interpolating()