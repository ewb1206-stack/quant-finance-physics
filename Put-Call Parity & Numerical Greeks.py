import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo European option pricer with put/call support,
# put-call parity verification, and numerical delta estimation
# via finite differences with common random numbers.

K = 110
S0 = 100
r = 0.03
T = 1
paths = 100000
steps = 252
h = 1

def monte_carlo_pricer(Z, S0=100, K=110, r=0.03, sigma=0.2, T=1, steps=252, paths=10000, option_type='call'):
    dt = T/steps
    returns = np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)
    prices = S0 * np.cumprod(returns, axis=1)
    if option_type == 'call':
        payoffs = np.maximum(prices[:,-1]-K, 0)
    else:
        payoffs = np.maximum(K-prices[:,-1], 0)
    option_price = np.mean(payoffs) * np.exp(-r*T)
    return option_price

# --- Put-call parity verification ---
Z_parity = np.random.normal(0, 1, (paths, steps))
C = monte_carlo_pricer(Z_parity, S0=S0, K=K, r=r, T=T, paths=paths, steps=steps, option_type='call')
P = monte_carlo_pricer(Z_parity, S0=S0, K=K, r=r, T=T, paths=paths, steps=steps, option_type='put')
parity_P = C - S0 + K*np.exp(-r*T)

print(f"Call price: {C}")
print(f"Put price: {P}")
print(f"Put price from parity: {parity_P}")
print(f"Difference: {abs(P - parity_P)}")

# --- Delta sweep across a range of spot prices ---
S0_range = np.linspace(70, 130, 50)
Z_delta = np.random.normal(0, 1, (paths, steps))
deltas = []

for S in S0_range:
    price_up = monte_carlo_pricer(Z_delta, S0=S+h, K=K, r=r, T=T, paths=paths, steps=steps)
    price_down = monte_carlo_pricer(Z_delta, S0=S-h, K=K, r=r, T=T, paths=paths, steps=steps)
    deltas.append((price_up - price_down)/(2*h))

plt.figure()
plt.plot(S0_range, deltas)
plt.axvline(x=K, color='red', linestyle='--', alpha=0.5, label=f'Strike (K={K})')
plt.xlabel('Spot Price ($)')
plt.ylabel('Delta')
plt.title('Variation of Delta')
plt.legend()
plt.savefig('delta_vs_spot.png')
plt.show()