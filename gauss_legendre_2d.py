import numpy as np

# Function to be integrated over the rectangular domain
def f(x, y):
    return x**2 + y**2

# Gauss-Legendre quadrature points and weights for num_quad points
def gauss_legendre_points(num_quad):
    i = np.arange(0, num_quad)
    x = -np.cos((2 * i + 1) * np.pi / (2 * num_quad))
    return x

def integrate_over_rectangular_domain(num_quad_x, num_quad_y):
    # Domain boundaries
    x_min, x_max = -1, 1
    y_min, y_max = -1, 1

    # Get the 1D quadrature points and weights
    x = gauss_legendre_points(num_quad_x)
    y = gauss_legendre_points(num_quad_y)

    # Compute the tensor product of the 1D quadrature points
    X, Y = np.meshgrid(x, y)
    X = X.flatten()
    Y = Y.flatten()

    # Compute the product of the 1D quadrature weights
    wx = np.array([2 / num_quad_x] * num_quad_x)
    wy = np.array([2 / num_quad_y] * num_quad_y)
    W = np.outer(wx, wy)
    W = W.flatten()

    # Evaluate the function at the quadrature points and compute the weighted sum
    result = np.dot(f(X, Y), W) * (x_max - x_min) * (y_max - y_min) / 4

    return result

# Number of quadrature points in x-axis and y-axis
num_quad_x = 4
num_quad_y = 3

# Compute the integral over the rectangular domain using Gaussian quadrature
result = integrate_over_rectangular_domain(num_quad_x, num_quad_y)

print("Approximation of the integral: ", result)
