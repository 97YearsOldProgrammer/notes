import numpy as np
import matplotlib.pyplot as plt

x_points = np.array([1, 1.25, 1.6])
y_points = np.sin(np.pi * x_points)

def lagrange_basis(x, x_data,k):
    xk = x_data[k]
    Lk = 1.0
    for i, xi in enumerate(x_data):
        if i != k:
            Lk *= (x-xi)/(xk - xi)
    return Lk

x_eval = np.linspace(0.8, 1.8, 300)   
y_eval = [lagrange_basis(xx ,x_points , 2) for xx in x_eval]
L_points = [lagrange_basis(xx , x_points, 2) for xx in x_points]
plt.figure( figsize= (8,5) )
plt.plot(x_points, L_points, 'ro' , label = 'L_n0 at Interpolation Points')
plt.plot(x_eval, y_eval, 'b-', label = 'L_n0')
plt.title('Lagrange basis function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

def lagrange_interpolation(x, x_data, y_data):
    result = 0.0
    for i in range(len(x_data)):
        result += y_data[i] * lagrange_basis(x, x_data, i)
    return result

y_eval = [lagrange_interpolation(xx, x_points, y_points) for xx in x_eval]
y_true = np.sin(np.pi * x_eval)

plt.figure(figsize = (8 , 5 ))
plt.plot(x_points, y_points, 'ro', label= 'Interpolation Points')
plt.plot(x_eval, y_eval, 'b-', label= 'Interpolated Polynomial')
plt.plot(x_eval, y_true, 'g--', label= 'True sin(x)')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()