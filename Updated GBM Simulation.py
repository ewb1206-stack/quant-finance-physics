import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#parameters

S0 = 100
K = 110
r = 0.03
sigma = 0.2
T = 1
steps = 252
dt = T / steps
paths = 10000

#simulation

Z = np.random.normal(0,1,(paths,steps))
returns =  np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)
prices = S0 * np.cumprod(returns, axis =1)

#option pricing

payoffs = np.maximum(prices[:,-1]-K, 0)
option_price = np.mean(payoffs) * np.exp(-r*T)

#BS verification

d1 =  (np.log(S0 / K) + (r+0.5*sigma**2)*T) / (sigma * np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
C = S0 * norm.cdf(d1)- K*np.exp(-r*T) * norm.cdf(d2)

print(f"Monte Carlo Option Price: {option_price:.4f}")
print(f"Black Scholes Option Price: {C:.4f}")

#plot

plt.figure()
plt.plot(prices[:50].T, alpha = 0.3)
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('GBM Simulated Price Paths')
plt.axhline(S0, color = 'red', linestyle  = '--', linewidth = 1)


plt.show()
