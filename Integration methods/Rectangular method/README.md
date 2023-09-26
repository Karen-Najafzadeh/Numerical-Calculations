# Rectangular Integration Method
calculating the integration of a mathematical function with numerical methods is one of the easiest things to do. You just need to know the definition of integral.
<br />Suppose that we have a function $f(x)$. Then $\int_{a}^{b}{f(x)}$ means the area under the curve of $f(x)$ and between $a$ and $b$ where in the picture below, i've marked as blue

![integral defenition](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/3e37772c-8e02-45b1-99fa-ab3400e50f11)

As the blue shape does not look like any common shape that we know how to calculate its area, we are going to break it into many little rectangles with the same width ($h$)
<br />With this approche we can calculate $\int_{a}^{b}{f(x)}$ approximately

# integral methods
 1. Left Rectangle method
 2. right Rectangle method
 3. Middle Rectangle method

# 1 Right Rectangle Integration method
In this method we chop the area into same width ($h$) rectangles So that the top **Right** tip of every rectangle touches $f(x)$ curve. Just like the picture below:

![image](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/6dbbfe05-b228-4210-ad59-e2309b7d8064)

Now we have n rectangles ($n =\frac{b-a}{h}$) with the lengh of $f(x)$ and the width of $h$.
<br /> we can calculate the area of these rectangles, right? 
$$\int_{a}^{b}{f(x)}\ =\ \sum_{i\ =\ 1}^{n}{f(x_i)h}$$
where $x_i = a+(ih)$. As simple as that
we start the sumation from 1 to n because the top right tip of the first rectangle is in $x = a+1h$ which by the defenition means $x_1$ so we start with $i=1$
![right rectangular integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/ed6f97d2-719d-414c-8146-5d5ddb89a73d)


# 2 Left Rectangle Integration method
We do just the same we did in the previous method but in this one, we chop the area into same width ($h$) rectangles so that the top **Left** tip of every Rectangle touches $f(x)$ curve Just like the picture below:

![image](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/9e94649b-d648-47ee-9822-c0530ae3774e)

But this time we start the iterations from $i=0$ upto $n-1$
$$\int_{a}^{b}{f(x)}\ =\ \sum_{i\ =\ 0}^{n-1}{f(x_i)h}$$
![rectangular integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/13ea7ec3-3aef-49eb-be3a-99a165f93f70)

# 3 Middle Rectangle Integration method

Just like the same but in this method we are interested in the points where that point is the middle of the rectangle.

![image](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/151f0ee8-9cd5-4b03-8c07-2ef900103828)

<br />how to obtain the middle? 
$$middle\ =\ \frac{x_i+x_{(i+1)}}{2}$$

Thus: 
$$\int_{a}^{b}{f(x)}=\sum_{i=0}^{n-1}{f\left(\frac{x_i+x_{(i+1)}}{2}\right)h\ }$$

![middle rectangular integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/fb517385-27a3-411a-96c8-3329698448e2)

