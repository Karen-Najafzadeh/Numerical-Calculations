# Runge-Kutta method for solving differential equations

Runge-Kutta method is one of the most powerful methods for solving initial values differential equations.<br />
In this method we are given a differential equation, and an initial value for that equation and a step size, and we can solve the equation for any desirable conditions.


# Second order Runge-Kutta (mathematics)
Suppose that we have a mathematical function $y' = f(x,y)$ where y is an unknown function. We also have an initial state $y_0 = x_0$. By using this method and with taking a step $h>0$ we can determine the value of y function at any desired position like x, meaning $y_n = y(x)$ is calcutable, where n is an integer which varies from $n=0$ to $n=\frac{x-x_0}{h}$ 
<br />Now we can start from $y_0$ and get closer and closer to $y(x)$ step by step. In each step we have to calculate two expressions

*  $K_1 = hf(x_n , y_n)$
*  $K_2 = hf(x_n + h , y_n + K_1)$

Where $f(x,y)$ is given by the problem and $y_n$ and $x_n$ are:

$$y_{n+1} = y_n + \frac{1}{2}(K_1 + K_2) \ \ \ \ \ \ \ and \ \ \ \ \ \ \ \ x_n = x_0 + nh $$

Now by having these parameters we can loop over $n$ and calculate $y(m)$ easy as that!

#  Second order Runge-Kutta (Flowchart) 

The variable $n$ in the mathematics section and the variable **step** here in the flowchart are equivalent dont get confused, and the variable m in $y_m$ is considered to be m=n+1

![Runge-Kutta 2nd order flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/2d9284b0-8a7d-4046-aa7b-625dbe1b2a86)

# Fourth order Runge-Kutta (mathematics)

The mathematics here are almost identical as the Second order Runge-Kutta method but the difference in each iteration is, instead of calculating $K_1$, $K_2$ and $y_{n+1}$ we have to calculate the following expressions:

* $K_1 = hf(x_n , y_n)$
* $K_2=\ hf(x_n+\frac{h}{2},\ y_n+\frac{K_1}{2})$
* $K_3=\ hf(x_n+\frac{h}{2},\ y_n+\frac{K_2}{2})$
* $K_4=\ hf(x_n+h,\ y_n+K_3)$

# Fourth order Runge-Kutta (Flowchart)

Just like before The variable $n$ in the mathematics section and the variable **step** here in the flowchart are equivalent dont get confused, and the variable m in $y_m$ is considered to be m=n+1

![Runge-Kutta 4th order flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/74d0034b-76db-43f6-989d-0a4852d20371)
