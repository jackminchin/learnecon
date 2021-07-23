# Monetary Theory

## Evidence on the Impact of Monetary Policy

## Monetarism and the equation of exchange

In the past, some central banks attempted to stabilising by directly controlling the money supply. Monetarist still favour this approach. The 'equation of exchange' links the money supply $M$ to how often each unit of currency changes hands, known as the velocity of money $V$ to the total volume of spending $P$, and real output in the economy $Y$.

```{admonition} Taking log differences
$$M_t V_t = P_t Y_t$$

The natural logs of the variables are denoted with
lower case letter (note: when taking logs, the products of variables
turn to addition) 
$$m_t + v_t = p_t + y_t$$ 

Take time first differences.

$$\Delta m_t + \Delta v_t = \Delta p_t + \Delta y_t$$

The first difference of natural logs are approximately equal to
growth rates when they are small.

If the velocity is stable and doesn't depend on policy and $M$ can be
controlled, then controlling the growth rate of $M$ is a way to control
nominal spending $PY$. If $Y$ doesn't depend on monetary policy in the
long run, then 

$$\Delta m_t + \Delta v_t = \Delta p_t + \Delta y_t$$

$$\Delta p_t \approx a + \Delta m_t$$

```

If the velocity of money is fixed, or only slowly changes over time and the money supply can be controlled by the central bank and total output only depends on real factors, so can be taken as given, from:

$$\Delta m_t + \Delta v_t = \Delta p_t + \Delta y_t$$

$$\Delta P_t \approx a + \Delta m_t$$

### The Monetary Base

In principle, a central bank has control over the size of its balance sheet. The monetary base (MB) consists of the central bank reserves and the bank notes in circulation. The central bank could increase the monetary base by buying securities from banks and paying them with newly created reserve money. However, in practice, this is hard to achieve.

```{admonition} Chodorow-Reich et al. 

In November 2016, the Indian government declared 86% of existing currency in circulation illegal tender. Holders could replace them at banks with new notes, but they could no longer be used to facilitate transactions. 

This sharp reduction in the money supply while notes were exchanged for newly printed notes gave rise to a natural experiment to see whether changes monetary changes can affect the real economy. 

The authors found that this destruction of cash reduces GDP by about 2% in the quarter of demonetisation.

{cite:p}`626905`
```

### Some Correlations

1. Inflation and money growth is highly correlated across countries or time periods when inflation is highly variable.
2. Correlation is weak and unstable when inflation is low. 
3. There is some correlation with output at high frequency but not at low frequency. 
4. Evidence from India that money supply contraction can contract output.


Friedman and Schwarz {cite:p}`RePEc:nbr:nberbk:frie63-1` found that growth in the money supply lead to changes in economic activity, it was taken to suppose a causal interpretation - *post hoc ergo propter hoc*. 


### How do central banks control interest rates?

Commercial banks need the central bank reserves to:

-   Settle inter-bank transaction;

-   As a safe asset, and;

-   To meet reserve requirements.

To satisfy their own demand, banks can borrow reserves from each other - but this does not affect the total supply. The tighter the supply the
higher the interest rate, so the level of reservers determine the
interbank interest rate.

The central bank may increase reserves to rescue banks or to implement QE, in such a case it may lose control of the interbank interest rate. To remedy this, central banks not typically have standing deposit and lending facilities which place a corridor around the interbank rate.

Suppose the central bank wants to stabilise output (assume prices are
sticky for now). The output is determined by equilibrium in the goods
and money markets, both of which are hit by shocks. The central bank can observe the interest rate but not the shocks to the goods and money markets.

How, then should the Central Bank choose with instrument to use?

#### Poole (1970)

{cite:p}`10.2307/1883009` proposed the following simple model on optimal instrument choice?

The simple equations linking log output and log money demand and
interest rates can be written as: 

$$\tag{IS}
  y_t = - \alpha i_t + u_t$$ 
  
$$\tag{LM}
  m_t = y_T - ci_y v_t
  $$

Where $\alpha$ and $c$ are respective semi-elasticities of output and
money demand with respect to interest rates. $u_t$ and $v_t$ are the
respective shocks to output and the money demand.

The objective of the policy maker is to minimise the variance of output around its trend, which is normalised to zero. The central bank can
either set $i_t$ or $m_t$ before it knows $u_t$ or $v_t$.

Firstly, we can get an equation that links $y$ to $m$ and the shocks,
removing $i$. Taking $LM$ we can arrange to get $i$ on the LHS.

$$i_t = \frac{y_t - m_t + v_t} {c}$$ 

