#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def solve_diskretni(N):

    h = 1.0 / (N + 1)
    xi = np.linspace(h, 1 - h, N)

    d = h**2 * xi * np.exp(xi)

    pod_diag = -1.0 * np.ones(N - 1)  # pod hlavní diagonálou
    hlav_diag = 2.0 * np.ones(N)      # hlavní diagonála
    nad_diag = -1.0 * np.ones(N - 1)  # nad hlavní diagonálou

    # Thomasův algoritmus - forward eliminace
    for i in range(1, N):
        w = pod_diag[i - 1] / hlav_diag[i - 1]
        hlav_diag[i] -= w * nad_diag[i - 1]
        d[i] -= w * d[i - 1]

    # Thomasův algoritmus - zpětná substituce
    u_vnitrni = np.empty(N)
    u_vnitrni[-1] = d[-1] / hlav_diag[-1]
    for i in range(N - 2, -1, -1):
        u_vnitrni[i] = (d[i] - nad_diag[i] * u_vnitrni[i + 1]) / hlav_diag[i]

    # Přidání okrajových hodnot u(0)= 0 =u(1)
    x_vse = np.linspace(0, 1, N + 2)
    u_vse = np.hstack(([0.0], u_vnitrni, [0.0]))

    return x_vse, u_vse


x, u = solve_diskretni(100)

index_max = np.argmax(u)
u_max = u[index_max]
x_max = x[index_max]


print(f"Numerické maximum u = {u_max}")
print(f"v bodě x = {x_max}")


# In[ ]:




