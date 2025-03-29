import numpy as np

N = int(input("počet intervalů:"))
h = 1/(N+1)
xi = np.linspace(h, 1-h, N)

# Tridiagonální matice
A = (np.eye(N, k=0)*-(2)+   #diagonála
    np.eye (N, k = -1)+     #pod diagonálou
    np.eye(N, k = 1))       #nad diagonálou

D = np.identity(N)*(-2)
L = -np.tril(A, -1)
U = -np.triu(A, 1)
invD = np.linalg.inv(D)

# Pravá strana
hodnoty = xi * np.exp(xi)
b = -h**2 * hodnoty

# Jakobi
x = np.zeros(N)
for i in range(N):
    y = np.dot(invD, np.dot(-(L+U), x) + b)
    x = y.copy()

print(f"Maximum je {np.max(x)}")

# Analytické řešení
def anRes(x):
    return (x - 1) * np.exp(x) + 1

print(f"Maximální chyba: {np.max(np.abs(x - anRes(xi)))}")

