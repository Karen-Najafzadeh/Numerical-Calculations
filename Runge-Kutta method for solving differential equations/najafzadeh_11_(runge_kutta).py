#inputs
x0 = float(input("what is the initial value of x? \n"))
y0 = float(input("what is the initial value of y? \n"))
h = float(input("what is the value of h? \n"))
x = float(input("what x you want to calculate? \ny(x=?)"))

#definitions
def f(x,y):
    return (x+y)
step = int((x-x0)/h)

# for the begining(n=0) yn = y0
def R_K2(x0, yn, step, h):
    for n in range(step):
        k1 = h*f(x0+(n*h),yn)
        k2 = h*f(x0+(n*h),yn+k1)
        # if we take m=n+1, then:
        ym = yn+0.5*(k1+k2)
        yn = ym
    return ym

def R_K4(x0, yn, step, h):
    for n in range(step):
        k1 = h*f(x0+(n*h),yn)
        k2 = h*f(x0+(n*h),yn+k1)
        k3 = h*f(x0+(n*h)+0.5*h,yn+0.5*k2)
        k4 = h*f(x0+(n*h)+h,yn+k3)
        # if we take m=n+1, then:
        ym = yn+(1/6)*(k1+2*k2+2*k3+k4)
        yn = ym
    return ym

print(R_K2(x0, y0, step, h))
print(R_K4(x0, y0, step, h))
