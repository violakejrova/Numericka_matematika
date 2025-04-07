#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np

N = 4
A = (2 * np.eye(N) - np.eye(N, k=-1) - np.eye(N, k=1))
Q = np.zeros_like(A)     #nuloví matice
R = np.diag(np.ones(N))  #diagonální matice - jednotková

def GS(A):
    Q[:, 0] = A[:, 0]
    for k in range(1, N): 
        v = A[:, k]
        for l in range(0, k):
            q_l = Q[:, l]
            R[l, k] = (q_l.T @ A[:, k]) / (q_l.T @ q_l)
            v = v - R[l, k] * q_l
        R[k, k] = np.linalg.norm(v)
        Q[:, k] = v


    return Q,R

Q, R = GS(A)

for i in range(666):
    A = R @ Q 
    
print("Vlastní čísla):", np.diag(A))

