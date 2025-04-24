import numpy as np
import matplotlib.pyplot as plt

def simulate_bacteria_growth(initial_count, target=1e6, days=50, death_prob=0.25):
    counts = [initial_count]
    current_count = initial_count
    
    for day in range(1, days+1):
        current_count *= 2
        
        deaths = np.random.binomial(current_count, death_prob)
        current_count -= deaths
        
        counts.append(current_count)
        
        if current_count >= target:
            print(f"tedade bakteri ha dar roz {day} be {current_count:,.0f} resid!")
            break
    else:
        print(f"dar {days} roz be yek milion bakteri naresidim: {current_count:,.0f}")
    
    return counts

initial_bacteria = 1
target = 1_000_000
simulation_days = 100

results = simulate_bacteria_growth(initial_bacteria, target, simulation_days)

plt.figure(figsize=(12, 6))
plt.plot(results, 'g-', linewidth=2, label='tedade bakteri ha')
plt.axhline(y=target, color='r', linestyle='--', label='hadaf (1,000,000)')
plt.title('modele roshde bakteri ha ba taghsime rozaneh va ehtemale marge 25%', fontsize=14)
plt.xlabel('roz', fontsize=12)
plt.ylabel('tedade bakteri ha', fontsize=12)
plt.yscale('log')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()