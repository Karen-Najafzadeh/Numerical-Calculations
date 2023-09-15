def Library_Installer():
    #if any problems show up when we try to import a library, this will fix the problem
    import os #anyone have this library by default, so there won't be any problems here

    # finding user's desktop directory path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

    #creating a .bat file and writing the cmd commands that you wnat
    with open (f"{desktop}\my_bat.bat",'w') as file:
        file.write(f'pip install numpy')
        file.write(f'pip install matplotlib')

    # running the .bat file
    os.system(f"{desktop}/my_bat.bat")

    # deleting the .bat file after we are finished installing
    os.remove(f"{desktop}\my_bat.bat")

# here we go, start of program
try:
    import matplotlib.pyplot as plt
    import numpy as np
except:
    Library_Installer()

# taking input from user
n = int(input("how many numbers you have?\n"))
x = [float(input(f"what is the x No.{i+1}?\n")) for i in range(n)]  # for example =  [1,3,4,6,8,9,11,14]
print("\n now turn for y\n")
y = [float(input(f"what is the y No.{i+1}?\n")) for i in range(n)]  # for example = [1,2,4,4,5,7,8,9] 

# nececery definitions
x2 = [x[i]**2 for i in range(n)]
xy = [x[i]*y[i] for i in range(n)]
s_xy = sum(xy)
s_x = sum(x)
s_y = sum(y)
s_x2 = sum(x2)


# if f = a*x + b, then:
a = ((n*s_xy)-(s_x*s_y)) / ((n*s_x2)-(s_x**2))
b = ((s_y*s_x2)-(s_x*s_xy)) / ((n*s_x2)-(s_x**2))

# here is our function
def f(x): 
    return a*x+b

# calculating error for this method
K2 = 0
for i in range(n):
    K2 += (y[i]-f(x[i]))**2

# results
print(f"the fitting function for these numbers is: {round(a,3)}x + {round(b,3)}\nand the error is: {K2**(1/2)}")
x_axis = np.linspace(min(x),max(x),100)
plt.scatter(x,y,c='red')
plt.plot(x_axis,f(x_axis))
plt.show()

# the end