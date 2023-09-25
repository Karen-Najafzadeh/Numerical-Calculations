# Polynomial Fitting

This method is pretty much like [least square method](https://github.com/Karen-Najafzadeh/Numerical-Calculations/tree/main/Fitting/Least%20square%20method) but The difference is that
with this method you can fit higher order expressions than just linear expressions.

# Mathematics
Just as I explained in the other method, we have a series of $x_i$ and thier corresponding $y_i$ but the difference here is that instead of trying to find a function like $f(x) = ax+b$ to fit the data,
we are looking for some function like this:

$$ f(x) = a_n x^n + a_{n-1}x^{n-1} + ... + a_1 x + a_0 $$

Where n<m and m is the number of the total pair of data we have

Just like before, in order to find thos $a_n$ coefficients we have to minimize the following expression:

$$ S =\ \sum_{i=1}^{m}{(y_i-f(x_i))}^2 = \ \sum_{i=1}^{m}{(y_i-(a_n x_{i}^n + a_{n-1}x_{i}^{n-1} + ... + a_1 x_{i} + a_0))}^2 $$

in order to do so, this expression's partial derivative with respect to each $a_n$ should be zero.

$$ \frac{\partial S}{\partial a_n}\ =\ 0\ ,\ \ \frac{\partial S}{\partial a_{n-1}}\ =\ 0\ ,\ \ \frac{\partial S}{\partial a_{n-2}}\ =\ 0\ ,\ \ \ \ \cdots\ ,\ \ \frac{\partial S}{\partial a_0}\ =\ 0 $$

Well, solving these equations depends on the varriable $n$. Actually $n$ is the degree of the function you want to fit the data, so for example if you set $n=2$, your function will look loke this : $f(x) = a_2 x^2 + a_1 x + a_0$.<br />
But in general by solving them we'll get this:

$$ \sum_{i=1}^{m}{x_i^ny_i}=\ \sum_{i=1}^{m}{x_i^na_0}+\sum_{i=1}^{m}{x_i^{n+1}a_1}+\cdots+\sum_{i=1}^{m}{x_i^{2n}a_n} $$

$$ \sum_{i=1}^{m}{x_i^{n-1}y_i}=\ \sum_{i=1}^{m}{x_i^{n-1}a_0}+\sum_{i=1}^{m}{x_i^na_1}+\cdots+\sum_{i=1}^{m}{x_i^{2n-1}a_n} $$

$$ \vdots $$

$$ \sum_{i=1}^{m}{x_i^0y_i}=\ \sum_{i=1}^{m}{x_i^0a_0}+\sum_{i=1}^{m}{x_i^1a_1}+\cdots+\sum_{i=1}^{m}{x_i^na_n} $$

Well, I think solving this coulb be used as a punishment for serious crimes 😂. So what we have here is $n$ unknown variables wrapped inside $n+1$ equations. so it's possible to solve and obtain the unknowns which I'm going to explain next.

# algorithm 
Let's make the work easier by taking $n=2$. And let's try writing the equations in a matrix formation. We name the left side of the above equations (I mean these ones $\sum{x_i^ny_i}$ ) as $r_{i,j}$ (or whatever🤷).
And about the right side, as you can see $a_n$ coefficients are calcutable, so if we call them $x_{i,j}$ we can write all of those equations in a matrix form like this:

$$ r_{11} = x_{11} a_0 + x_{12} a_1 + x_{13} a_2  $$

$$ r_{21} = x_{21} a_0 + x_{22} a_1 + x_{23} a_2  $$

$$ r_{31} = x_{31} a_0 + x_{32} a_1 + x_{33} a_2  $$

Now Let's make a loop (for n in range(degree+1)) (from now on we call n, degree), and inside it we do two things Simultaneously. First, on another loop inside it, we make a nested loop (for i in range(m)) (where m is the total number of data pair we have) so we can calculate $r_{i,j}$.
<br /> On the same level of the m loop, still inside the n loop we make another loop to calculate $x_{i,j}$

After doing all that, we are left with two lists, first the one called **left_side** which contains [ $r_{11}$ , $r_{21}$ , $r_{31}$] and another list called **right_side** which contains the calculated right side of above equations. Now Let's cast those lists to Numpy arrays to make our work easier and faster. 
<br />So we define R a numpy array as:

$$ R\ = \begin{bmatrix}r_{1,1}\\
r_{2,1}\\
r_{3,1}\end{bmatrix} $$

And we create another np array (called **B**) to store the coefficients of $a_n$ in the list **right_side** 

$$ B\ = \begin{bmatrix}x_{1,1}&x_{1,2}&x_{1,3}\\
x_{2,1}&x_{2,2}&x_{2,3}\\
x_{3,1}&x_{3,2}&x_{3,3}
\end{bmatrix} $$

And if:

$$ A\ = \begin{bmatrix}a_{0}\\
a_{1}\\
r_{2}\end{bmatrix} $$

Then 

$$R = B.A$$

As the goal is to find $A$ so:

$$A\ =\ B^{-1}R$$

Where $B^{-1}$ is the inverse matrix of $B$. It's Done, we have $a_0$ $a_1$ and $a_2$. Now it's time to form up the actual mathematical function $f(x) = a_n x^n + a_{n-1}x^{n-1} + ... + a_1 x + a_0$ and we are done!

![polynomial fitting flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/d0c37ab8-940f-45e2-8740-310e3fdee066)
