# 2 Point Gauss Legendre Integration Rule

Well this topic a little advanced and complicated so I just ignore the mathematics and dive into the code.
<br /> Lets be quick about it, there are dozens of very good articles about this topic so I suppose you're ok with that.
<br />The only thing you have to know to understand this code is just if you have a mathematical function $f(x)$ and want to calculate $\int_{a}^{b}{f(x)}$ you can simpely use this formula

$$\int_{a}^{b}{f(x)}=\ \frac{b-a}{2}\left(f\left(\frac{1}{2}\left(\frac{(a-b)\sqrt3}{3}+(a+b)\right)\right)+f\left(\frac{1}{2}\left(\frac{(b-a)\sqrt3}{3}+(a+b)\right)\right)\right)$$

![Gaussian method flowchart](https://github.com/Karen-Najafzadeh/Numerical-Calculations/assets/106056574/a9683cb7-5fdb-419d-badc-9e5c6b0dd20c)

check the code, get your answer and compare with an online integral calculator and see the accuracy
