# Newton's divided difference interpolation method

Interpolation is very useful when you have a bunch of data that you want to make sense out of them. It's useful in many fields specialy in astronomy, physics and many other sciences.<br />
Here I've written a program which takes **n** numbers (**$x_i$**) and their corresponding $f(x_i)$  and then, by using Newton's divided difference method gives you the best mathematical function that can fit the given data.

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

And the second divided difference would be:

$$ F\left[x_i,x_{i+1},x_{i+2}\right]\ =\ \frac{F\left[x_i,x_{i+1}\right]-F\left[x_{i+1},x_{i+2}\right]}{x_i-x_{i+2}} $$

And so on ...

* The function

Now by using the formula I just introduced, we can obtain a polynomial function $P(x)$ that fits the data we have. so by having the mathematical function you can accurately predict any desired $f(x)$ 

$$ P(x)\ =\ f(x_0)+(x-x_0)F\left[x_0,x_1\right]+\ (x-x_0)(x-x_1)F\left[x_0,x_1,x_2\right]+\cdots+(x-x_0)(x-x_1)\cdots(x-x_{n-1})F\left[x_0,x_1,x_2,\cdots x_n\right] $$


Woho! That's a lot of work, isn't it? But don't worry there is a more simple way to calculate the divided differences. Let me explain with a simple example. Supose we have the given set of data:

| i | 0 | 1 | 2 | 3 | 4 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| $x_i$ | -2 | -1 | 0 | 1 | 2 |
| $f(x_i)$ | 4 | 1 | 0 | 1 | 4 |

So the trick here is to rewrite the data in vertical columns just like the following figure and do the math as shown. the first number in each column will be the value of the corresponding divided difference.

![image](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/bdc3ff69-d33a-4f8e-8d79-3f31bfbb7427)

So $P(X)$ is :

$$ P(x)\ =\ 4+(x-(-2))(-3)+\ (x-(-2))(x-(-1))(1)+0+0 $$

$$ P(x)\ =\ 4\ -\ 3x\ -\ 6\ +\ x^2+x\ +2x\ +2 $$

$$ P(x)\ =x^2 $$

Tadaaaaa, Beautiful isn't it?

# algorithm
I came up with this idea that we can consider $f(x)$ column as a variable named **left_column** and the first divided difference as an empty list called **right_column**. Then we can calculate the operations showed in the previous figure for each column and append them to its **right_column** list. When we're done with all the calculations for the first divided difference, we append right_column[0] to a list defined to store the divided differences coefficients called **Coefficient**. Then we change the columns, (left_column = right_column and right_column = [] ) and we start to do the same for second divided difference and third and ...

![divided difference](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/d1e85c1c-1c3f-4b89-978a-8933e9578267)

# Interpolation function
When we are done with finding the coefficients (divided differences), this function will create the $P(x)$ and insert a given $x$ by the user and returns the value of the mathematical function at that particular $x$.

![interpolating function](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/d86b92f9-1a32-4d90-b442-bb52499136d9)
