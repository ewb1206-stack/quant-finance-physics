import numpy as np


# --- Monte Carlo European Call Option Pricer ---
# Returns the risk-neutral price of a European call option
# using exact GBM simulation and risk-free discounting


def monte_carlo_pricer(S0=100,K=110,r=0.03,sigma=0.2,T=1,steps=252,paths=1000):
    dt = T/steps
    Z = np.random.normal(0,1,(paths,steps))
    returns =  np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)
    prices = S0 * np.cumprod(returns, axis =1)
    payoffs = np.maximum(prices[:,-1]-K, 0)
    option_price = np.mean(payoffs) * np.exp(-r*T)
    
    return(option_price)


