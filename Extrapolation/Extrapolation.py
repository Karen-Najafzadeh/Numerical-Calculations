#taking input
Range = int(input('how many numbers you want to enter?\n'))
x_axis = [float(input(f"enter x number {i+1} : ")) for i in range(Range)]
print(f"now it's time for f(x)s \n")
y_axis = [float(input(f"enter f({x_axis[i]}) : ")) for i in range(Range)]
x = float(input("give me x so i'll give you the f(x)!\n"))

if x > max(x_axis):
    y = y_axis[-2]+((x-x_axis[-2])*((y_axis[-2]-y_axis[-1])/(x_axis[-2]-x_axis[-1])))
else:
    y = y_axis[0]+((x-x_axis[0])*((y_axis[1]-y_axis[0])/(x_axis[1]-x_axis[0])))


print(f"f({x})={y}")
