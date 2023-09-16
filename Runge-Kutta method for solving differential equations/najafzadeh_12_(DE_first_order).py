# taking inputs
x0 = float(input("what is the initial value of x?\n"))
y0 = float(input("what is the initial value of y?\n"))
p0 = float(input("what is the initial value of p?\n"))
h  = float(input("what is h?\n"))
x  = float(input("what x you want to calculate? \ny(x=?) and p(x=?)\n"))


# defining the differential equations
def f1(x,y,p):
    return p

def f2(x,y,p):
    return -y+0.1*(1-y**2)*p

step = int((x-x0)/h)

# using Runge-Kutta algorithm:
def R_K4(x0, yn, pn, step, h):

    def xn(n):
        return x0+(n*h)
    
    def yn(n):
        return y0+(n*h)
    
    def pn(n):
        return p0+(n*h)

    for n in range(step):
        print(n,step,x0,y0,p0,h,x)
        k1 = h*f1(xn(n),yn(n),pn(n))
        l1 = h*f2(xn(n),yn(n),pn(n))

        k2 = h*f1(xn(x)+0.5*h,yn(n)+0.5*k1,pn(n)+0.5*l1)
        l2 = h*f2(xn(n)+0.5*h,yn(n)+0.5*k1,pn(n)+0.5*l1)

        k3 = h*f1(xn(x)+0.5*h,yn(n)+0.5*k2,pn(n)+0.5*l2)
        l3 = h*f2(xn(n)+0.5*h,yn(n)+0.5*k2,pn(n)+0.5*l2)

        k4 = h*f1(xn(x)+h,yn(n)+k3,pn(n)+l3)
        l4 = h*f2(xn(n)+h,yn(n)+k3,pn(n)+l3)

        # if we take m=n+1, then:
        ym = yn(n) + (1/6)*(k1+2*k2+2*k3+k4)
        pm = pn(n) + (1/6)*(l1+2*l2+2*l3+l4)

        yn=ym
        pn=pm
    return(f"yn={yn}, pn={pn},")

print(f"the results for the given equations are: {R_K4(x0,y0,p0,step,h)}")