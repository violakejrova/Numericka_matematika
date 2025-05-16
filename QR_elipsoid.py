#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np

N = 3
A = 1/5*np.array([[2,2,0],[2,3,0],[0,0,4]])

def GS(A):
    N = A.shape[0]
    Q = np.zeros_like(A)
    R = np.zeros((N, N))
    for k in range(N):
        v = A[:, k].copy()
        for j in range(k):
            R[j, k] = Q[:, j] @ A[:, k]
            v -= R[j, k] * Q[:, j]
        R[k, k] = np.linalg.norm(v)
        Q[:, k] = v / R[k, k]
    return Q, R

A_iter = A.copy()
Q_total = np.eye(N)

for i in range(100):
    Q, R = GS(A_iter)
    A_iter = R @ Q
    Q_total = Q_total @ Q

print("Vlastní čísla:", np.diag(A_iter))
print("Vlastní vektory (sloupce):")
print(Q_total)


# In[ ]:




