# Extrapolation

In some cases we have a set of data ( $x$ and $f(x)$ ) and we want to see that within a short range, outside of the given interval how would data continue to act.
This method of extrapolating can be beneficial in such cases, but remember this method of extrapolating is not necessarily accurate to predict the behaviour of the data, specially when trying to work with far numbers from the original data it's just a lucky guess.

So suppose we have some data between x<m, and x>n  where n<m there are two scenarios:
* 1 if the $x$ we want to calculate its corresponding $f(x)$ is greater than **m**:

$$ y\ =\ f(x_{k-1})+(x-x_{k-1})F[x_{k-1},x_k] $$

Where $x_k$ is the greatest x and $x_{k-1}$ is the one right before it.<br />
Also $F[x_{k-1},x_k]$ is newton's first divided difference.I've explained about it in [Newton's divided differences method for interpolation](https://github.com/Karen-Najafzadeh/Numerical-Calculations/tree/main/Newton's%20divided%20differences%20method%20for%20interpolation).

* 2 if the $x$ we want to calculate its corresponding $f(x)$ is less than **n**:
  
  Here the formula is the same but $x_k$ is the least x and $x_{k-1}$ is the one right after it

We've got all we need, just take a $x$ to calculate $f(x)$.

![extrapolation flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/7a362f98-f293-4729-8716-5b5d15a59344)
