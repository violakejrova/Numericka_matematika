import math

def u(x):
    u = (math.exp(x) - x*math.exp(x) + 2 - math.e)
    return u
def du(x):
    du = -x*math.exp(x)
    return du

# Newton
x0 = 1/2
for i in range (667):   
    x1 = x0 - (u(x0) / du(x0))
    x0 = x1
print(x1)
print(u(x1)) #ověření, že je to kořen

