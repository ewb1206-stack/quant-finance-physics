from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

S0 = 100
K = 120
r = 0.03
sigma = 0.3
T = 5
steps = 252
dt = T / steps

d1 = (np.log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
C = S0 *norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
MC_prices=[]
path_values = list(range(100,10001,100))

for paths in path_values:

    changes = np.random.normal(0,1,(paths,steps))
    prices = S0 * np.cumprod(np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*changes), axis=1)
    payoff = np.maximum(prices[:,-1] -K,0)
    option_price = np.mean(payoff) *np.exp(-r*T)
    MC_prices.append(option_price)
   

plt.figure()
plt.plot(path_values,MC_prices, label= 'Monte Carlo Price')
plt.axhline(C,color = 'red', linestyle = '--', label = 'Black-Scholes Price')
plt.xlabel('Number of Paths')
plt.ylabel('Option Price')
plt.title('Convergence of Monte Carlo Simulation')
plt.legend()
plt.show()