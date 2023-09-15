# mohammad sadegh najafzadeh
# 982042031

# a program to find the root of a mathematical function by bisection method


# definig the mathematical function here

def f(x):
    return (x**2)+x-1  # the function can be changed to anything else

# getting inputs

a = float(input("Where is the beggining of the range? \n"))
b = float(input("Where is the end of the range? \n"))
dx = float(input("ٌHow much accuracy is needed? (smaller number = more accurate)\n"))

# defining the middle of the range
middle = (b+a)/2
counter = 0
# algorithm
with open ('najafzadeh_1_(Bisection_root).txt','w') as file :
    intro = "mohammad sadegh najafzadeh\n982042031\na program to find the root of a mathematical function by bisection method\n\n"
    file.write(intro)



    while(True):
        middle = (b+a)/2
        counter += 1
        if ( abs(f(middle)) <= dx ):
            file.write( f"\nafter {counter} times of sclicing {round(middle,3)} is one of the possible roots of your function! \n end of program\n\n")
            break

        # sclising the range
        elif ( (f(a)*f(middle)) >= 0 ):
            a = middle
        elif ( (f(a)*f(middle)) <= 0 ):
            b = middle

        # we also want f(x_counter) where counter is even 
        if ( counter %2 == 0):
                file.write(f"\ncounter is even({counter}) so f(x_counter)={f(middle)}\n")

    file.write("if any unusual answers appeared, it's because of the weakness of the algorithm")
