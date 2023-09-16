# importing essentials
import sympy as sp

#taking input
Range = int(input('how many numbers you want to enter?\n'))
x_list = [float(input(f"enter x number {i+1} : ")) for i in range(Range)]
print(x_list)
f = [float(input(f"enter x number {i+1} : ")) for i in range(Range)]

first_list = f
second_list = []
Coefficient = []

# trying to find the Coefficients of differences
for i in range(1,len(x_list)+1):
    for j in range(len(f)-i):
        second_list.append((first_list[j+1]-first_list[j])/(x_list[j+i]-x_list[j]))
    try:
        Coefficient.append(second_list[0])
        first_list = second_list
        second_list = []
    except:
        break

print(f'\nfor this example, Coefficients are {Coefficient}\n')

x = sp.symbols("x")
p = f[0]+(x-x_list[0])*Coefficient[0]+((x-x_list[0])*(x-x_list[1])*Coefficient[1])+((x-x_list[0])*(x-x_list[1])*(x-x_list[2])*Coefficient[2])
print(f"\np = {p}")