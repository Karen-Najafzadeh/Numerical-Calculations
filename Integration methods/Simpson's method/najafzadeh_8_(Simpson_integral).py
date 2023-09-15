# mohammad sadegh najafzadeh
# 982042031
# a program to calculate the integral of a matheatical function using simpson method

a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
h = float(input('what is the h? (accuracy)\n'))

iterations = (b-a)/h

def f(x):
    return x

sum = 0

for i in range(1,int(iterations)):
    if i%2 == 0:
        sum += 2*f(a+(i*h))
    else:
        sum += 4*f(a+(i*h))
sum += f(a)+f(b)
integral = ((h/3)*sum)
with open ("najafzadeh_8_(Simpson_integral).txt", "w") as file:
    intro = "mohammad sadegh najafzadeh\n982042031\na program to calculate the integral of a matheatical function using simpson method\n\n"
    file.write(intro)
    file.write(f'integral is {round(integral,3)}')