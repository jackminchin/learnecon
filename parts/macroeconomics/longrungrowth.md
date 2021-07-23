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




# References
<!-- ## The Neoclassical Growth Model -->
```{bibliography} ../../zreferences.bib
```