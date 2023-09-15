# Extrapolation
# mohammad sadegh najafzadeh
# 982042031
x_axis = [0,1,2,3,4,5]
y_axis = [0,1,2,3,4,5]


x = float(input('what x you want to find?'))

if x > max(x_axis):
    y = y_axis[-2]+((x-x_axis[-2])*((y_axis[-2]-y_axis[-1])/(x_axis[-2]-x_axis[-1])))
else:
    y = y_axis[0]+((x-x_axis[0])*((y_axis[1]-y_axis[0])/(x_axis[1]-x_axis[0])))

with open("najafzadeh_5_(Extrapolation).txt", "w") as file:
    intro ="Extrapolation\nmohammad sadegh najafzadeh\n982042031\n"
    file.write(f"y is {y}")
