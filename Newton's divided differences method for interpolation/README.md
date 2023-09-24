# Newton's divided difference interpolation method

Interpolation is very useful when you have a bunch of data that you want to make sense out of them. It's useful in many fields specialy in astronomy, physics and many other sciences.<br />
Here I've written a program which takes **n** numbers (**$x_i$**) and their corresponding $f(x_i)$  and then, by using Newton's divided difference method gives you the best mathematical function that can fit the given data.

# warnings
* First of all I've witten this program for fun so it's not that perfect, but it's practical.<br />
* Second, currently this program can't find the function for cases that have under 4 pair of data.(but I'll fix it, having the time)<br />
* Finally, It only calculates till third diveded difference, but don't worry, because the errorrs are neglectable.(I'll try to fix this too)<br />

# Mathematics
* What is divided difference?
  
Suppose that we have a bunch of data like this:
  
| i | 0 | 1 | 2 | 3 | ... | n |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| $x_i$ | 0 | 1 | 3 | 6 |... | m |
| $f(x_i)$ | 1 | -6 | 4 | 169 | ... | $f(m)$ |

where i is just a counter, an index to help keep tracking of the data. And $x_i$ can be any real number and $f(x_i)$ is the function value at $x_i$.

The following expression is defined as newton's first divided difference:

$$ F\left[x_i,x_{i+1}\right]\ =\ \frac{f(x_i)-f(x_{i+1})}{x_i-x_{i+1}} $$

Second divided difference:

$$ F\left[x_i,x_{i+1},x_{i+2}\right]\ =\ \frac{F\left[x_i,x_{i+1}\right]-F\left[x_{i+1},x_{i+2}\right]}{x_i-x_{i+2}} $$

And so on ...

* The function

Now by using the formula I just introduced, we can obtain a polynomial function ( $P(x)$ ) that fits the data we have. so by having the mathematical function you can accurately predict any desired $f(x)$ 

$$ P(x)\ =\ f(x_0)+(x-x_0)F\left[x_0,x_1\right]+\ (x-x_0)(x-x_1)F\left[x_0,x_1,x_2\right]+\cdots+(x-x_0)(x-x_1)\cdots(x-x_{n-1})F\left[x_0,x_1,x_2,\cdots x_n\right] $$


Woho! That's a lot of work, isn't it? But don't worry there is a more simple way to calculate the divided differences. Let me explain with a simple example. Supose we have the given set of data:

| i | 0 | 1 | 2 | 3 | 4 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| $x_i$ | -2 | -1 | 0 | 1 | 2 |
| $f(x_i)$ | 4 | 1 | 0 | 1 | 4 |

So the trick here is to rewrite the data in vertical columns just like the following figure and do the math as shown. the first number in each column will be the value of the corresponding divided difference.


