import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


count = 1000

changes_a = np.random.normal(0,0.02,count)
prices_a = 100 * np.cumprod(changes_a + 1)

changes_b = np.random.normal(0,0.05, count)
prices_b = 100* np.cumprod(changes_b +1)

plt.plot(prices_a, label='Stable Stock A')
plt.plot(prices_b, label='Volatile Stock B')

final_a = prices_a[-1]
final_b = prices_b[-1]

avg_a = np.mean(prices_a)
avg_b = np.mean(prices_b)

print("-" * 30)
print(f"STOCK A (Stable):")
print(f"  Final Price:   ${final_a:.2f}")
print(f"  Average Price: ${avg_a:.2f}")
print("-" * 30)
print(f"STOCK B (Volatile):")
print(f"  Final Price:   ${final_b:.2f}")
print(f"  Average Price: ${avg_b:.2f}")
print("-" * 30)

plt.axhline(y=avg_a, color='blue', linestyle='--', alpha=0.3, label='Avg A')
plt.axhline(y=avg_b, color='orange', linestyle='--', alpha=0.3, label='Avg B')

plt.title("Monte Carlo Simulation: Asset Price Volatility Comparison")
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.grid(True, alpha=0.3)

#plt.show()
now = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"stock_analysis_{now}.png"
plt.savefig(filename, dpi=300)
print(f"Graph permanently saved as: {filename}")
