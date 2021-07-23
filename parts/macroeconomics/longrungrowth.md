# Long Run Growth Theories

## Introduction

There is much interest in the drivers and the determinants of long-run economic development. Theories of proposed, which are simplifications of the real world, and to validate these theories, economists create measurements that relate models to the real world.

To make measurements, one requires units of measurement that are stable over time. For economics, money seems like a sensible choice for this unit, facilitating aggregation and allows for compatibility. Unfortunately, money is not a stable unit of account over time. This is due to __inflation__ and the __different currencies__ that countries use.

### Introducing GDP

GDP measures the total goods and services produced in country over a particular time period, usually a year. Intermediate production is excluded, to avoid double counting. It measures the welfare of the average person in this country, derived from consumption of goods an services plus future consumption utility current investment goods will
eventually generate in the future - it is important to remember that it omits everything else. 

The fundamental accounting identity which governs GDP can be written:

$$ Y_t = C_t + I_t + G_t + \underbrace{(X_t - M_t)}_{\text{Net Exports}}$$

where $Y_t$ is GDP, $C_t$ is private consumption, this includes durable and non-durable goods and services, $I_t$ is private investment which includes structures, machinery & equipment, and software which is bought or produced by firms. $G_t$ is government expenditures and $(X_t - M_t)$ are net exports, that is, exports ($X_t$) minus imports ($M_t$).

### Economic Growth

Economic growth is the increase in real GDP, however we measure GDP in nominal terms, which includes inflation. In order to calculate real GDP, a price index - or deflator - is used for each item. The growth rate for an item can be written:

$$ \frac{\Delta x}{x} = \frac{\Delta X}{X} - \frac{\Delta p}{p} $$
where $\frac{\Delta x}{x}$ is the real growth rate, $\frac{\Delta X}{X}$ is nominal growth and \frac{\Delta p}{p} is the item's inflation.

The growth of GDP is an average of these growth rates, weighted by their relative shares in GDP. In practice, the process involves measuring chained quantity indexes {cite:p}`ONSQMI`.


### The Kaldor Facts

In 1957, Nicholas Kaldor summarized the main properties of long run growth {cite:p}`Kaldor1961`:

1. GDP grows at a roughly constant rate.

2. The capital to GDP rate is roughly constant.

3. Capital and labour shares are roughly constant across time.

4. The rate of return on investment is roughly constant.

5. The real wages grows at a roughly constant rate

For any theory of long run economic growth to be plausible, they must adhere to these stylized facts.

```{warning} 
Since Kaldor's work in 1957, some of the Kaldor facts have been shown to be inaccurate. It is important to remember when learning these models that they are just models, and real world dynamics and processes are much more complicated than the models suggest. 
```


## Neoclassical Growth Model

### Introduction

### Description of the economy



In this model, time is denoted by $t$ and is continuous. Population, which is denoted by $L_t$ is assumed to grow at rate $n > 0$, such that:

$$ L_t = L_0 e^{nt}$$

we require that initial population $L_0 >0$, which in the authors opinion is a reasonable one.

At each period, each individual offers one unit of labour inelastically. The total labour supply can be given by $L_t$.

#### Production Technology


The is a continuum of firms of measure one that combine capital and labour to produce a single, homogenous and undifferentiated final good. These final goods firms operate in a perfectly competitive market.

The representative firm produces this good subject to a neoclassical technology: 

$$Y_t =(K_t, A_tL_t)$$

This technology combines capital $K_t$ and labour $L_t$ to produce output, which is denoted $Y_t$. $A_t$ is the current state of technology, it is a labour augmenting technology which is assumed to directly augment the productivity of labour in the production process.

The production function $F(\cdot)$ is assumed to be homogenous in the first degree, such that:

$$ F(\gamma K, \gamma L) = \gamma F(K,L)$$

where $\gamma$ is a positive, real number. This property suggests that the production technology possess 'constant returns to scale' (CRS). Constant returns to scale suggests that an change in both factors of production of the same scale, $\gamma$ raises total output at the rate $\gamma$.

We can express output in the measurement of efficicency units. In order to do this, divide by $A_tL_t$, yielding:

