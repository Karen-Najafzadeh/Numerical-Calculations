# Rectangular Integration Method
calculating the integration of a mathematical function with numerical methods is one of the easiest things to do. You just need to know the definition of integral.
<br />Suppose that we have a function $f(x)$. Then $\int_{a}^{b}{f(x)}$ means the area under the curve of $f(x)$ and between $a$ and $b$ where in the picture below, i've marked as blue

![integral defenition](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/edba3bdf-2a0e-4620-b261-be026d5e944d)

As the blue shape does not look like any common shape that we know how to calculate its area, we are going to break it into many little rectangles with the same width ($h$)
<br />With this approche we can calculate $\int_{a}^{b}{f(x)}$ approximately

# integral methods
 1. Left Rectangle method
 2. right Rectangle method
 3. Middle Rectangle method

# 1 Right Rectangle Integration method
In this method we chop the area into same width ($h$) rectangles So that the top **Right** tip of every rectangle touches $f(x)$ curve. Just like the picture below:

![right rectangle](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/f7d66c0b-0848-4284-9447-7a0ee1fd819c)

Now we have n rectangles ($n =\frac{b-a}{h}$) with the lengh of $f(x)$ and the width of $h$.
<br /> we can calculate the area of these rectangles, right? 
$$\int_{a}^{b}{f(x)}\ =\ \sum_{i\ =\ 1}^{n}{f(x_i)h}$$
where $x_i = a+(ih)$. As simple as that
we start the sumation from 1 to n because the top right tip of the first rectangle is in $x = a+1h$ which by the defenition means $x_1$ so we start with $i=1$
![reqtangular integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/3fb52000-25da-49a1-afc3-0a5ff986c076)


# 2 Left Rectangle Integration method
We do just the same we did in the previous method but in this one, we chop the area into same width ($h$) rectangles so that the top **Left** tip of every Rectangle touches $f(x)$ curve Just like the picture below:

![left rectangle](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/7eadd3e6-c9c3-4df5-b098-436e9ebc9f12)

But this time we start the iterations from $i=0$ upto $n-1$
$$\int_{a}^{b}{f(x)}\ =\ \sum_{i\ =\ 0}^{n-1}{f(x_i)h}$$

![left reqtangular integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/3aae0fe8-a5c0-45da-999b-4f8729660ef0)

# 3 Middle Rectangle Integration method

Just like the same but in this method we are interested in the points where that point is the middle of the rectangle.

![middle rectangle](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/1890bd8f-57bb-4136-b016-fa59bd3303b2)

<br />how to obtain the middle? 
$$middle\ =\ \frac{x_i+x_{(i+1)}}{2}$$

Thus: 
$$\int_{a}^{b}{f(x)}=\sum_{i=0}^{n-1}{f\left(\frac{x_i+x_{(i+1)}}{2}\right)h\ }$$

![middle reqtangular integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/f3c63bb6-78e3-4af3-8004-3f2e7bd9e2c9)

