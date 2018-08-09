
# PSTAT 234 Final Project - Portfolio Optimization

*Group: Xining Li, Ben Ku, Mi Yu, Zhipu Zhou*


## Summary

Welcome to the PSTAT 234 final project report of our group. The topic of this report is portfolio optimization. 

Portfolio optimization has wide application in financial industry. To make investment in a group of assets, investors need to construct a portfolio that determines how much money we should allocate to each asset. Generally, investors are risk-inverse -- they pursue high portfolio return while avoid uncertainty of return (i.e. risk). This leads to the primary objective of portfolio optimization: how to maximize the portfolio return at a given level of risk, or how to minimize portfolio risk at a given level of portfolio return. In Markovitz mean-variance portfolio model [1], risk is measured by the standard deviation of portfolio returns, and the optimal portfolio allocation is totally determined by the true return of each asset and the covariance matrix of the returns of the group of assets. However, in practice, the true returns and covariance matrix are not observable, they can only be estimated from asset historical data.
 
There are many ways to estimate the covariance matrix of returns of a group of assets. In this report, we will compare 3 estimation methods for the true covariance matrix or its inverse. As a result, we need to consider the minimal variance portfolio (MVP) model [2], instead of the mean-variance portfolio model. The former pursues to minimize portfolio risk regardless of the portfolio return and only requires to estimate the covariance matrix. It provides a better setting to compare the effectiveness of different (inverse) covariance matrix estimations. One problem of using historical data to estimate (inverse) covariance matrix is that because the financial market is not stationary, it needs to re-computed periodically (called rebalancing). This report will compare different rebalancing frequencies for each estimation method.


## Project objectives

The objectives of this report include:

- Introduction to MVP model with rebalancing 
- 3 (inverse) covariance matrix estimations: sample covariance estimation, Ledoit-Wolf estimation [3], graphical lasso estimation [4].
- Conduct empirical study to compare of portfolio performance.


## Introduction to MVP model with rebalancing

Suppose that we invest among $p$ assets. Let $r_{ti}$ is the daily return of $i$-th asset at time $t$, and $r_t = (r_{t1}, r_{t2}, \cdots, r_{tp})^T$ be the daily return vector of all assets at time $t$. Assume that the true covariance matrix of asset returns is $\Sigma$, then the optimal portfolio allocation is given by 
\begin{equation}
\text{minimize}_{w\in\mathbb{R}^p}\quad w^T\Sigma w\quad\text{subject to}\quad \mathbf{1}^Tw = 1
\end{equation}
where $\mathbf{1} = ({1,1,\cdots, 1})^T$. $\Sigma$ is unobservable and we need to estimate it using $\hat{\Sigma}$ from market historical data. However, because returns are not stationary over time, the estimated covariance of returns must be periodically updated. A general way is to periodically re-calculate $\hat{\Sigma}$ and rebalance the portfolio. Suppose that portfolio rebalancing period is $L$, meaning that every $L$ days the portfolio will be rebalanced once. Let $T_0$ be the investment starting time, and $T_E$ be the end time. The number of rebalancing times 
\begin{equation}
\mathcal{T} = 
\begin{cases}
&\lfloor\frac{T_E - T_0}{L}\rfloor,\quad&\text{if $\frac{T_E - T_0}{L}$ is not an integer}\\
&\frac{T_E - T_0}{L}-1,\quad&\text{if $\frac{T_E - T_0}{L}$ is an integer}
\end{cases}
\end{equation}
The rebalancing time points are assumed to be $T_1, T_2, \cdots, T_k, \cdots, T_{\mathcal{T}}$ with $T_k - T_{k-1} = L$ for $k=1, 2, \cdots, \mathcal{T}$. Suppose that the estimated covariance matrix for $k$-th rebalancing period is $\hat{\Sigma}_k$. Under MVP model, the portfolio allocation $w_k = (w_{k1}, w_{k2}, \cdots, w_{kp})$ during $k$-th period is

\begin{equation}
w_k = \text{argmin}_{w\in\mathbb{R}^p}\quad w^T\hat{\Sigma}_kw\quad\text{subject to}\quad \mathbf{1}^Tw = 1
\end{equation}

The solution to this model is

\begin{equation}
w_k = (\mathbf{1}^T\hat{\Sigma}_k^{-1}\mathbf{1})^{-1}\hat{\Sigma}_k^{-1}\mathbf{1}
\end{equation}


## Model parameter estimations

- **Sample covariance matrix estimator**: A standard way to estimate covariance matrix is sample covariance matrix. For $k$-th period, the sample covariance matrix estimation is
\begin{equation}
S = \frac{1}{L-1}\sum_{t=T_{k-1}+1-L}^{T_{k-1}}(r_t-\bar{r}_{k-1})(r_t-\bar{r}_{k-1})^T
\quad\text{where}\quad
\bar{r}_{k-1} = \biggl(\frac{1}{L}\sum_{t = T_{k-1}+1-L}^{T_{k-1}}r_{t1}, \cdots, \frac{1}{L}\sum_{t = T_{k-1}+1-L}^{T_{k-1}}r_{tp}\biggr)
\end{equation}

