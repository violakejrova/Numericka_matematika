import numpy as np

A = np.array([[-4,3,0,0], [4,20,13,1], [0,0,2,1], [3,-6,7,3]])
B = A.T@A

# Sloupcová norma (p = 1)
def sloup_norm(A): 
# Součet absolutních hodnot prvků ve sloupcích
    x = 0
    for s in range(0, len(A[0])):
        soucet = 0
        for r in range(0, len(A)):
            soucet += abs(A[r][s])
        if soucet > x:
            x = soucet    
    return x

# Řádková norma (p = ∞)
def rad_norm(A):
# Součet absolutních hodnot prvků v řádcích 
    x = 0
    for r in range(0, len(A[0])):
        soucet = 0
        for s in range(0, len(A)):
            soucet += abs(A[r][s])
        if soucet > x:
            x = soucet    
    return x   

def maxlambda(A):
    u = np.array([1,0,1/2,0])
    tol = 1e-6
    maxint = 100
    l_old = 0
    
    for i in range(maxint):
        u = A@u / np.linalg.norm(A@u)
        l = (u.T @ A @ u) / (u.T @ u)

        if np.abs(l_old - l) < tol:
            break
        else:
            l_old = l
    return l        

def spekt_norm(A):
    l = maxlambda(B)
    snorm = np.sqrt(l)
    return snorm
print(f"sloupcová norma je {sloup_norm(A)}, řádková norma je {rad_norm(A)} a spektrální norma je {spekt_norm(A)}") 

#čísla podmíněnosti
A1 = np.linalg.inv(A)
KR = rad_norm(A) * rad_norm(A1)
KS = sloup_norm(A) * sloup_norm(A1)
KF = spekt_norm(A) * spekt_norm(A1)
