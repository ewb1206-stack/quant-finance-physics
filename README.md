## Stochastic Asset Modelling

Geometric Brownian Motion (GBM) is the mathematical foundation of modern quantitative finance. It models asset prices as a continuous random walk with constant drift and volatility. This project implements GBM from first principles using the stochastic differential equation dS = μS dt + σS dW, where μ is the expected return, σ is volatility, and dW is a Wiener process increment. By simulating 1,000-day price trajectories across different volatility regimes, it demonstrates how standard deviation directly governs the distribution of possible asset outcomes — a core concept in risk modelling and derivative pricing.

A Python-based simulation engine using Geometric Brownian Motion to model and compare asset price trajectories under different volatility regimes.

## Key Features

- Stochastic Simulation: Uses NumPy to generate 1,000 days of market activity based on random walks.
- Comparative Analysis: Contrasts stable vs. volatile asset profiles by varying standard deviation.
- Visualisation: Matplotlib implementation featuring statistical mean markers for risk-adjusted return analysis.

![GBM Simulation Output](1000DaySimulation.png)

## Notes on Stochastic Behaviour

Each run produces a unique price trajectory by design. Results vary between executions, illustrating path dependency and why average price alone is an insufficient risk metric.

## Usage

Requires numpy and matplotlib. Run the script directly to generate a comparative plot:
python "Geometric Brownian Motion.py"

## Project 2: Monte Carlo Options Pricing

This project extends the GBM framework to price European call options using Monte Carlo simulation. By generating 1,000 price paths over 252 trading days, it estimates the fair value of a call option from first principles and analyses how drift affects the option price.

### Key Features

- Options Pricing: Estimates call option price by averaging payoffs across 1,000 simulated paths
- Drift Analysis: Compares option prices under zero drift (μ = 0) and positive drift (μ = 0.0003)
- Visualisation: Three charts — simulated price paths, net profit distribution, and final price distribution

### Results

- No drift: option price £8.39, break-even at £118.39
- With drift: option price rises to £12.72
- Core insight: drift shifts the final price distribution rightward, increasing the proportion of paths expiring in-the-money and raising the expected payoff

### Notes on Stochastic Behaviour

Each run produces unique results by design. The drift comparison isolates the effect of expected return on option valuation — a core concept in derivatives pricing.
