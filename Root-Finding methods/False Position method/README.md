
# False Position method  

In this method we have a range which there is a probability of existing a root. we call the beginning and the end of the range **a** and **b** respectively.

By using the straight line which connects f(a) to f(b) we can use the following algorithm to find one of the possible roots of our function.

# How does the method work

The first thing we do here is tho draw a straight line which connects **f(a)** to **f(b)** directly. To do so, first we need to calculate the Slope of this line(Let's call it **m**).

$$m\ =\ \frac{f(b)-f(a)}{b-a}$$

The linear equation of a straight line can be obtained by the following furmula:
$$f(x)-f(x_1)=m(x-x_1)$$
where $x$ and $a_1$ are any valid number on the x axis.

Lets put $a$ to the equation instead of $x_1$ and take $x$ as a place where the line crosses the $y=0$ line, meaning $f(x)=0$

Now we've got everything we need:
$$f(x)-f(a)=m(x-a)$$
$$-f(a)=m(x-a)$$
$$-\frac{f(a)}{m}\ =x-b$$
$$x=a-\frac{f(a)}{m}\$$
now if we rewrite m as what we defined earlier:
$$x\ =\ \ a\ -\ \frac{f(a)(b-a)}{f(b)-f(a)}$$

Now that we have the position where the line between $a$ and $b$ is $Zero$, we chack if our function in that position is too equal to zero. And by that I mean we check if $f(x)$ is equal or less than a number close to zero that we call $accuracy$
. If so, we have found the root, if not ? we change the range ($a$ and $b$) as shown in the flowchart below to focus on the part of function that there is  a probable root:

![False position flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/62c37b1b-e1cf-4474-bab1-e554569e8a5c)

We keep doing this until we find the root 
.It's obvious that the smaller $accuracy$ becomes, the higher precise aswer we get but also takes more time to be calculated. And remember that this is not the best way to find the roots of a function. I just coded this for fun.