- **Ledoit-Wolf shrinkage estimator**: The problem of using sample covariance matrix estimation is that in high dimensional case where $L\leq p$, $S$ is singular and not invertible. Also, it has been shown [5] that sample covariance matrix contains large estimation error that could distort the portfolio optimization.  Many regularization methods have been proposed to estimate (inverse) covariance matrix. For example, the Ledoit-Wolf shrinkage estimator
\begin{equation}
\lambda S + (1-\lambda)I
\end{equation}
where $S$ is the sample covariance matrix, $\lambda\in[0,1]$ is a tuning parameter, and $I$ is the identity matrix. 

- **Graphical lasso estimator**: Although Ledoit-Wolf estimator helps to shrink extreme covariances to zero, its result is dense and fails to give a sparse matrix. Thi impose difficulty to interpret the dependences among asset returns. To solve this difficulty, [4] focuses on estimating inverse covariance matrix (also called precision matrix and is denoted as $\Omega = \Sigma^{-1}$) and proposes graphical lasso estimator:
\begin{equation}
\text{argmin}_{\Omega\in\mathbb{R}^{p\times p}}-\log\text{det}\Omega + \text{tr}(S\Omega) + \lambda\|\Omega\|_1
\end{equation}
where $\|\cdot\|_1$ is $l_1$ norm, $\text{det}\Omega$ is the determinant of $\Omega$, $\text{tr}(S\Omega)$ is the trace of $S\Omega$, $S$ is sample covariance matrix, and $\lambda$ is a tuning parameter. 

## Tuning parameter determination


## Portfolio performance measurements

Denote $k_t = k(t) = \{t: t\in[T_{k-1}+1, T_k]\}$, and we assume that there are 252 trading days per year. Following quantities are generally used to measure the performance of a portfolio [2]:

- **Realized return**: the annualized average return of the portfolio over the entire investment horizon $[T_0, T_E]$:

\begin{equation}
r_p = \frac{252}{T_E - T_0}\sum_{t=T_0+1}^{T_E}r_t^Tw_{k_t}
\end{equation}

- **Realized risk**: the standard deviation of portfolio over the entire investment horizon:

\begin{equation}
\sigma_p = \sqrt{\frac{252}{T_E-T_0}\sum_{t=T_0+1}^{T_E}(r_t^Tw_{k_t} - r_p)^2}
\end{equation}

- **Sharpe ratio**: the realized excess return of portfolio over the annualized risk-free interest rate $r_f$ per unit realized risk.

\begin{equation}
SR = \frac{r_p - r_f}{\sigma_p}
\end{equation}

- **Turnover**: the amount of new portfolio assets purchased or sold over $k$-th period:
\begin{equation}
TO(k) = \biggl\|w_k - w_{k-1}\cdot\bigodot_{t=T_{k-1}+1}^{T_k}(1+r_t)\biggr\|_1
\end{equation}
where 
\begin{equation}
\bigodot_{t=T_{k-1}+1}^{T_k}(1+r_t) = (1+r_{T_{k-1}+1})\cdot(1+r_{T_{k-1}+2})\cdot\cdots\cdot(1+r_{T_k})
\end{equation}
and $\cdot$ is dot product, $w_0 = (0,0,\cdots, 0)$. The average turnover over the entire investment horizon is:
\begin{equation}
\overline{TO} = \frac{1}{\mathcal{T}}\sum_{k=1}^{\mathcal{T}}TO(k)
\end{equation}

- **Size of short side**: the proportion of negative weights to the sum of absolute weights of portfolio allocation at $k$-th period:
\begin{equation}
SS(k) = \frac{\sum_{i=1}^p|\min(w_{ki},0)|}{\sum_{i=1}^p|w_{ki}|}
\end{equation}
and the average short side over the investment horizon is
\begin{equation}
\overline{SS} = \frac{1}{\mathcal{T}}\sum_{k=1}^{\mathcal{T}}SS(k)
\end{equation}

- **Normalized wealth**: accumulated wealth of portfolio with initial budget is 1 dollar. Transaction costs and borrowing costs are taken into consideration. Let $r_c$ be the transaction cost rate and $r_b$ be the daily borrowing cost rate of interest, the transaction cost incurred in the beginning of $k$-th period is 
\begin{equation}
TC(k) = r_c\times TO(k)
\end{equation}
and the borrowing cost incurred in $k$-th period is 
\begin{equation}
BC(k) = ((1+r_b)^L-1)\sum_{i=1}^p|\min(w_{k-1,i},0)|
\end{equation}
Let $W_{t-1}$ represent the wealth of portfolio after time $t-1$, then wealth of portfolio after time $t$ is
\begin{equation}
W_t =
\begin{cases}
&W_{t-1}(1+r_t^Tw_{k_t} - TC(k_t) - BC(k_t)), &t = T_{k_t-1}+1\\
&W_{t-1}(1+r_t^Tw_{k_t}), & t\neq T_{k_t-1}+1
\end{cases}
\end{equation}

