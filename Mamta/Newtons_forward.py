import numpy as np
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
y = np.array([1, 1, 2214, 1.4918, 1.8221, 2.2255, 2.7183])
n = len(x)
A = np.zeros([n, n])
A[:, 0] = y
for j in range(1, n):
    for i in range(n-j):
        A[i, j] = A[i+j, j-1]-A[i, j-1]
xp = 0.1
h = x[2]-x[1]
p = (xp-x[0])/h
q = 1
s = y[0]
for i in range(n-1):
    q= [q*(p-i)]/[(i+1)]*A[0,i+1]
    s = s+q*A[0,i+1]
print(s)