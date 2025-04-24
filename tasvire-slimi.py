import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20*np.pi, 3000)

x = t * np.cos(t) * 0.2
y = t * np.sin(t) * 0.2

plt.figure(figsize=(10, 10))

plt.plot(x, y, color='darkblue', linewidth=1.5)

plt.title("tasvire slimi", fontsize=18, pad=20)
plt.axis('equal')
plt.axis('off')

plt.savefig('tasvire slimi.png', dpi=300, bbox_inches='tight')
plt.show()