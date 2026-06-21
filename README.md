## Stochastic Asset Modelling

Geometric Brownian Motion (GBM) is the mathematical foundation of modern quantitative finance. It models asset prices as a continuous random walk with constant drift and volatility. This project implements GBM from first principles using the stochastic differential equation dS = μS dt + σS dW, where μ is the expected return, σ is volatility, and dW is a Wiener process increment. By simulating 1,000-day price trajectories across different volatility regimes, it demonstrates how standard deviation directly governs the distribution of possible asset outcomes — a core concept in risk modelling and derivative pricing.

A Python-based simulation engine using Geometric Brownian Motion to model and compare asset price trajectories under different volatility regimes.

## Key Features

- Stochastic Simulation: Uses NumPy to generate 1,000 days of market activity based on random walks.
- Comparative Analysis: Contrasts stable vs. volatile asset profiles by varying standard deviation.
- Visualisation: Matplotlib implementation featuring statistical mean markers for risk-adjusted return analysis.

![GBM Simulation Output](simulation.png)

## Notes on Stochastic Behaviour

Each run produces a unique price trajectory by design. Results vary between executions, illustrating path dependency and why average price alone is an insufficient risk metric.

## Usage

Requires numpy and matplotlib. Run the script directly to generate a comparative plot:
python "Geometric Brownian Motion.py"
