
import numpy as np

def jacobi(a, b, x_init=None, tol=1e-2, max_iterations=100):
    n = len(b)
    x = np.zeros_like(b) if x_init is None else x_init
    x_new = np.zeros_like(x)
    
    for k in range(max_iterations):
        for i in range(n):
            s1 = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s1) / a[i][i]
        
        if np.allclose(x, x_new, atol=tol):
            break
        
        x = np.copy(x_new)
    
    return x

a = np.array([[5, 3, -2], 
              [2, 1, -1], 
              [3, -2, -3]], float)

b = np.array([-1, 0, 2], float)

solution = jacobi(a, b)
print("–ешение методом якоби:", solution)
