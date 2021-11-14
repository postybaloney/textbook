#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** A box contains two coins, one of which lands heads with chance $p_1$ while the other lands heads with chance $p_2$. One of the coins is picked at random and tossed $n$ times. Find the expectation and variance of the number of heads.

# **2.** A positive random variable $V$ has expectation $\mu$ and variance $\sigma^2$. 
# 
# (a) For each $v > 0$, the conditional distribution of $X$ given $V=v$ is Poisson $(v)$. Find $E(X)$ and $Var(X)$.
# 
# (b) For each $v > 0$, the conditional distribution of $X$ given $V=v$ is gamma $(v, \lambda)$ for some fixed $\lambda$. Find $E(X)$ and $Var(X)$.

# **3.** The lifetime of each Type A battery has the exponential distribution with mean $100$ hours. The lifetime of each Type B battery has the exponential distribution with mean $150$ hours. Assume that the lifetimes of all batteries are independent of each other.
# 
# Suppose I have a packet of five batteries of which four are of Type A and one is of Type B. Let $T$ be the lifetime of a battery picked at random from this packet. Find $E(T)$ and $SD(T)$.

# **4.** The lifetime of each Type A battery has the exponential distribution with mean $100$ hours. The lifetime of each Type B battery has the exponential distribution with mean $150$ hours. Assume that the lifetimes of all batteries are independent of each other.
# 
# A factory produces large numbers of batteries, of which $80\%$ are of Type A and $20\%$ are of Type B. Suppose you pick batteries one by one at random from the factory's total output until you pick a Type B battery. Let $N$ be the number of Type A batteries that you pick, and let $T$ be the total lifetime of these $N$ batteries.
# 
# (a) Find $E(N)$ and $SD(N)$.
# 
# (b) Find $E(T)$ and $SD(T)$.

# **5.** Think of the interval $(0, l)$ as a stick of length $l$. The stick is broken at a point $L_1$ chosen uniformly along it. This creates a smaller stick of random length $L_1$ which is then broken at a point $L_2$ chosen uniformly along it. Find $E(L_2)$ and $SD(L_2)$.

# **6.** Let $X_1, X_2, \ldots, X_n$ be i.i.d. with expectation $\mu$ and variance $\sigma^2$. Let $S = \sum_{i=1}^n X_i$.
# 
# (a) Find the least squares predictor of $S$ based on $X_1$, and find the mean squared error (MSE) of the predictor.
# 
# (b) Find the least squares predictor of $X_1$ based on $S$, and find the MSE of the predictor. Is the predictor a linear function of $S$? If so, it must also be the best among all linear predictors based on $S$, which is commonly known as the regression predictor. 
# 
# [Consider whether your predictor in (b) would be different if $X_1$ were replaced by $X_2$, or by $X_3$, or by $X_i$ for any fixed $i$. Then use symmetry and the additivity of conditional expectation.]

# **7.** Let $X$ and $Y$ be jointly distributed random variables, and as in [Section 22.1](http://prob140.org/textbook/content/Chapter_22/01_Conditional_Expectation_Projection.html) let $b(X) = E(Y \mid X)$. Show that $Cov(X, Y) = Cov(X, b(X))$.

# **8.** A $p$-coin is tossed repeatedly. Let $W_{H}$ be the number of tosses till the first head appears, and $W_{HH}$ the number of tosses till two consecutive heads appear.
# 
# (a) Describe a random variable $X$ that  depends only on the tosses after $W_H$ and satisfies $W_{HH} = W_H + X$.
# 
# (b) Use Part (a) to find $E(W_{HH})$. What is its value when $p = 1/2$?
# 
# (c) Use Parts (a) and (b) to find $Var(W_{HH})$. What is the value of $SD(W_{HH})$ when $p = 1/2$?

# In[ ]:




