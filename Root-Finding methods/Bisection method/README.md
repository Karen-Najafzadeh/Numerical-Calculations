# Bisection Method
First of all you need to determine a range in **x axis** so that the program can check if there are any possible roots within the given range.This method requiers three variables to work:

**a:** The beginning of the range

**b:** The end of the range

**dx:** as the method has its own errors, we need a number close enough to **zero** to compare the output of the mathematical function to this **dx** variable so if the output was equal of less than this number, we concider that output's x as one of the possible roots of our function so smaller number = more accurate answer but also takes more time to calculate


# Flowchart

![bisection method flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/8f7a94d1-6609-4452-b4da-e4cab55e9e1b)


# How does the method works?

First of all, we obtain the middle of the range and assign it to the varriable **middle**.

Then we check if the middle point is the root or not, by checking if the absolute value of the function in the middle of the range is less than or equal to the number we defined as **dx** or not.

If so, that **middle** is the root of the function, but if not, we are going to cut out the part of the range that there is no potential of containing a root so we can make our range smaller and look for the root there.

so if our function is **f(x)**, and f(a)*f(middle) was a positive number, it means that both **a** and **middle** are positive or negative simultaneously so the function has no roots there. if not try again with a smaller range (remember this is not a very strong method).

thus we make the range smaller by doing this **a = middle**.

but otherwise, if f(a)*f(middle) was a negative number, it means that we have at least one root within that range. so we keep the range and cut off the other part.

by this method every time we get closer and closer to the root till we find it.

Again, I know it's not the best method to do this, it has errors, it might not be able to find the root if the function is too complicated, I did't invented this. I just wanted to program this method for fun :)
