import numpy as np
import matplotlib.pyplot as plt

N =  20 # Počet intervalů
tol = 1e-6 
max_iter = 200

# tridiagonální matice
A = (2 * np.eye(N) - np.eye(N, k=-1) - np.eye(N, k=1))
b = np.ones(N)

D = np.diag(np.diag(A))  # diagonální
L = np.tril(A, -1)      # dolní trojúhelníková 
U = np.triu(A, 1)       # horní trojúhelníková 
invD = np.linalg.inv(D)

#Jacobi
x = np.zeros(N)  # Počáteční odhad
for i in range(max_iter):  
    y = invD @ (b - (L + U) @ x)    
    if np.linalg.norm(y - x, ord=np.inf) < tol:  # kontrola konvergence
        break     
    x = y 
print("x=",x)

#graf
i = np.arange(len(x))
plt.figure(figsize=(10, 7))
plt.plot(i, x, marker = "o")
plt.xlabel("Iterace")
plt.ylabel("Hodnota")
plt.show()




