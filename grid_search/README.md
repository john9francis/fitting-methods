# Overview

Here, I will be testing out the grid search method. The data for this problem was found in the following source: Bevington Data Analysis for the Physical Sciences, problem 8.3.

# Development environment

In this project I used python with the matplotlib, numpy, and sympy libraries. I was also on windows 11. 

# How to run:
```
python -m venv venv
.\venv\scripts\activate
pip install -r requirements.txt
```

# Fit function

$$y(x) = a_1L(x;\mu_1\Gamma_1) + a_2L(x;\mu_2,\Gamma_2)$$

- The goal of this method is to find more accurate values for our parameters, ultimately reducing the chi-squared value.
- Here are our initial guesses for each parameter:

- $a_1$ = 1826
- $a_2$ = 2812
- $\mu_1 = 102.1$
- $\Gamma_1 = 30$
- $\mu_2 = 177.9$
- $\Gamma_2 = 20$


- We are also assuming uncertainties as follows:
- $\sigma_i = \sqrt{y_i}$

# Methods:
## 1. Grid search (From bevington pg. 151)
1. Select starting values $a_j$ and step sizes $\Delta a_j$ for each parameter, and calculate $\chi ^2$ with these starting params.
2. Increment one parameter $a_j$ by $\Delta a_j$ and make sure that $\chi ^2$ decreases with the new value
3. Repeat step 2 until $\chi ^2$ is minimized (aka it stops decreasing and starts increasing)
4. Use the minimum value and the point on either side (3 datapoints) to fit a parabola. Then find the minimum of that parabola. The minimum of this parabola is our accepted value of $a_j$. 
5. Repeat for all the other parameters.
6. Continue until the total $\chi ^2$ value is minimized to what we perfer.