Now taking the $IS$ equation, we
can replace $i_t$ with the revised $LM$ equation.

$$y_t = - \alpha \left(  \frac{y_t - m_t + v_t} {c} \right)+ u_t$$

Collecting all terms of $y_t$ on the LHS we arrive at:

$$y_t + \frac{a}{c}y_t = (1 + \frac{a}{c})y_t = \frac{c + \alpha}{c}y_t = \alpha(\frac{m_t - v_t}{c}) + u_t$$

Dividing through both sides by $\frac{c + \alpha}{c}$ we obtain:

$$y_t = \frac{\alpha}{c + \alpha}(m_t - v_t) + \frac{c}{c+\alpha}u_t$$

Following the same logic to link $y$ to $i$ and remove $m$, we can just use $IS$. The variance of output is $E_[y^2] = \sigma^2_u$. We can now see which policy gives the lowest variance for output.

$$\begin{aligned}
    \frac{1}{(\alpha + c)^2}(a^2\sigma^2_v + c^2 + \sigma^2_u) &> \sigma^2_u \\
    (a^2\sigma^2_v + c^2\sigma^2_u) &> (a^2 + c^2 + 2ac)\sigma^2_u \\
    a^2\sigma^2_v &> (a^2 + 2ac)\sigma^2_u \\
    \sigma^2_v &> \left( 1 + \frac{2c}{a} \right)\sigma_u^2
  \end{aligned}$$

This can be taken to mean that when the volatility of financial markets is relatively high, when money demand is insensitive to interest rates, or when expenditure is very sensitive to interest rates, this is when
the interest rate should be used as the policy mechanism.

Central banks could traditionally control the money supply or the
interest rate. Before 2008, interest rates were the dominant tool - this can be rationalised as a response to volatile money demand relative to the real economy.

With the advent of payment on reserves and interest rate corridors,
central banks now control both interest rates and money supply.

Monetary Shocks
---------------

#### Fisher Equality

Links the nominal interest rate to the expected real interest rate and
expected inflation $$i \approx r^e + \pi^e$$

The mainstream view is that the central bank can influence the real
interest rate, but only in the short run. In the long run, the real
interest rate depends on forces beyond the central bank's control.

#### Taylor Principle

Central bank should raise interest rates at least as much as inflation to stabilise inflation.

The positive low-frequency correlation could come from the central
bank's response to low-frequency inflation variation.

### What is a shock?

-   Exogenous with respect to the other current and lagged variables in
    the model.

-   Uncorrelated to other exogenous shocks.

-   Represents either unanticipated movements in exogenous variables or
    new about this.

### A Simple VAR

Consider the simple economy where $y_t$ is output and $i_t$ represents the nominal interest rate. Both $y_t$ and $i_t$ are subject to exogenous shocks denoted by $\varepsilon$.

$$i_t = b_{iy} y_t + \epsilon_{it}$$

$$y_t = b_{yi} i_t + \epsilon_{yt}$$ 

This system of equations can be
written in matrix form as: 

$$Ax_t = \epsilon_t$$ 

where:

$$\epsilon_t = \begin{bmatrix}
\epsilon_{it} \\
\epsilon_{yt}
\end{bmatrix}, \;\;\; x_t =\begin{bmatrix}
  i_t \\
  y_t
\end{bmatrix}, \;\;\; A = \begin{bmatrix}
  1 & -b_{iy}  \\
  -b_{yi} & 1 
\end{bmatrix}$$

