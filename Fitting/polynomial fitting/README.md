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
