import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

α = 0.1
β = 0.02
γ = 0.3
δ = 0.01

def model(y, t):
    H, W = y
    dHdt = α * H - β * H * W
    dWdt = δ * H * W - γ * W
    return [dHdt, dWdt]

H0 = 40
W0 = 9
y0 = [H0, W0]

t = np.linspace(0, 200, 2000)

solution = odeint(model, y0, t)
H, W = solution.T

H_eq = γ / δ
W_eq = α / β
print(f"noghte taadol: aho ha = {H_eq:.0f}، gorg ha = {W_eq:.0f}")

plt.figure(figsize=(12, 6))
plt.plot(t, H, 'g-', label='tedade aho ha')
plt.plot(t, W, 'r-', label='tedade gorg ha')
plt.axhline(H_eq, color='g', linestyle='--', alpha=0.5, label='taadole aho ha')
plt.axhline(W_eq, color='r', linestyle='--', alpha=0.5, label='taadole gorg ha')
plt.title('rabete shekar va shekarchi')
plt.xlabel('roz')
plt.ylabel('tedad')
plt.legend()
plt.grid()
plt.show()