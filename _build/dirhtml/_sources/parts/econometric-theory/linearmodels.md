---
author: Somebody
---

# The Linear Regression Model

```{note}
This section is best read by someone with basic knowledge of linear algebra and calculus.
```

The linear regression model concerns itself with modelling a multivariate linear relationship between an endogenous (or dependent) variable which is denotes as $y_t$, and a number of exogenous (or explanatory) variables, denoted $x_{ti}$, observed across $t = 1, 2, ... , T$. In a model with $k$ exogenous variables, the liner regression model is specified:

$$ y_t = \beta_1 x_{t1} + \beta_2 x_{t2} + ... + \beta_{k} x_{tk} + u_t$$

Typically, econometricians add a constant term, setting $x_{t1} = 1$ for all $t$, such that the specification can be written:

$$ y_t = \beta_1 + \beta_2 x_{t2} + ... + \beta_{k} x_{tk} + u_t$$

$u_t$ is unobserved, or stochastic, error term. For the ordinary least squares estimator to work, it must satisfy the following three assumptions:

$$E(u_t) = 0 \;\; \forall \; t$$
This is to say that the expectation, or mean, of the errors should always be zero.

$$V(u_t) = \sigma^2 \;\; \forall \; t$$
This means that the variance should always equal $\sigma^2$.

$$C(u_t, u_s) = 0 \;\; \forall \; t$$
Finally, there should never be any covariance between any of the explanatory variables.

Additionally, there are two further assumptions that the explanatory (read: exogenous or independent) variables must satisfy:

1. The explanatory variables must be nonstochastic, this means that they must not be random.
2. They must be linearly independent of one another.

The multivariate linear regression model can be expressed in the language of linear algebra, that of matrices and vectors. In matrix form, the regression specification be written as:

$$ \left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{T}
\end{array}\right]=\left[\begin{array}{cccc}
1 & x_{12} & \ldots & x_{1 k} \\
1 & x_{22} & \ldots & x_{2 k} \\
\vdots & \vdots & \vdots & \vdots \\
1 & x_{T 2} & \ldots & x_{T k}
\end{array}\right]\left[\begin{array}{c}
\beta_{1} \\
\beta_{2} \\
\vdots \\
\beta_{k}
\end{array}\right]+\left[\begin{array}{c}
u_{1} \\
u_{2} \\
\vdots \\
u_{T}
\end{array}\right]$$

or, more simply, $y = X \beta + u$.

In this new language, we can state the assumptions slightly differently:

1. $E(u) = 0$
2. $V(u)=E\left[(u-E(u))(u-E(u))^{\prime}\right]=E\left(u u^{\prime}\right)=\sigma^{2} I_{T}$
3. $X$ is nonstochastic with full column rank ($k < T$)

From this matrix form, we can consider how to estimate the parameter $\beta$.

# Ordinary Least Squares Estimation

The method of OLS estimation chooses the values for the $\beta$ parameters in the model in order minimize the residuals sum of squares. That is the squared error term added for each time period.

$$ \max \sum_{t=1}^{T} \hat u_t^2 $$

In matrix form, this can be written as:

$$ \text{choose } \hat \beta \text{ to minimise } RSS = \hat u'\hat u$$
where $\hat u = y - X \hat \beta$$

```{note}
**What is $u'$?**

The apostrophe, or 'prime' symbol notes the transpose of the matrix that it appended to. This means that we flip the matrix's columns and rows such that:

$$\left[\begin{array}{ll}1 & 2 \\ 3 & 4 \\ 5 & 6\end{array}\right]^{\mathrm{T}}=\left[\begin{array}{lll}1 & 3 & 5 \\ 2 & 4 & 6\end{array}\right]$$

```

Now, 

$$\begin{aligned} R S S &=\hat{u}^{\prime} \hat{u}=(y-X \hat{\beta})^{\prime}(y-X \hat{\beta}) \\ &=\left(y^{\prime}-\hat{\beta}^{\prime} X^{\prime}\right)(y-X \hat{\beta}) \\ &=y^{\prime} y-y^{\prime} X \hat{\beta}-\hat{\beta}^{\prime} X^{\prime} y+\hat{\beta}^{\prime} X^{\prime} X \hat{\beta} \\ &=y^{\prime} y-2 y^{\prime} X \hat{\beta}+\hat{\beta}^{\prime} X^{\prime} X \hat{\beta} \end{aligned}$$

The last line follows because $\hat \beta' X' y$ is a scalar.

As mentioned, our aim is to minimise the residual sum of squares. The first order condition for this problem is:

$$
\frac{\partial R S S}{\partial \hat{\beta}}=0
$$

In order to achieve this, we must obtain a $k$ dimensional vector of partial derivatives. 

```{note}
Differentiation involving matrices proceeds using standard calculus applied to the
relevant elements in turn. In terms of arranging the results, a number of conventions
apply. If $y = f(x)$ with $y$ a scalar and $x$ an $n \times 1$ vector:

$$
\frac{\partial y}{\partial x}=n \times 1 \text { vector of palrtial derivatives with elements } \frac{\partial y}{\partial x_{i}}
$$

$$
\frac{\partial^{2} y}{\partial x \partial x^{\prime}}=n \times n \text { matrix of second order partial derivatives with elements } \frac{\partial^{2} y}{\partial x_{i} \partial x_{j}}
$$


If $ y = f(x)$ with $y$ an $m x1$ vector and $x$ an $n \times 1$ vector:

$$
\frac{\partial y}{\partial x^{\prime}}=m \times n \text { matrix of partial derivatives with elements } \frac{\partial y_{i}}{\partial x_{j}}
$$

These allow us to right the following results:

$$
\begin{array}{ll}
y=a^{\prime} x, & \frac{\partial y}{\partial x}=a \\
y=A x, & \frac{\partial y}{\partial x^{\prime}}=A \text { or } \frac{\partial y^{\prime}}{\partial x}=A \\
y=x^{\prime} A x, & \frac{\partial y}{\partial x}=2 A x, \quad \frac{\partial^{2} y}{\partial x \partial x^{\prime}}=2 A
\end{array}
$$
```

So, from the conventions above $
\frac{\partial A b}{\partial b}=A^{\prime} \quad ; \quad \frac{\partial b^{\prime} A b}{\partial b}=2 A b,
$ we can write:

$$
\frac{\partial R S S}{\partial \hat{\beta}}=-2 X^{\prime} y+2 X^{\prime} X \hat{\beta}
$$

Equating this to 0, as per the first order conditions, gives:

$$
X^{\prime} X \hat{\beta}=X^{\prime} y
$$

and, solving for $\hat \beta$ we can derive the OLS estimator:$$
\hat{\beta}=\left(X^{\prime} X\right)^{-1} X^{\prime} y
$$

Now, here's where some of the assumptions come in, $(X'X)^{-1}$ must exist given the assumptoin that $X$ has full column rank $k$.  Also, note that the second order conditions are satisfied: 

$$
\frac{\partial^{2} R S S}{\partial \hat{\beta} \partial \hat{\beta}^{\prime}}=2 X^{\prime} X>0 \text { (i.e. is a positive definite matrix) }
$$