$$ y_t = F(\frac{K_t}{A_tL_t}, 1) = f(k_t)$$

where $y_t = \frac{Y_t}{A_tL_t}$ and $k_t = \frac{K_t}{A_tL_t}$.

The state of technology follows the process:

$$ A_t = A_0 e^{\gamma t}$$

where $\gamma > 0$ is the rate of technological progress and, the initial level of technology $A_0 > 0$.

Production, or total output, is assumed to be fully consumed in either consumption or investment, no output is ever wasted:

$$ Y_t = C_t + I_t $$

The law of motion for capital is governed by a differential equation:

$$\dot K_t = I_t + \delta K_t$$

where $\delta > 0$ is the level of capital depreciation and the initial level of capital is greater than zero, $K_0 > 0$.

We can now develop the feasibility condition for capital, by combining the production function, resource constraint and law of motion for capital and converting to efficiency units, yielding:

$$ \dot k_t = f(k_t) - c_t - (\delta + n + \gamma) k_t $$

$k_t$ is the capital labour ratio measured in efficiency units. Over time, capital depreciates at rate $\delta$, requiring that $\delta k$ units of output must be invested to maintain the level of capital. Additionally, with population growing at rate $n$, in order to keep capital per capita constant $nk$ units of output must be invested, analogously, since $k_t$ is measured in efficiency units, $\gamma k$ units of output must be invested in order to keep capital constant with the growth of technology.

Now, let us give the technology a function form. For this, we will use the most common of the Neoclassical technologies, the Cobb-Douglass production function:

$$ F(K_t, A_tL_t) = K^\alpha_t (A_tL_t)^{1-\alpha} $$

where $1 > \alpha > 0$. In efficiency units, this can be written:

$$ f(k_t) = k_t^\alpha $$

#### Household Preferences

In this model, households belong to an infinitely lived dynasty. The economy is populated by a continuum of households of measure one. The size of the representative household is $L_t$. 

The preferences of the household are given by the utility function:

$$ 
U(C_t, L_t) = L_0 \int_0^\infty u(\hat c_t) e^{(\rho - n)t} \; dt
$$

where $\hat c_t = \frac{C_t}{L_t}$, or consumption per capita. The utility of each member is measured by the instantaneous utility function $u(\hat c_t)$, it is multiplied by $L_t$ and discounted by the discount factor $\rho > 0$. This parameter, $\rho$, is the subjective discount rate that households attach to time. The larger the value, the less they value future consumption, implying that they prefer to consumer more today, that is, become more impatient.

To give the utility function $u(c)$ a functional form, we assume that it is exhibits constant intertemporal elasticity of substitution:

$$
    u(c) = \frac{c^{1-\frac{1}{\sigma}}}{1-\frac{1}{\sigma}}
$$
where the parameter $\sigma > 0$ is the intertemporal elasticity of substitution.

#### Markets

Firms own capital and they employ labour a the wage rate $w_t$. They finance capital by borrowing from households at an interest rate given by $r_t$.

Markets are perfectly competitive. This means that firms and households have no market power, and as such are price takers for price of goods and the wage rate. Prices adjust such that all markets clear. The price is normalised to 1 in every period.


### Equilibrium

In this section, we will solve the model in order to find the equilibrium. The representative firm maximises profits subject to the flow of capital. As mentioned, they take wages and prices as given. The problem of the firm can be written:

$$ 
\max \int_0^\infty \big[F(K_t, A_tL_t) - w_tL_t - I_t\big] R_t \;d_t \\ \text{} \;\; \dot K_t = I_t - \delta K_t
$$

$R_t = e^{-\int_0^t r_s\;ds}$ is the market discount factor, a cumulation of the interest rate $r_s$ on the interval $[0, t]$. The Hamiltonian for this problem is:

$$
\mathcal{H}_t - F(K_t, A_tL_t) - w_tL_t - I_t + \mu_t(I_t - \delta K_t)
$$
In this Hamiltonian, $L_t$ and $I_t$ are control variables, $K_t$ is the the state variable and $\mu_t$ is the costate which measures the marginal value of capital.