Then $x_t = A^{-1}\epsilon_t$. We observe the covariance matrix of
observables $E[x_tx't]$. This contains three parameters - two variances
and one covariance. The model, however, contains four parameters
$\{b_{iy}, b_{yi}, \sigma^2_\epsilon i, \sigma^2_\epsilon y\}$.

The general form of a VAR is $x_t = \phi x_{t-1} + B\epsilon_t$ which
can be written in extended matrix, or linear form. $\epsilon$ is a
vector of unobservable zero mean, white noise processes. Meaning they
are serially uncorrelated and independent of each other.

Now, forming a concrete example of the model, assume that

-   $x_{1t}$ and $x_{2t}$ are output growth $y_t$ and the policy rate
    $r_t$, demeaned.

-   $\epsilon_{1t}$ and $\epsilon_{2t}$ are a demand shock $\epsilon ^D$
    and a monetary policy shock $\epsilon^{mp}$.

-   B is known

we can formulate the model as:

$$\begin{bmatrix}
y_t \\
r_t
\end{bmatrix}  = \underbrace{\begin{bmatrix}
  \phi_{11} &  \phi_{12} \\
  \phi_{21} &  \phi_{22} \\
\end{bmatrix}}_{\text{dynamic matrix}} \begin{bmatrix}
y_{t-1} \\
r_{t-1}
\end{bmatrix} + \underbrace{\begin{bmatrix}
  b_{11} &  b_{12} \\
  b_{21} &  b_{22} \\
\end{bmatrix} }_{\text{impact matrix}}
 \begin{bmatrix}
\epsilon ^D \\
\epsilon ^{mp}
\end{bmatrix}$$

What is the effect of monetary policy shocks on output?

-   The coefficient $b_{12}$ captures the impact effect of a monetary
    policy shock on output growth.

-   The $\phi$ matrix allows us to trace the dynamic effect of the
    monetary policy shock over time.

Of course, in practise, the shocks are unobserved, how can we estimate
$B$?. Firstly, we can bundle the error terms into a single object such
that: 

$$u_t = B \epsilon_t \rightarrow \begin{bmatrix}
y_{1t} \\
u_{2t}
\end{bmatrix}\begin{bmatrix}
  b_{11} &  b_{12} \\
  b_{21} &  b_{22} \\
\end{bmatrix}\begin{bmatrix}
\epsilon ^D \\
\epsilon ^{mp}
\end{bmatrix} \rightarrow \begin{cases}
    u_{yt} = b_{11} \epsilon^D + b_{12}\epsilon^{mp}\\  
    u_{rt} = b_{21} \epsilon^D + b_{22}\epsilon^{mp}
 \end{cases}$$ 
 
 In which case the VAR becomes $x_t = \phi x_{t-1} + u_t$
which can estimate $\phi$ $u_t$ with OLS.

The reduced form innovation are a linear combination of the two
structural shocks. 

$$\begin{array}{l}
u_{y t}=b_{11} \varepsilon_{t}^{\text {Demand }}+b_{12} \varepsilon_{t}^{\text {Monpol }} \\
u_{r t}=b_{21} \varepsilon_{t}^{\text {Demand }}+b_{22} \varepsilon_{t}^{\text {Monpol }}
\end{array}$$

An increase in $u_{rt}$ could be due to either \[1\] a positive demand
shock that increases both output growth and the policy rate, or \[2\], a
monetary policy shock that decreases output growth and increases the
policy rate.

The identification problem consists in finding a mapping from the reduce
form VAR to its structural counterpart $u_t = B\epsilon_t$. To do that,
we can exploit the relationship between reduced form and structural
innovations to write

$$\Sigma_{u}=\mathbb{E}\left[u_{t} u_{t}'\right]=\mathbb{E}\left[B \varepsilon_{t}\left(B \varepsilon_{t}\right)'\right]=B \mathbb{E}\left(\varepsilon_{t} \varepsilon_{t}'\right) B'=B \Sigma_{\varepsilon} B'=B B'$$

### Solutions to the Identification Problem

There are an infinite set of $B$s which satisfy the constraint. In the
example previous, we have a system of 3 equations in 4 unknowns. We can
solve this by adding a fourth equation.

Economic theory can help to provide the missing equations. We can make
an assumption about the structure of the economy based on beliefs and
try to map this assumption into an equation that involves the VAR
parameters.

This additional assumption is known as a restriction.

#### Choleski Decomposition

This solution imposes zero restrictions on the impact matrix $B$. The
$b_{12}$ coefficient captures the contemporaneous effect of monetary
policy on output growth, which we set to zero by assumption.

$$\begin{bmatrix}
y_t \\
r_t
\end{bmatrix}  = \underbrace{\begin{bmatrix}
  \phi_{11} &  \phi_{12} \\
  \phi_{21} &  \phi_{22} \\
\end{bmatrix}}_{\text{dynamic matrix}} \begin{bmatrix}
y_{t-1} \\
r_{t-1}
\end{bmatrix} + \underbrace{\begin{bmatrix}
  b_{11} & 0 \\
  b_{21} &  b_{22} \\
\end{bmatrix} }_{\text{impact matrix}}
 \begin{bmatrix}
\epsilon ^D \\
\epsilon ^{mp}
\end{bmatrix}$$

This removes one of the structural parameters to estimate, with three
structural parameters and three restrictions.

#### External Instruments

This solution involves exploiting information from a variable that is
external to the VAR, but is correlated with a particular shock and
uncorrelated with other shocks.

Assume that we have some 'narrative' series of policy surprises, for
example, assume that such an instrument $z_t$ exists and satisfied the
following properties 

$$E[\epsilon^{D} z'_t]= c$$

$$E[\epsilon^{mp} z'_t]= 0$$ 

then we can identify one column (in this
example the second column) of the $B$ matrix.

$$\begin{bmatrix}
y_t \\
r_t
\end{bmatrix}  = \underbrace{\begin{bmatrix}
  \phi_{11} &  \phi_{12} \\
  \phi_{21} &  \phi_{22} \\
\end{bmatrix}}_{\text{dynamic matrix}} \begin{bmatrix}
y_{t-1} \\
r_{t-1}
\end{bmatrix} + \underbrace{\begin{bmatrix}
  - & b_{12} \\
  - &  b_{22} \\
\end{bmatrix} }_{\text{impact matrix}}
 \begin{bmatrix}
\epsilon ^D \\
\epsilon ^{mp}
\end{bmatrix}$$

The OLS estimator of $\beta$ in the first stage regression indentifies
$b_{2}$ up to a scaling factor.

$$u_{rt} = \beta z_t = \zeta_t$$

The procedure is then

-   Estimate the reduced form VAR to obtain reduced-form residuals $u$.

-   Regress $u_{yt}$ on $u_{rt}$ using $z_t$ as the instrument.

-   The coefficient we derive is an estimate of $\frac{b_{12}}{b_{22}}$.

-   Normalise $b_{22} =1$.

#### Romer and Romer (1989) 

In this paper {cite:p}`RePEc:nbr:nberch:10964`, the authors look at episodes of large monetary disturbances not caused by output fluctuations. It tests whether these disturbances have effects in the real economy. 

They find that a shift to anti-inflationary monetary policy led to a rise in the unemployment rate of two percentage points, on average.

#### Romer and Romer (2004)

In 2004 {cite:p}`10.1257/0002828042002651` added a further contribution to the literature. The paper develops a measure of U. S. monetary policy shocks for the period 1969–1996 that is relatively free of endogenous and anticipatory movements.

> Quantitative and narrative records are used to infer the Federal Reserve's intentions for the federal funds rate around FOMC meetings. This series is regressed on the Federal Reserve's internal forecasts to derive a measure free of systematic responses to information about future developments. Estimates using the new measure indicate that policy has large, relatively rapid, and statistically significant effects on both output and inflation. The effects are substantially stronger and quicker than those obtained using conventional indicators.

#### High-frequency identification

Looks at how markets move in a short (e.g. 30 minute) window around a
'policy event'. The idea is that all macro data are priced in before the
meeting, by deriving the instrumental variable from this window we know
that it is a) only correlated with the policy shock because the window
was too short for anything else to have happened.

### Policymakers' view of monetary policy shocks

-   Many policymakers will tall you there is no such thing as a policy
    shock.

-   The understandably resist the idea that policy is ever random or
    unrelated to the economy.

-   It's true that there is no exact empirical counterpart to the
    question of how to change the policy rate.

-   We never observe a counter-factual.

### Impulse Responses

-   Most studies find that a positive interest rate shock reduces output
    after 1-2 years, and inflation a bit later.

-   Recent samples find smaller anomalous effects.

-   Policy more stable / stabilising in recent past.

    -   Most policy rate movements are endogenous.

    -   Harder to identify shocks.

-   Large shocks in the past are a better guide

    -   End of the gold standard

    -   Volcker disinflation

-   Tension between internal and external validity.

## Barro and Gordon (1983)

This section explains the Barrow and Gordon model. The central bank has
a utility function that specifies that is increasing in output and
decreasing inflation. The CB attempts to maximise this utility function
by setting monetary policy. There is perfect information, so the private
sector can understand this when forming expectations of inflation.

### Central Bank's Objective Function

The central bank attempts to maximise the value of their objective
function that is: 

$$\label{eq:CBOBJ}
  U = \lambda(y-y_n) - \frac{1}{2}\pi^2$$ 

where $y$ is output, $y_n$ is
natural output, $\lambda$ is the weighting of output within the utility
function and $\pi$ is inflation. The central bank prefers higher output,
and the costs of inflation are quadratic, meaning the marginal costs of
inflation are increasing. Natural output, $y_n$ is a constant that the
central bank cannot affect.

### The Economy

The economy behaves subject to a supply function of the form:

$$\label{eq:SUPPLY}
  y = y_n + \alpha(\pi-\pi^e) + \varepsilon$$ 
  
in this supply function $\pi^e$ represents the inflation expectations of the private sector and
$\varepsilon$ is a supply shock that increases output without an
increase in inflation. Inflation only increases output when it exceeds
inflation, because if $\pi < \pi^e \rightarrow \alpha(\pi - \pi^e) < 0$.
It should also be noted that natural output is achieved when the
realisation of the supply shock is 0 and inflation is equal to
expectations.

### Influencing inflation

The central bank can choose inflation by setting the money growth,
subject to a velocity shock or a control error: 

$$\label{eq:INF}
  \pi = \Delta m + \nu$$ 
  
The order of the process is as follows:

1.  The private sector sets inflation expectations.

2.  The supply shock $\varepsilon$ is realised.

3.  The policy $\Delta m$ is chosen.

4.  The velocity shock $\nu$ is realised.

### Solution under discretion

The central bank chooses $\Delta m$ in order to maximise its utility
function $U$, given in ([\[eq:CBOBJ\]](#eq:CBOBJ){reference-type="ref"
reference="eq:CBOBJ"}). Substituting in output and inflation, and taking
expectations of the velocity shock, which has not yet happened, yields:

$$\begin{aligned}
    U &= \lambda(y-y_n) - \frac{1}{2}\pi^2 \\
    &= \lambda(y_n + \alpha(\pi-\pi^e) + \varepsilon - y_n) - \frac{1}{2}\pi^2 \\
    &= \lambda(\alpha(\pi-\pi^e) + \varepsilon) - \frac{1}{2}\pi^2 \\
    &=\lambda(\alpha(\Delta m + v-\pi^e) + \varepsilon) - \frac{1}{2}(\Delta m + v)^2 \\
    &=\lambda(\alpha(\Delta m + E[v]-\pi^e) + \varepsilon) - \frac{1}{2}(\Delta m + E[v])^2 \\
  \end{aligned}$$ 
  
  Then, finding the first order conditions with respect
to the policy tool $\Delta m$ yields: 

$$\begin{aligned}
        \frac{\partial U}{\partial \Delta m} = 0 = \lambda\alpha  - \Delta m \\
        \Delta m&= \lambda\alpha
    \end{aligned}$$

The policy choice of the central bank then does not depend on the shocks
or the expected inflation of the private sector. Substituting this back
into the definition of inflation
([\[eq:INF\]](#eq:INF){reference-type="ref" reference="eq:INF"}):

$$\pi = \lambda\alpha + \nu$$ 

The private sector, because of perfect
information understands this, consequently setting their expectations of
inflation equal to $\lambda\alpha$, the shock disappears because it is
i.i.d with mean zero: $$\pi^e = E[\pi] = \lambda\alpha$$

The supply function ([\[eq:SUPPLY\]](#eq:SUPPLY){reference-type="ref"
reference="eq:SUPPLY"}) can now be written: 

$$\begin{aligned}
      y &= y_n + \alpha(\lambda\alpha + v - \lambda\alpha) + \varepsilon \\ 
      &= y_n + \alpha v + \varepsilon \\ 
\end{aligned}$$

Showing that output is now completely independent of policy. In this
case, when the central bank sets their policy, this generates inflation
but does not generate more output.

The central banks loss can be written as: 

$$\begin{aligned}
      E[U] &= E\left[\lambda(y - y_n) - \frac{1}{2} \pi^2\right] \\
      &= E\left[\lambda(\alpha \nu + \varepsilon) - \frac{1}{2} (\lambda\alpha + \nu)^2\right] \\
      &= -\frac{1}{2} (\alpha^2 + \lambda^2 + \sigma^2_v)
\end{aligned}$$ 

This shows that the loss is increasing in the central
bank's relative preference for extra output $\lambda$, the sensitivity
of output to surprise inflation $\alpha$ and the variance of the
velocity shock. In equilibrium, the Central Bank cannot create surprise
inflation, however $\alpha$ and $\lambda$ express the desirability of
creating excess inflation.

### Solution under Commitment

In a rational expectations equilibrium, actual inflation must equal
expected inflation, so from the supply function, on average output must
be equal to the natural output. In this case, the best solution is to
set the money supply change to 0, $\Delta m =0$.

In this case, the central bank's utility function can be written:

$$\begin {aligned}
    U &= \lambda(y - y_n) - \frac{1}{2}\pi^2    \\
    &=0 - \frac{1}{2}(\Delta m + v)^2 \\
    & = - \frac{1}{2} (0^2 + v^2) \\ 
    & = -\frac{1}{2} \sigma_v^2
  \end {aligned}$$

# References
```{bibliography} ../../zreferences.bib
:filter: docname in docnames
```