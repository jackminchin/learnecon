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

and, solving for $\hat \beta$ we can derive the OLS estimator:

$$
\hat{\beta}=\left(X^{\prime} X\right)^{-1} X^{\prime} y
$$

Now, here's where some of the assumptions come in, $(X'X)^{-1}$ must exist given the assumptoin that $X$ has full column rank $k$.  Also, note that the second order conditions are satisfied: 

$$
\frac{\partial^{2} R S S}{\partial \hat{\beta} \partial \hat{\beta}^{\prime}}=2 X^{\prime} X>0 \text { (i.e. is a positive definite matrix) }
$$

## Properties of the OLS ($\hat\beta$) estimator

There are a number of properties associated with the OLS estimator.
First, a useful expression relating $\hat\beta$ and $\beta$ can be
derived.

The fundamental point of econometrics is that *y* is random. We assume
that the only source of randomness in the model is the error term
$\epsilon \; or \; u$. Anything that we construct from our data must be
a random variable.

$$\beta  = \hat\beta + \underbrace{(X'X)^{-1}}_{\text{Constant}} X'u$$

This is found by:

$$\begin{aligned}
        \hat\beta &= (X'X)^{-1}X'y \\ 
        &=   (X'X)^{-1}X' (X\beta + u)  \\ 
        &=   (X'X)^{-1}X'X\beta + (X'X)^{-1}X'u \\
        &= \beta + \underbrace{(X'X)^{-1}}_{\text{Constant}} X'u 
    \end{aligned}$$

It might be useful to know that $(X'X)^{-1}(X'X) = I$, (i.e the identity
matrix). $(X'X)^{-1}(X'X) \beta = \beta$. The identity matrix times
$\beta$ is just $\beta$.

### Expectation of $\hat\beta$

The expectation of $\hat\beta$, which can be denoted as $E[\hat\beta]$, can be written from the above term :

$$ E[\hat\beta] =  \bigg [\beta+\left(X^{\prime} X\right)^{-1} X^{\prime} u \bigg]$$

Now, because $\beta$ is a constant, it can be bought out of the expectations operator which gives: 

$$  E[\hat\beta] = \beta+ E \bigg [\left(X^{\prime} X\right)^{-1} X^{\prime} u \bigg]$$

similarly, with $\left(X^{\prime} X\right)^{-1} X^{\prime}$ being constant, the expectation is itself, meaning we can bring these terms out of the expectations operator, leaving just the error term:

$$  E[\hat\beta] =\beta+ \left(X^{\prime} X\right)^{-1} X^{\prime} E [u]$$

From the classical assumptions, we know that the expectation of the error term is 0. Substituting this in, we can see that the expectation of $\hat\beta$ is always $\beta$, the outcome of $\hat\beta$ won't be
$\beta$, however the average outcome will equal beta.:

$$E[\hat\beta] = \beta$$

** This is what it means to say that $\hat\beta$ is an unbiased estimator of $\beta$ **


### Variance of $\hat\beta$

The variance of a vector $v$ is equal to $(E[v] - E[\bar v])(v - \bar v)'$ (that is, the expected value of vector minus the mean
of the vector times the vector minus the mean of the vector transpose).
Because in the case of the $\hat\beta$, the expected value is $\beta$
itself, the variance of $\hat\beta$ is simply:



$$
\begin{aligned}
V(\hat{\beta}) &=E\left[(\hat{\beta}-\beta)(\hat{\beta}-\beta)^{\prime}\right] \\
&=E\left[\left(X^{\prime} X\right)^{-1} X^{\prime} u\left(\left(X^{\prime} X\right)^{-1} X^{\prime} u\right)^{\prime}\right] \\
&=E\left[\left(X^{\prime} X\right)^{-1} X^{\prime} u u^{\prime} X\left(X^{\prime} X\right)^{-1}\right]=\left(X^{\prime} X\right)^{-1} X^{\prime} E\left[u u^{\prime}\right] X\left(X^{\prime} X\right)^{-1} \\
&=\left(X^{\prime} X\right)^{-1} X^{\prime}\left(\sigma^{2} I_{T}\right) X\left(X^{\prime} X\right)^{-1}=\sigma^{2}\left(X^{\prime} X\right)^{-1} X^{\prime} X\left(X^{\prime} X\right)^{-1} \\
&=\sigma^{2}\left(X^{\prime} X\right)^{-1}
\end{aligned}
$$

We have the random quantity in the middle, the error terms $uu'$,
everything to the left and right are constant quantities. In the final
equation, we see that we are multiplying by the identity matrix, which
just leaves the original matrix giving the variance to equal
$\sigma^2(X'X)^{-1}$.

However, we can see that in order to know the variance, we must estimate $\sigma^2$. 

### Estimating $\sigma^2$

We can estimate $\sigma^2$ based on the residual sum of squares $RSS = \hat u'\hat u$. Firstly, using the definition of the linear model in matrix form we can write:

$$\hat u = y - X\hat\beta$$

Rearranging yields: 

$$
\begin{aligned}
\hat{u} &=y-X \hat{\beta}=X \beta+u-X \hat{\beta} \\
&=X \beta+u-X\left(\beta+\left(X^{\prime} X\right)^{-1} X^{\prime} u\right) \\
&=u-X\left(X^{\prime} X\right)^{-1} X^{\prime} u \\
&=\left(I_{T}-X\left(X^{\prime} X\right)^{-1} X^{\prime}\right) u=M u
\end{aligned}
$$

$M$ is defined as $M = I_T - X(X'X)^{-1} X'$. We can show that this new matrix, $M$, is symmetric, we can also show that is satisfies $MM  = M$, making $M$ what is known as *idempotent*. This
means that the RSS ($\hat u ' \hat u$) can be written as

$$\begin{aligned}
    \hat u ' \hat u &= (Mu)'Mu = u'MMu = u'Mu \\
    &= Tr(u'Mu) = Tr(Muu')\end{aligned}$$

Because it is a scalar a 1 by 1 matrix, the trace of the matrix is the
same. We know that the trace of a product of two matrices is the same as
the trace of product of 2 matrices.

Next,

$$E[Tr(Muu')] = Tr(ME[uu']) = Tr(M\sigma^2I_T) = \sigma^2Tr(M)$$

and

$$Tr(M) = T - k$$

Therefore, $E(\hat u ' \hat u) = \sigma^2(T-k)$ and it follows that:

$$E( \frac{\hat u '\hat u} {T -k }) = \sigma^2$$

Such that an unbiased estimator of sigma squared is provided by:

$$\frac{\hat u '\hat u} {T -k } = \sigma^2$$

We can therefore construct an unbiased estimator of $V(\hat \beta)$
using:

$$\hat V( \hat \beta) = \hat\sigma^2(X'X)^{-1}$$

### Orthogonality Properties

Two orthogonality results also follow from OLS estimation:

$$\underbrace{X'}_{K \times T} \underbrace{\hat u}_{T \times 1} = X'Mu = 0$$

since

$$\begin{aligned}
    X'M &= X'\underbrace{(I_T - X(X'X)^{-1}X')}_{M} \\
    &= \underbrace{X'}_{X'I_T} - X'X (X'X)^{-1} X' \\
    &=  X' - {X'X} {(X'X)^{-1}} \; X' \\
    &= X' - X' = 0
\end{aligned}$$

i.e the regression are orthogonal to the residuals. given that the first
column of X is a constant, the orthogonality results $X'\hat u' = 0$
implies:

$$\sum_{t=1}^T \hat u_t = 0$$

so the residuals sum to zero when a constant term is present in the
regression.

Also,

$$\hat y' \hat u = (X \hat\beta)'\hat u = \hat\beta'X'Mu = 0$$

This is the inner product of the predicted values, where the predicted
values are derived from as being the difference of the actual values and
residuals.

#### Takeaway

The sum of the residuals in OLS is always 0, and the sum of the product
of predicted values times the residuals is also 0.

## Goodness-of-Fit

Assuming there is a constant in the regression model, we can measure how
well the sample regression fits the data, by assessing how much of the
variation of the dependent variable about its mean is explained by the
regression. The total variation of $y_t$ about its mean is defined as
the total sum of squares:

$$TSS = \sum_{t=1}^T (\hat y_t - \bar{\hat y_t})^2$$

This quantity can be decomposed into the part explained by the
regression, i.e the variation of the fitted values about their mean (the
explained sum of squares, ESS), and the part not explained by the
regression (i.e the variation of the residuals \[RSS\]).

$$\begin{aligned}
      TSS &=  \sum_{t=1}^T (\hat y_t - \bar{\hat{y_t}})^2 \\ 
      &= \sum_{t=1}^T [(\hat y_t - \bar{\hat{y_t}}) + \hat u_t]^2 \\
      &= \underbrace{\sum_{t=1}^T (\hat y_t - \bar{\hat{y_t}})}_{ESS} + \underbrace{\sum_{t=1}^T \hat u_t^2}_{RSS} + 2\sum_{t=1}^T (\hat y_t - \bar y) \hat u_t
\end{aligned}$$

This can be written simply below, because the final term in the above
equation sums to 0 because of the orthogonality results above.

$$TSS = ESS + RSS$$

All of these quantities are sums of squares, which cannot be negative.
The measure of how well a regression model does is constructed
considering the proportion of the variation in the dependant variable we
can explain to the total amount of variation.

$$\begin{aligned}
    R^2 &= \frac{ESS}{TSS} = 1- \frac{RSS}{TSS} \\
    &= \frac{ \hat y' \hat y - T \bar y ^2 } {y' y - T \bar y ^2} \\
    &= 1 - \frac{\hat u' \hat u} {y'y - T \bar y ^2}
\end{aligned}$$

If we add another explanatory variable variable to a model, then the
worst outcome that the new variable could add to the model is 0. In
other words, you can not reduce the quality of the model by adding
another explanatory variable. Adding a new variable, then, will always
increase $R^2$. To overcome this we use the adjusted $R^2$ measure,
$\bar R^2$, which incorporates a penalty for including additional
variables:

$$\bar R^2 = 1 - \left[\left(\frac{T - 1}{T - k}\right) (1 - R^2)\right]$$

This measure only increases if its contribution outweighs the penalty
for its inclusion. note that for $k > 1,\bar R^2 < R^2$, and $R^2$ can
be negative.

# The Gauss-Markov Theorem

This theorem shows that among the class of estimators that linear
functions of $y_t$ and are also unbiased estimators, the OLS estimator
$\hat\beta$ has the smallest variance. We say that $\hat \beta$ is BLUE
(Best Linear Unbiased Estimator).

Let $\tilde \beta = Cy$ be an arbitrary estimator that is linear in $y$
(where $\underbrace{C}_{K \times T \; matrix}$ is non-stochastic).

*In the case of OLS, C is defined as*

$$\hat \beta = [\underbrace{(X'X)^{-1} X}_{K \times K \;\bullet \; K \times T} ]y$$

In the first line we can take C outside of the Expected values function
because it is a constant, leaving $E(y)$ where $y$ is a linear model. We
substitute this model in to get $CE(X\beta + u)$. WE can then take the
constant $X$ out, leaving $CE(u)$. From the fundamental assumptions of
the linear regression model $E(u)$ is 0, leaving simply $CX\beta$, then:

$$\begin{aligned}
    E(\tilde \beta) &= E(Cy) = CE(y) = CE(X \beta + u) \\
    &= CX\beta + CE(u) \\
    &= CX\beta      
  \end{aligned}$$

Therefore, we require the restriction $CX = I$ to hold in order that
$\hat\beta$ is an unbiased estimator.

$$\begin{aligned}
    \tilde \beta &= Cy = C(X\beta + u)\\ &= CX \beta + Cu \\& = \beta + Cu  
\end{aligned}$$

Now, because $\tilde\beta$ is unbiased, then:

$$\begin{aligned}
      V(\tilde\beta) &= E[(\tilde\beta - \beta) (\tilde\beta - \beta)'] \\&= E[Cu(Cu)'] = E[Cuu'C'] \\ &= C\underbrace{E[uu']}_{\sigma^2 I_T}C' \\ &= \sigma^2CC'
\end{aligned}$$

The idea is to compare $\sigma^2CC'$ with $\sigma^2(X'X)^{-1}$.

First add a zero to the simplest of all possible equations

$$C = C + 0$$

We make this zero by inserting in two like terms that cancel each other
out, in this case $-(X'X)^{-1}X' + (X'X)^{-1}X'$ to give:

$$\begin{aligned}
          C &= C -(X'X)^{-1}X' + (X'X)^{-1}X' \\
          &= A + (X'X)^{-1}X',
    \end{aligned}$$

where $A = c - (X'X)^{-1}X'$, and notice that 

$$\begin{aligned}
            AX &= CX - (X'X)^{-1}X'X \\
            &= CX - \underbrace{{(X'X)^{-1}}{X'X}}_{I_K} \\
            &= \underbrace{CX}_{I_K} - I\\
            &= I - I = 0
        \end{aligned}$$

Because we are only considering estimators which are unbiased,
$\tilde \beta$ will only be an unbiased estimator if $CX$ is also equal
to the identity matrix $I_K$.

If $AX = 0$, then $(AX)' = 0$ so $AX = (AX)'$, then,

$$\begin{aligned}
        V(\tilde\beta) = \sigma^2CC' &= \sigma^2(A + (X'X)^{-1}X')(A + (X'X)^{-1}X')' \\
        &= \sigma^2(A + (X'X)^{-1}X')(A '+ X(X'X)^{-1}X')\\
        &= \sigma^2(AA' + (X'X)^{-1}X'A' + AX(X'X)^{-1} + (X'X)^{-1}X'X(X'X)^{-1}) \\
        &= \sigma^2(AA' + {(X'X)^{-1}}\underbrace{X'A'}_0 + \underbrace{AX}_{0}{(X'X)^{-1}} + (X'X)^{-1} \underbrace{{X'X}{(X'X)^{-1}}}_{I_K}) \\
        &= \sigma^2(AA') + \sigma(X'X)^{-1} 
    \end{aligned}$$

So $V(\tilde\beta)$ exceeds $V(\hat\beta)$ by a positive definite
matrix. (Note that $\sigma^2AA' = 0$ if an only if A = 0 in which case
$\tilde\beta = \hat\beta$.

The intuition for this is that, if $A = 0$ then
$C = 0  + (X'X)^{-1}X')$, so $\tilde\beta = \hat\beta$.


Maximum Likelihood Estimation
=============================

MLE is an alternative method for estimating the multivariate linear
regression model. It is another way to estimate the unknown parameters
of a linear regression model. MLE can be quite complex.

The idea is that the process attempts to match the given observations to
some probability function. MLE chooses the estimator to be that value
which is most likely to have given rise to the observed sample.

More rigorously if $y_1, y_2, ..., y_T$ represents a random sample of
$T$ observations on a random variable $Y$ with PDF $f(u;\theta)$ where
$\theta$ represents a vector of unknown population parameters. Then, the
joint density, or likelihood function, of the $y_t$, since they are
independent is:

$$L(y_1, y_2, ..., y_T; \theta) = f(y_1; \theta)f(y_2;\theta) ...f(y_T;\theta) = \prod_{t=1}^T f(y_t; \theta)$$

and the MLE chooses an estimator $\hat\theta$ such that

$$\hat\theta = \arg_\theta \max L(y_1, y_2, ... , y_T; \theta)$$

To make MLE operational, we must specify a functional form for $f(.)$.

In the context of multivariate linear regression with normal errors, we
have:

$$y = X\beta + u, \;\;\;\; u \sim  N(0, \sigma^2I_T)$$
$$y \sim  N(X\beta, \sigma^2I_T)$$

i.e we add the assumption that the errors are normally distributed.

Using multivariate normal distribution results we can then write:

$$L(y; \beta, \sigma^2) = (2\pi\sigma^2)^{-T/2} \exp\{- \frac{1}{2\sigma^2}(y - X\beta)'(y - X\beta)) \}$$

This can be found in the part 0 notes on statistics. Normally, you would
just begin the normal maximisation process and solve for FOCs set to 0,
however, this is difficult because the function contains an exponent. If
we take the log (which is a monotone function \[if the target function
is increasing the log will increase and vice versa\]).

Maximising the likelihood L with respect to $\beta$, $\sigma^2$ yields
the same estimates as maximising the log-likelihood:

$$\ln L = - \frac{T} {2} \ln(2\pi) - \frac{T} {2} \ln(\sigma^2) - \frac{1}{2\sigma^2}(y - X\beta)'(y-X\beta)$$

Maximising $\ln L$ gives the first order conditions:

$$\begin{aligned}
  &\frac{\partial \ln L} {\partial \beta } = \frac{1}{\sigma^2}(X'y - X'X\beta) =0 \\
  &\frac{\partial \ln L} {\partial \sigma^2} = - \frac{T} {2\sigma^2} + \frac{1}{2\sigma^4}(y - X\beta)'(y-X\beta) = 0
 \end{aligned}$$

Solving gives the MLEs:

$$\tilde\beta = (X'X)^{-1}X'y$$

$$\tilde\sigma^2 = \frac{\tilde u' \tilde u}{T},$$

where $\tilde u = y -X\tilde\beta$. Note that the MLE of $\beta$ is
identical to the OLS estimate of $\beta$, and the MLE of $\sigma^2$ is
biased in finite samples.

$$\tilde\beta = \hat\beta$$
$$\tilde\sigma^2 = \left( \frac{T - k}{T} \right) \hat\sigma^2$$
