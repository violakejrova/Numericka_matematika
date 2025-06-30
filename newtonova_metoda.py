import math

def u(x):
    return - (x - 2) * math.exp(x) + (2 - math.e) * x - 2
    
def du(x):
    du = - (x - 1) * math.exp(x) + (2 - math.e)
    return du
    
def duu(x):
    duu = - x * math.exp(x)
    return duu

# Newton
x0 = 1/2
for i in range (666):   
    x1 = x0 - (du(x0) / duu(x0))
    x0 = x1
print(x1)
print(u(x1))
print(f"u v maximu: {u(x1)}")

