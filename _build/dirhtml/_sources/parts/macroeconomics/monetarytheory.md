# Monetary Theory

## Evidence on the Impact of Monetary Policy

Coming soon...

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
