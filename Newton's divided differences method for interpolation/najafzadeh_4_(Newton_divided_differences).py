# The Newton's divided differences method of Interpolation
# Mohammad Sadegh Najafzadeh
# 982042031
import sympy as sp
x_list = [0,1,3,6]
f = [1,-6,4,169]

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


with open ("najafzadeh_4_(Newton_divided_differences).txt", "w") as file:
    intro = "The Newton's divided differences method of Interpolation\nMohammad Sadegh Najafzadeh\n982042031\n"
    file.write(intro)
    file.write(f'\nfor this example, Coefficients are {Coefficient}\n')

    x = sp.symbols("x")
    p = f[0]+(x-x_list[0])*Coefficient[0]+((x-x_list[0])*(x-x_list[1])*Coefficient[1])+((x-x_list[0])*(x-x_list[1])*(x-x_list[2])*Coefficient[2])
    file.write(f"\np = {p}")