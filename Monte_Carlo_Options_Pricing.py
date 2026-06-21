import numpy as np
import matplotlib.pyplot as plt

days = 252
paths = 1000
start_price = 100
r = 0.05
T = 1


changes = np.random.normal(0, 0.02,(paths,days))
prices = start_price * np.cumprod(1 +changes, axis=1)
final_prices = prices[:,-1]

strike_price = 110

payoffs = np.maximum(final_prices - strike_price,0) # this picks the biggest value either the profit we make or 0 if negative profit
option_price = np.mean(payoffs) * np.exp(-r*T)
net_profit = payoffs - option_price 
break_even = strike_price + option_price

print(f"Estimated option price: {option_price:.2f}")
print(f"Break-even price: {break_even:.2f}")
print(f"Average net profit: {np.mean(net_profit):.2f}")
print(f"Max loss: {-option_price:.2f}")
print(f"Mean final price: {np.mean(final_prices):.2f}")
print(f"5th percentile: {np.percentile(final_prices, 5):.2f}")
print(f"95th percentile: {np.percentile(final_prices, 95):.2f}")

mu = 0.0003
sigma = 0.02
changes_drift = np.random.normal(mu, sigma,(paths,days))
prices_drift = start_price*np.cumprod(1+changes_drift, axis=1)
final_drift = prices_drift[:,-1]

payoffs_drift = np.maximum(final_drift - strike_price, 0)
option_price_drift = np.mean(payoffs_drift) * np.exp(-r*T)
net_profit_drift = payoffs_drift - option_price_drift
break_even_drift = strike_price + option_price_drift


plt.figure()
plt.plot(prices[:50].T, alpha = 0.3)
plt.title("Monte Carlo Stock Price Simulation")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.grid(True, alpha=0.15)
plt.axhline(np.mean(final_prices), color='black', linestyle='--', linewidth=1)


plt.text(
    5, max(prices[:20].flatten()) * 0.92,
    f"Mean Final: {np.mean(final_prices):.2f}\n"
    f"5th Percentile: {np.percentile(final_prices, 5):.2f}\n"
    f"95th Percentile: {np.percentile(final_prices, 95):.2f}",
    fontsize=9,
    bbox=dict(facecolor="white", alpha=1))

fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)


# ---- No Drift ----
axs[0].axvline(np.mean(net_profit), color="black", linestyle=":")
axs[1].axvline(np.mean(net_profit_drift), color="black", linestyle=":")
axs[0].hist(net_profit, bins=30, color="blue", alpha=0.7,
            edgecolor="black", label="No Drift")

axs[0].axvline(0, color="red", linestyle="--", linewidth=2,
               label="Break-even")

axs[0].set_title("No Drift (μ = 0)")
axs[0].set_xlabel("Net Profit")
axs[0].set_ylabel("Frequency")
axs[0].grid(True, alpha=0.2)

axs[0].legend()

# ---- With Drift ----
axs[0].set_xlim(-20, 100)
axs[1].set_xlim(-20, 100)
axs[1].hist(net_profit_drift, bins=30, color="orange", alpha=0.7,
            edgecolor="black", label="With Drift")

axs[1].axvline(0, color="red", linestyle="--", linewidth=2,
               label="Break-even")

axs[1].set_title("With Drift (μ = 0.0003)")
axs[1].set_xlabel("Net Profit")
axs[1].grid(True, alpha=0.2)

axs[1].legend()

# ---- Shared Title ----
fig.suptitle("Option Net Profit Distribution")

# ---- Clean summary at bottom ----
fig.text(
    0.5, 0.01,
    f"No Drift Price: {option_price:.2f}   |   With Drift Price: {option_price_drift:.2f}",
    ha="center",
    fontsize=10
)

plt.tight_layout()

fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

# No drift
axs[0].hist(final_prices, bins=30, color="blue", edgecolor="black", alpha=0.7)
axs[0].axvline(np.mean(final_prices), color="purple", linestyle="--", linewidth=2, label="Mean")
axs[0].axvline(strike_price, color="red", linestyle="--", linewidth=2.5, label="Strike")
axs[0].set_title("No Drift")
axs[0].set_xlabel("Final Price")
axs[0].set_ylabel("Frequency")
axs[0].legend(loc="upper right")
axs[0].grid(True, alpha=0.2)

# With drift
axs[1].hist(final_drift, bins=30, color="orange", edgecolor="black", alpha=0.7)
axs[1].axvline(np.mean(final_drift), color="purple", linestyle="--", linewidth=2, label="Mean")
axs[1].axvline(strike_price, color="red", linestyle="--", linewidth=2, label="Strike")
axs[1].set_title("With Drift")
axs[1].set_xlabel("Final Price")
axs[1].legend()
axs[1].grid(True, alpha=0.2)

fig.suptitle("Final Price Distribution: Drift vs No Drift")

fig.text(
    0.5, 0.01,
    f"No Drift Mean: {np.mean(final_prices):.2f}   |   With Drift Mean: {np.mean(final_drift):.2f}",
    ha="center",
    fontsize=10
)

plt.tight_layout()

plt.show()
