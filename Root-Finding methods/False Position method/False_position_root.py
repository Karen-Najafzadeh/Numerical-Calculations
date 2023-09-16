#a program to find the root of a mathematical function using false position (also known as secant) method.
# mohammad sadegh najafzadeh
# 982042031
# taking inputs
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
eps = float(input('what is the accuracy?\n'))

#defining the mathematical function
def f(x):
    return (3*x)-3


# algorithm
with open('najafzadeh_2_(False_position_root).txt','w') as file:
    intro = "a program to find the root of a mathematical function using false position (also known as secant) method.\nmohammad sadegh najafzadeh\n982042031\n\n"
    file.write(intro)
    while True:
        x = (((-f(a))*(b-a))/(f(b)-f(a)))+ a
        if abs(f(x))<=eps:
            file.write(f'\nroot is {x}\n')
            break
        else:
            if f(x)*f(a)<0:
                b=x
            else:
                a=x
