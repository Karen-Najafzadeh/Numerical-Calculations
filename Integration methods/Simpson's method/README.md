# Simpson's 1/3 rule

Suppose that you have a mathematical function called $f(x)$ and an interval (say from $a$ to $b$).
<br /> Let's divide the intevral into **n** parts (let's call them **iterations**) so that we can define a variable called $h$ where: $h\ =\ \frac{b-a}{n}$
<br /> the answer of $\int_{a}^{b}{f(x)dx}$ can be obtained by the following formula:

$$ \int_{a}^{b}{f(x)dx}\ =\ \frac{h}{3}((f(x_0)+4f(x_1)+f(x_2))\ +\ (f(x_2)+4f(x_3)+f(x_4))+\ \cdots\ +\ (f(x_{n-2})+4f(x_{n-1})+f(x_n)) $$

Where $x_i = a + ih$

If you pay close attention you'll see that for odd iterations ( i%2 != 0 ) we have a factor of four and for even iterations ( i%2 = 0 ) we have a factor of two.
<br /> So let's rewrite the expression like this:

$$ \int_{a}^{b}{f(x)dx}\ =\ \frac{h}{3}((f(x_0)+f(x_n))\ +\ 4(f(x_1)+f(x_3)+\cdots+f(x_{n-1}))+2(f(x_2)+f(x_4)+\ \cdots\ +\ f(x_{n-2}))) $$

And the rest I think is pretty much obvious. We declare a variable called sum and in every iteration we add $4f(x_i)$ to it if $x_i$ is odd or $2f(x_i)$ if $x_i$ is even.
And at the end we add $f(x_0)$ and $f(x_n)$ to the total sum. so that the final answer would be:

$$ \int_{a}^{b}{f(x)dx}\ =\ \frac{h}{3}(sum) $$

![simpson integration flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/81351290-a229-4b81-98d3-951b52d579cc)
