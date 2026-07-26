# Quant Finance & Physics Portfolio

A collection of Python projects applying stochastic modelling 
and Monte Carlo methods to quantitative finance problems.

---

## Project 1: Stochastic Asset Modelling

Geometric Brownian Motion (GBM) is the mathematical foundation 
of modern quantitative finance. It models asset prices as a 
continuous random walk with constant drift and volatility — the 
same stochastic process that underpins the Black-Scholes framework.

### Volatility Regime Comparison
Implements GBM from first principles using the stochastic differential equation (SDE) dS = μS dt + σS dW, 
simulating 1,000-day price trajectories across different volatility 
regimes to demonstrate how standard deviation governs the distribution 
of possible asset outcomes.

**Key features:** comparative volatility analysis | NumPy random 
walks | Matplotlib visualisation with statistical mean markers

![GBM Simulation Output](1000DaySimulation.png)

### Exact GBM with Options Pricing
Rebuilds GBM using the exact log-normal formula, simulating 10,000 
price paths over 252 trading days. Prices a European call option 
via Monte Carlo and verifies against the Black-Scholes analytical 
solution.

<img src="Updated GBM Simulation.png" width="400"/>

**Key features:** exact GBM log-normal simulation | Monte Carlo 
option pricing | Black-Scholes verification | risk-neutral discounting

---

## Project 2: Monte Carlo Options Pricing

Extends the GBM framework to price European call options from first 
principles. Simulates 1,000 price paths over 252 trading days, 
computing call option value as the mean payoff across all paths.

Compares pricing under zero drift (μ = 0) vs positive drift 
(μ = 0.0003), demonstrating how expected return shifts the final 
price distribution rightward — increasing in-the-money paths and 
raising the expected payoff. A fundamental concept in derivatives 
pricing.

**Key features:** call option pricing | drift analysis | profit 
distribution visualisation | percentile risk metrics

<img src="price_paths.png" width="400"/>
<img src="profit_distribution.png" width="400"/>
<img src="final_price_distribution.png" width="400"/>

*Results vary between runs by design — stochastic behaviour 
is the point.*

---

## Project 3: Monte Carlo Convergence Analysis

Demonstrates the convergence of Monte Carlo option pricing toward the 
Black-Scholes analytical solution as the number of simulation paths increases.

Simulates a European call option across path counts from 100 to 50,000, 
plotting the MC price against the closed-form Black-Scholes price to 
visualise the law of large numbers in action.

**Key features:** convergence analysis | Black-Scholes verification | 
law of large numbers | exact GBM simulation.

<img src="Convergence Simulation.png" width="400"/>


## Project 4: Put-Call Parity & Numerical Greeks

Extends the Monte Carlo pricer to value European put options, then verifies the result against put-call parity, a no-arbitrage relationship that ties call and put prices together without needing a second pricing model. Both prices are computed independently and checked against the parity formula. The gap between them shrinks as path count increases, confirming the simulation converges correctly. The same pricer estimates delta numerically via finite differences, using common random numbers to isolate the effect of spot price from simulation noise. Sweeping delta across a range of spot prices reproduces the S-shaped curve from the Black-Scholes formula, with the risk sensitivity emerging naturally from the simulation rather than being borrowed from BS.

<img src="delta_vs_spot" width="400"/>
