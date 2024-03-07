# fitting-methods
A few methods of fitting data to a function including grid search, gradient search, and expansion

Source: Bevington Data Analysis for the Physical Sciences, 8.3

# Fit function

$$y(x) = a_1L(x;\mu_1\Gamma_1) + a_2L(x;\mu_2,\Gamma_2)$$

- At first we will be finding just a1 and a2, but eventually we will expand our fit function to find the parameters $\mu_1$, $\Gamma_1$, etc.
- For now, we will accept these initial values:


- $\mu_1 = 102.1$
- $\Gamma_1 = 30$
- $\mu_2 = 177.9$
- $\Gamma_2 = 20$


- We are also assuming uncertainties as follows:
- $\sigma_i = \sqrt{y_i}$

# Methods:
## 1. Grid search
1. Select starting values $a_j$ and step sizes $\Delta a_j$ for each parameter, and calculate $\chi ^2$ with these starting params.
2. Increment one parameter $a_j$ by $\Delta a_j$ and make sure that $\chi ^2$ decreases with the new value
3. Repeat step 2 until $\chi ^2$ is minimized (aka it stops decreasing and starts increasing)
4. Use the minimum value and the point on either side (3 datapoints) to fit a parabola. Then find the minimum of that parabola. The minimum of this parabola is our accepted value of $a_j$. 
5. Repeat for all the other parameters.
6. Continue until the total $\chi ^2$ value is minimized to what we perfer.