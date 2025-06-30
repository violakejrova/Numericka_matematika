#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt

# Eulerova metoda
def euler_metoda(N):
    h = 10 / N
    x = np.linspace(0, 10, N+1)
    y = np.zeros(N+1)
    y[0] = 1

    for i in range(N):
        y[i+1] = y[i] + h * np.sin(y[i] + x[i])
    return x, y

N_list = [10, 100, 1000]

for N in N_list:
    x_euler, y_euler = euler_metoda(N)

    print(f"\n Pro N = {N}")
    print(f"y(10) ≈ {y_euler[-1]}")

    plt.plot(x_euler, y_euler, label=f"Euler N={N}")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




