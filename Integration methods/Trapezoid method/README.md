# Trapezoid integration method

This method is very similar to the [Rectangular Integration Method](https://github.com/Karen-Najafzadeh/Numerical-Calculations/tree/main/Integration%20methods/Reqtangular%20method) with only one difference that here, instead of rectangles we use trapezoids.
and the rest is pretty much the same.

So just like I explained [here](https://github.com/Karen-Najafzadeh/Numerical-Calculations/tree/main/Integration%20methods/Reqtangular%20method) before, we divine the area under the $f(x)$ curve into same hight (called $h$) right trapezoids so that the lengh of the top base of the trapezoid in position $x$ is f(x) and the lengh of the bottom base at $x = x+ih$ is $f(x+ih)$ where i goes from 1 to the number of trapezoids.

![image](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/1054fd68-93e1-4f30-acfb-691eea381e02)


Area of a right trapezoid is found with the formula, $area =(a+b)h/2$ where a and b are the two parallel sides (**bases**) and h is the hight.
<br /> So in our case in each trapezoid $a = f(x)$ and $b = f(x+h)$ so the area of each trapezoid will be $\frac{h}{2}(f(x_i)+f(x_{i+1}))$ and since we have n trapezoids the area under the curve (or as I should say $\int_{a}^{b}{f(x)}$) would be the sumation of all these trapezoids. Thus:

$$\int_{a}^{b}{f(x)}=\ \frac{h}{2}(f(x_0)+f(x_1))+\frac{h}{2}(f(x_1)+f(x_2))+\ \frac{h}{2}(f(x_2)+f(x_3))+\ \frac{h}{2}(f(x_3)+f(x_4))+\ \cdots\ +\frac{h}{2}(f(x_{n-1})+f(x_n))\ \ $$

As you can see except the first and the last base( $f(x_0) , f(x_n)$ ), we have two of each $f(x)$ so it's better to calculate the sum of these bases in one **for loop** and then the other two bases and finally sum them up to obtain the final answer.

![trapezoid integration method flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/df03c1cc-ef2c-4e29-8116-5046c9b11841)

This method is much more accurate than the rectangular method. Test the program and compare the answer with an online integral calculator and see how accurate it is.
