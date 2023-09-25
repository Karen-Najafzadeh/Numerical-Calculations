# linear fitting

Suppose that you have a set of data ( some $x_i$ and their corresponding $y_i$ )that is acting like a linear function like $f(x) = ax+b$. By using **K square method** or also called **Least square method**, you can find that $f(x)$ and use it to predict how your data will behave at any position.

# Mathematics

To find $f(x)= ax+b$ we have to minimize the following expression:

$$ s\ =\ \sum_{i=1}^{m}{(y_i-f(x_i))}^2=\sum_{i=1}^{m}{(y_i-\ (ax_i+b))}^2\  $$

Where m is the total number of data pairs we have

To minimize $s$ we have to do these simple steps:

$$ \frac{\partial s}{\partial b}=\sum_{i=1}^{m}{2{(y_i-(ax_i+b))}^2(-1)}=0 $$

and 

$$ \frac{\partial s}{\partial a}=\sum_{i=1}^{m}{2{(y_i-(ax_i+b))}^2(-x_i)}=0 $$

By solving the equations we obtain $a$ and $b$:

$$ b\ =\ \frac{\sum y_i\sum x_i^2-\sum x_i\sum{x_iy_i}}{m\sum x_i^2-{(\sum x_i)}^2} $$

$$ a\ =\ \frac{\sum{x_iy_i}-\sum x_i\sum y_i}{m\sum x_i^2-{(\sum x_i)}^2} $$

where in all summation operations i is from 1 to m

By having $a$ and $b$ we have no problem calculating $f(x)$

# Errors
As we are talking all about predictions, errors in the result are inevitable. But these errors (called $K^2$) are too predictable by the equation below:

$$ K^2=\sum_{i=1}^{m}{(y_i\ -\ ax_i+b)}^2\  $$

# Code and Libraries used
I think the algorithm is pretty straightforward as I explained in the mathematics section, we just need to calculate those summations and the rest is simple, as the flowchart shows.<br />

![least square fitting method flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/e81cbf76-c935-45b1-9c0d-fd070933c5c9)

At the end of the code I also tried to plot the function we obtained so i used ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) to do so 
