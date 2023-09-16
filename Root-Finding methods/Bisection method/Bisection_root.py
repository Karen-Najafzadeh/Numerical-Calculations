# definig the mathematical function here
def f(x):
    return (x**2)+x-1  # for example

# getting inputs

a = float(input("Where is the beggining of the range? \n"))
b = float(input("Where is the end of the range? \n"))
dx = float(input("ٌHow much accuracy is needed? (smaller number = more accurate)\n"))

# algorithm

while(True):
    middle = (b+a)/2
    #checking if the middle point is the answer or not 
    if ( abs(f(middle)) <= dx ):
        print( f"\n{round(middle,3)} is one of the possible roots of your function! \n end of program\n\n")
        break

    # sclising the range
    elif ( (f(a)*f(middle)) > 0 ):
        a = middle
    elif ( (f(a)*f(middle)) <= 0 ):
        b = middle


print("if any unusual answers appeared, it's because of the weakness of the algorithm")
