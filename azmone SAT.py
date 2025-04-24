from scipy.stats import norm

mu = 1019
sigma = 209
min_score = 820

z = (min_score - mu) / sigma

percent_fail = norm.cdf(z) * 100

print(f"davtalabane vagede sharayet nashode: {percent_fail:.2f}%")