The First Order Conditions for this problem are {cite:p}`nla.cat-vn609458`:

$$
\frac{\partial \mathcal{H_t}}{\partial I} = 0 \rightarrow \mu_t = 1
$$

$$
\frac{\partial \mathcal{H_t}}{\partial L} = 0 \rightarrow w_t = A_tF_2(K_t,A_tL_t)
$$

$$
-\frac{\partial \mathcal{H_t}}{\partial K} = \dot\mu - r\mu \rightarrow \dot\mu - r\mu = F_1(K_t, A_tL_t) + \delta\mu_t
$$

From the CRS property of the production function, these first order conditions can be written [^f1]:

$$
\mu_t = 1
$$

$$
w_t = (f(k_t) - k_t f'(k_t)) A_t 
$$

$$
r_t + \delta = f'(k_t)
$$

The marginal value of capital $\mu_t$ is equal to one for all $t$. This is an implication of the fact that there is only one good, capital and output can be transmuted into each other at rate one. 

Euler's theorem yields:

$$
w_tL_t + (r_t + \delta)K_t = Y_t
$$

showing that income is fully distributed to capital and labour.

The representative household faces the following budget constraint:

$$
\dot{\hat a_t} = (r_t - n)\hat a_t + w_t - \hat c_t
$$
where $\hat a$ is the per capital stock of assets hold by the representative household. The house hold is not able to keep borrowing infinitely, in order to impose this we introduce a No-Ponzi-Game constraint:

$$
\lim_{t \rightarrow \infty} \hat a_t L_t R_t \ge 0
$$

The household has the following optimisation problem:

$$
\max \int_0^\infty u(\hat c_t)e^{-(\rho-n)t} \;dt \\ 

\text{s.t } \dot{\hat a_t = (r_t - n)\hat a_t + w_t - \hat c_t} \\
\text{and } \lim_{t \rightarrow \infty} \hat a_t L_t R_t \ge 0
$$

The Hamiltonian for the household's problem is:

$$
\mathcal{H_t} = u(\hat c_t) + \lambda_t\left((r_t - n) \hat a_t + w_t - \hat c_t\right)
$$

The first order conditions for this problem are:

$$
\frac{\partial\mathcal{H}_t}{\partial \hat c_t} =0 \rightarrow u'(\hat c_t) = \lambda_t
$$

$$
\frac{\partial\mathcal{H}_t}{\partial \hat a_t} =0 \rightarrow -\dot\lambda_t + (\rho - n)\lambda_t \rightarrow (r_t - n)\lambda_t = -\dot\lambda_t + (\rho - n)\lambda_t
$$

Notice that the above can be written

$$
\frac{\dot \lambda_t}{\lambda_t} = \rho -r_t
$$

Using the functional form for the households utility function we can find the Euler Equation:

$$
\frac{\dot{\hat c_t}}{\hat c_t} = \sigma_t(r_t - \rho)
$$

This equation is the optimal allocation of consumption over time. The larger the time-preference parameter $\rho$, the higher the household values current consumer, making them more impatient. The interest rate, $r_t$, shows the market value of time, larger interest rates means that it becomes relatively more attractive to postpone consumption. When $r_t > \rho$ the market assigns more value to time than households, making it more attractive to postpone consumption.

### Market Clearing and Equilibrium

Clearing in the credit market requires that $\hat a_t L_t = K_t$. This means that total borrowing is fully allocated to purchasing capital.

Combining the budget constraint with the optimal demands for labour and capital, we can derive the feasibility condition:

$$
\dot k_t = f(k_t) - c_t - (\delta + \gamma + n)k_t
$$

After some substitution, the Euler Equation can be written:

$$
\frac{\dot c_t}{c_t} = \sigma \left(f'(k_t) - \rho - \delta - \frac{\gamma}{\sigma}\right)
$$

We can, then, define an equilibrium path for the Neoclassical economy for $\{c_t, k_t\}, t \ge 0$, where these conditions hold.






# References
<!-- ## The Neoclassical Growth Model -->
```{bibliography} ../../zreferences.bib
:filter: docname in docnames
```


[^f1]: From the definition of the production function in efficiency units.