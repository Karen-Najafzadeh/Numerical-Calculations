# Newton's root finding method

This method uses first order derivation of the given mathematical function $f(x)$ to obtain one of the possible roots of the function. this method unlike the other two methods that i've discussed about, there is no requirement of any range to find the root.
 Instead we have to take a guess as the initial x (let's call it $x_i$) and the program will do the rest.

 # Libraries used

 Because of the algoritm, we need to work with the derivative equation of $f(x)$ and we are not able to use numerical methods directly (at least I couldn't figure out how).
 <br />So I've used a library called [sympy](https://www.sympy.org/en/index.html) to calculate the derivative equation I need.

 # Defenitions

 First of all we are given a function $f(x)$ that we need to calculate the first order derivative of it. to do so we need to install and import the library
  <br /> go ahead and execute it in your terminal:
 ```bash
  pip install sympy
```  
 then we import it in the program 
 ```bash
  import sympy as sp
```  
 Next we need to act with **x** like a mathematical symbol, not a usual python variable.
  ```bash
  x = sp.symbols("x")
```
So then we can calculate the derivative of the $f(x)$ with respect to $x$
  ```bash
  m = sp.diff(f(x),x)
```

Now all that's left is to take two inputs: <br />
* precision: this must be a small float. smaller number = more accurate answer but also longer time to calculate. As the method is not that accurate, and as we are calculating numerically not in an exact mathematically way,
  we need to define a number close enough to zero, so that if $f(x)$ was equal or less than that number, we take that $x$ as one of the possible roots
* $x_i$: As the method requires, we also need a first guess to do the calculations

# How does the method work
Well first of all we take $x_i$ as the initial x and draw the Tangent line of $f(x)$ in that position

The linear equation of a straight line can be obtained by the following furmula:
$$f(x)-f(x_1)=m(x-x_1)$$
where $x$ and $x_1$ are any valid number on the x axis, and m is the derivative equation of $f(x)$ in $x = x_i$ so it's a function too and we show it as $m(x)$.

Thus the equation of Tangent line of $f(x)$ in $x = x_i$ is:
$$f(x)-f(x_i)=m(x_i)(x-x_i)$$

Now the next step is to find in what x this function crosses the $y=0$ line, which means $f(x)=0$ so :
$$-f(x_i)=m(x_i)(x-x_i)$$
$$-\frac{f(x_i)}{m(x_i)}=x-x_i$$
$$x = x_i-\frac{f(x_i)}{m(x_i)}$$

Now let's call this $x$, $x_{new}$, the only thing left is to check if the value of $f(x_{new})$ is considerably close to zero to declare it as one of the possible roots of $f(x)$.<br />
If so, then we have the root. If not, $x_{new}$ is at least closer to the root than $x_i$. So we take $x_{new}$ as the next guess and try again and again until we find the root.<br />
Just like as the flowchart shows:

![newton's method flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/fde953ae-7da2-4eca-8f9a-1e6cf0f2c8a9)

