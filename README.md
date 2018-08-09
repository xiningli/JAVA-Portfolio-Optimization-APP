{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# PSTAT 234 Final Project - Portfolio Optimization\n",
    "\n",
    "*Group: Xining Li, Ben Ku, Mi Yu, Zhipu Zhou*\n",
    "\n",
    "\n",
    "## Summary\n",
    "\n",
    "Welcome to the PSTAT 234 final project report of our group. The topic of this report is portfolio optimization. \n",
    "\n",
    "Portfolio optimization has wide application in financial industry. To make investment in a group of assets, investors need to construct a portfolio that determines how much money we should allocate to each asset. Generally, investors are risk-inverse -- they pursue high portfolio return while avoid uncertainty of return (i.e. risk). This leads to the primary objective of portfolio optimization: how to maximize the portfolio return at a given level of risk, or how to minimize portfolio risk at a given level of portfolio return. In Markovitz mean-variance portfolio model [1], risk is measured by the standard deviation of portfolio returns, and the optimal portfolio allocation is totally determined by the true return of each asset and the covariance matrix of the returns of the group of assets. However, in practice, the true returns and covariance matrix are not observable, they can only be estimated from asset historical data.\n",
    " \n",
    "There are many ways to estimate the covariance matrix of returns of a group of assets. In this report, we will compare 3 estimation methods for the true covariance matrix or its inverse. As a result, we need to consider the minimal variance portfolio (MVP) model [2], instead of the mean-variance portfolio model. The former pursues to minimize portfolio risk regardless of the portfolio return and only requires to estimate the covariance matrix. It provides a better setting to compare the effectiveness of different (inverse) covariance matrix estimations. One problem of using historical data to estimate (inverse) covariance matrix is that because the financial market is not stationary, it needs to re-computed periodically (called rebalancing). This report will compare different rebalancing frequencies for each estimation method.\n",
    "\n",
    "\n",
    "## Project objectives\n",
    "\n",
    "The objectives of this report include:\n",
    "\n",
    "- Introduction to MVP model with rebalancing \n",
    "- 3 (inverse) covariance matrix estimations: sample covariance estimation, Ledoit-Wolf estimation [3], graphical lasso estimation [4].\n",
    "- Conduct empirical study to compare of portfolio performance."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction to MVP model with rebalancing\n",
    "\n",
    "Suppose that we invest among $p$ assets. Let $r_{ti}$ is the daily return of $i$-th asset at time $t$, and $r_t = (r_{t1}, r_{t2}, \\cdots, r_{tp})^T$ be the daily return vector of all assets at time $t$. Assume that the true covariance matrix of asset returns is $\\Sigma$, then the optimal portfolio allocation is given by \n",
    "\\begin{equation}\n",
    "\\text{minimize}_{w\\in\\mathbb{R}^p}\\quad w^T\\Sigma w\\quad\\text{subject to}\\quad \\mathbf{1}^Tw = 1\n",
    "\\end{equation}\n",
    "where $\\mathbf{1} = ({1,1,\\cdots, 1})^T$. $\\Sigma$ is unobservable and we need to estimate it using $\\hat{\\Sigma}$ from market historical data. However, because returns are not stationary over time, the estimated covariance of returns must be periodically updated. A general way is to periodically re-calculate $\\hat{\\Sigma}$ and rebalance the portfolio. Suppose that portfolio rebalancing period is $L$, meaning that every $L$ days the portfolio will be rebalanced once. Let $T_0$ be the investment starting time, and $T_E$ be the end time. The number of rebalancing times \n",
    "\\begin{equation}\n",
    "\\mathcal{T} = \n",
    "\\begin{cases}\n",
    "&\\lfloor\\frac{T_E - T_0}{L}\\rfloor,\\quad&\\text{if $\\frac{T_E - T_0}{L}$ is not an integer}\\\\\n",
    "&\\frac{T_E - T_0}{L}-1,\\quad&\\text{if $\\frac{T_E - T_0}{L}$ is an integer}\n",
    "\\end{cases}\n",
    "\\end{equation}\n",
    "The rebalancing time points are assumed to be $T_1, T_2, \\cdots, T_k, \\cdots, T_{\\mathcal{T}}$ with $T_k - T_{k-1} = L$ for $k=1, 2, \\cdots, \\mathcal{T}$. Suppose that the estimated covariance matrix for $k$-th rebalancing period is $\\hat{\\Sigma}_k$. Under MVP model, the portfolio allocation $w_k = (w_{k1}, w_{k2}, \\cdots, w_{kp})$ during $k$-th period is\n",
    "\n",
    "\\begin{equation}\n",
    "w_k = \\text{argmin}_{w\\in\\mathbb{R}^p}\\quad w^T\\hat{\\Sigma}_kw\\quad\\text{subject to}\\quad \\mathbf{1}^Tw = 1\n",
    "\\end{equation}\n",
    "\n",
    "The solution to this model is\n",
    "\n",
    "\\begin{equation}\n",
    "w_k = (\\mathbf{1}^T\\hat{\\Sigma}_k^{-1}\\mathbf{1})^{-1}\\hat{\\Sigma}_k^{-1}\\mathbf{1}\n",
    "\\end{equation}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Model parameter estimations\n",
    "\n",
    "- **Sample covariance matrix estimator**: A standard way to estimate covariance matrix is sample covariance matrix. For $k$-th period, the sample covariance matrix estimation is\n",
    "\\begin{equation}\n",
    "S = \\frac{1}{L-1}\\sum_{t=T_{k-1}+1-L}^{T_{k-1}}(r_t-\\bar{r}_{k-1})(r_t-\\bar{r}_{k-1})^T\n",
    "\\quad\\text{where}\\quad\n",
    "\\bar{r}_{k-1} = \\biggl(\\frac{1}{L}\\sum_{t = T_{k-1}+1-L}^{T_{k-1}}r_{t1}, \\cdots, \\frac{1}{L}\\sum_{t = T_{k-1}+1-L}^{T_{k-1}}r_{tp}\\biggr)\n",
    "\\end{equation}\n",
    "\n",
    "- **Ledoit-Wolf shrinkage estimator**: The problem of using sample covariance matrix estimation is that in high dimensional case where $L\\leq p$, $S$ is singular and not invertible. Also, it has been shown [5] that sample covariance matrix contains large estimation error that could distort the portfolio optimization.  Many regularization methods have been proposed to estimate (inverse) covariance matrix. For example, the Ledoit-Wolf shrinkage estimator\n",
    "\\begin{equation}\n",
    "\\lambda S + (1-\\lambda)I\n",
    "\\end{equation}\n",
    "where $S$ is the sample covariance matrix, $\\lambda\\in[0,1]$ is a tuning parameter, and $I$ is the identity matrix. \n",
    "\n",
    "- **Graphical lasso estimator**: Although Ledoit-Wolf estimator helps to shrink extreme covariances to zero, its result is dense and fails to give a sparse matrix. Thi impose difficulty to interpret the dependences among asset returns. To solve this difficulty, [4] focuses on estimating inverse covariance matrix (also called precision matrix and is denoted as $\\Omega = \\Sigma^{-1}$) and proposes graphical lasso estimator:\n",
    "\\begin{equation}\n",
    "\\text{argmin}_{\\Omega\\in\\mathbb{R}^{p\\times p}}-\\log\\text{det}\\Omega + \\text{tr}(S\\Omega) + \\lambda\\|\\Omega\\|_1\n",
    "\\end{equation}\n",
    "where $\\|\\cdot\\|_1$ is $l_1$ norm, $\\text{det}\\Omega$ is the determinant of $\\Omega$, $\\text{tr}(S\\Omega)$ is the trace of $S\\Omega$, $S$ is sample covariance matrix, and $\\lambda$ is a tuning parameter. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tuning parameter determination"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Portfolio performance measurements\n",
    "\n",
    "Denote $k_t = k(t) = \\{t: t\\in[T_{k-1}+1, T_k]\\}$, and we assume that there are 252 trading days per year. Following quantities are generally used to measure the performance of a portfolio [2]:\n",
    "\n",
    "- **Realized return**: the annualized average return of the portfolio over the entire investment horizon $[T_0, T_E]$:\n",
    "\n",
    "\\begin{equation}\n",
    "r_p = \\frac{252}{T_E - T_0}\\sum_{t=T_0+1}^{T_E}r_t^Tw_{k_t}\n",
    "\\end{equation}\n",
    "\n",
    "- **Realized risk**: the standard deviation of portfolio over the entire investment horizon:\n",
    "\n",
    "\\begin{equation}\n",
    "\\sigma_p = \\sqrt{\\frac{252}{T_E-T_0}\\sum_{t=T_0+1}^{T_E}(r_t^Tw_{k_t} - r_p)^2}\n",
    "\\end{equation}\n",
    "\n",
    "- **Sharpe ratio**: the realized excess return of portfolio over the annualized risk-free interest rate $r_f$ per unit realized risk.\n",
    "\n",
    "\\begin{equation}\n",
    "SR = \\frac{r_p - r_f}{\\sigma_p}\n",
    "\\end{equation}\n",
    "\n",
    "- **Turnover**: the amount of new portfolio assets purchased or sold over $k$-th period:\n",
    "\\begin{equation}\n",
    "TO(k) = \\biggl\\|w_k - w_{k-1}\\cdot\\bigodot_{t=T_{k-1}+1}^{T_k}(1+r_t)\\biggr\\|_1\n",
    "\\end{equation}\n",
    "where \n",
    "\\begin{equation}\n",
    "\\bigodot_{t=T_{k-1}+1}^{T_k}(1+r_t) = (1+r_{T_{k-1}+1})\\cdot(1+r_{T_{k-1}+2})\\cdot\\cdots\\cdot(1+r_{T_k})\n",
    "\\end{equation}\n",
    "and $\\cdot$ is dot product, $w_0 = (0,0,\\cdots, 0)$. The average turnover over the entire investment horizon is:\n",
    "\\begin{equation}\n",
    "\\overline{TO} = \\frac{1}{\\mathcal{T}}\\sum_{k=1}^{\\mathcal{T}}TO(k)\n",
    "\\end{equation}\n",
    "\n",
    "- **Size of short side**: the proportion of negative weights to the sum of absolute weights of portfolio allocation at $k$-th period:\n",
    "\\begin{equation}\n",
    "SS(k) = \\frac{\\sum_{i=1}^p|\\min(w_{ki},0)|}{\\sum_{i=1}^p|w_{ki}|}\n",
    "\\end{equation}\n",
    "and the average short side over the investment horizon is\n",
    "\\begin{equation}\n",
    "\\overline{SS} = \\frac{1}{\\mathcal{T}}\\sum_{k=1}^{\\mathcal{T}}SS(k)\n",
    "\\end{equation}\n",
    "\n",
    "- **Normalized wealth**: accumulated wealth of portfolio with initial budget is 1 dollar. Transaction costs and borrowing costs are taken into consideration. Let $r_c$ be the transaction cost rate and $r_b$ be the daily borrowing cost rate of interest, the transaction cost incurred in the beginning of $k$-th period is \n",
    "\\begin{equation}\n",
    "TC(k) = r_c\\times TO(k)\n",
    "\\end{equation}\n",
    "and the borrowing cost incurred in $k$-th period is \n",
    "\\begin{equation}\n",
    "BC(k) = ((1+r_b)^L-1)\\sum_{i=1}^p|\\min(w_{k-1,i},0)|\n",
    "\\end{equation}\n",
    "Let $W_{t-1}$ represent the wealth of portfolio after time $t-1$, then wealth of portfolio after time $t$ is\n",
    "\\begin{equation}\n",
    "W_t =\n",
    "\\begin{cases}\n",
    "&W_{t-1}(1+r_t^Tw_{k_t} - TC(k_t) - BC(k_t)), &t = T_{k_t-1}+1\\\\\n",
    "&W_{t-1}(1+r_t^Tw_{k_t}), & t\\neq T_{k_t-1}+1\n",
    "\\end{cases}\n",
    "\\end{equation}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [

}
