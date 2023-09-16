# taking inputs
a = float(input('what is the beginning of the range?\n'))
b = float(input('what is the end of the range?\n'))
accuracy = float(input('How much accuracy is needed? (smaller number = more accurate)\n'))

#defining the mathematical function
def f(x):
    return (3*x)-3


# algorithm
while True:
    x = (((-f(a))*(b-a))/(f(b)-f(a)))+ a
    if abs(f(x))<=accuracy:
        print(f'\n{x} is one of the possible roots of your function!\n')
        break
    elif f(x)*f(a)<0:
        b=x
    else:
        a=x
