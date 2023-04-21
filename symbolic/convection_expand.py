from sympy import Matrix, symbols

# Define the matrix U
U11, U12, U13, U21, U22, U23, U31, U32, U33 = symbols('du1dx du2dx du3dx du1dy du2dy du3dy du1dz du2dz du3dz')
U = Matrix([[U11, U12, U13], [U21, U22, U23], [U31, U32, U33]])
u1, u2, u3 = symbols('u1 u2 u3')
u = Matrix([[u1], [u2], [u3]])
# Compute the matrix multiplication of U with itself
result = u.transpose() * U 

# Print the result
print(result)

# Compute the double dot product of U with itself
#A_dot_U = 0.25 * (A * U).trace()

# Print the result
#print(A_dot_U)
