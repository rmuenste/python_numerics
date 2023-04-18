import numpy as np
import argparse 

parser = argparse.ArgumentParser()
#parser.add_argument()

# Function to be integrated
def f(x):
    return np.sin(x)

# Gauss-Legendre quadrature points and weights for num_quad points
def gauss_legendre_points(num_quad):
    i = np.arange(0, num_quad)
    x = -np.cos((2 * i + 1) * np.pi / (2 * num_quad))
    return x

def integrate_sine_using_gauss_legendre(num_quad):
    # Interval [a, b]
    a = 0
    b = np.pi / 2

    # Get the quadrature points
    x = gauss_legendre_points(num_quad)

    # Perform change of variables to map interval [-1, 1] to [a, b]
    x_transformed = (b - a) / 2 * x + (a + b) / 2

    # Get the corresponding weights
    w = np.array([2 / num_quad] * num_quad)

    # Evaluate the function at the quadrature points and compute the weighted sum
    result = np.dot(f(x_transformed), w) * (b - a) / 2

    return result

# Number of quadrature points
num_quad = 6

# Compute the integral using Gauss-Legendre quadrature with num_quad points
result = integrate_sine_using_gauss_legendre(num_quad)

print("Approximation of the integral using", num_quad, "quadrature points: ", result)
