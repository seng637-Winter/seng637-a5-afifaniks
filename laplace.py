import math

import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("failure-data-a5/failure-dataset-a5.csv")["FC"].values

def laplace_factor(k, n):
  if len(n) != k:
    raise ValueError("Length of list n must be equal to the number of sub-intervals k.")

  numerator_term1 = sum((i - 1) * failure for i, failure in enumerate(n, 1))
  numerator_term2 = (k - 1) / 2 * sum(n)
  numerator = numerator_term1 - numerator_term2

  denominator_term = sum(n) * ((k**2 - 1) / 12)
  denominator = math.sqrt(denominator_term)

  return numerator / denominator

try:
  u_k = [laplace_factor(k, data[:k]) for k in range(2, 32)]
  print(f"Laplace factor u(k): {u_k}")
  intervals = range(2, len(data) + 1)

  plt.plot(intervals, u_k, color='blue')
  plt.scatter(intervals, u_k, marker='*', color='red')
  plt.xlabel('Interval')
  plt.ylabel('Laplace Factor (u(k))')
  plt.title('Laplace Test Analysis')
  plt.axhline(y=0, color='black', linestyle='dotted')
  plt.xticks(intervals)
  plt.grid(True)

  plt.show()

except ValueError as e:
  print(e)
