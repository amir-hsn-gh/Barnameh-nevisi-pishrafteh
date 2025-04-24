import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 0, 1
x = np.linspace(-4, 4, 1000)

cdf = norm.cdf(x, mu, sigma)

plt.figure(figsize=(8, 4))
plt.plot(x, cdf, 
         label=f'CDF normal (μ={mu}, σ={sigma})', 
         color='red',
         linewidth=2)

plt.title('tabe tozie tajamoe ehtemali gosi', fontsize=14)
plt.xlabel('meghdar x', fontsize=12)
plt.ylabel('ehtemale tajamoe Φ(x)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='lower right')

plt.show()