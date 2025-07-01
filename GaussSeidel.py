#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

N = 20
tol = 1e-6
max_iter = 200

A = (2 * np.eye(N) - np.eye(N, k=-1) - np.eye(N, k=1))
b = np.ones(N)

x = np.zeros(N)  # počáteční odhad

for k in range(max_iter):
    x_old = x.copy()
    for i in range(N):
        s1 = np.dot(A[i, :i], x[:i])       # již spočítané nové hodnoty
        s2 = np.dot(A[i, i+1:], x_old[i+1:])  # staré hodnoty
        x[i] = (b[i] - s1 - s2) / A[i, i]
    if np.linalg.norm(x - x_old, ord=np.inf) < tol:
        break

print("x =", x)

# graf
i = np.arange(len(x))
plt.figure(figsize=(10, 7))
plt.plot(i, x, marker="o")
plt.xlabel("Index")
plt.ylabel("Hodnota")
plt.title("Řešení soustavy Gauss-Seidelovou metodou")
plt.show()


# In[ ]:




