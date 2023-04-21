from sympy import Matrix, symbols

# Define the matrix U
U11, U12, U13, U21, U22, U23, U31, U32, U33 = symbols('du1dx du2dx du3dx du1dy du2dy du3dy du1dz du2dz du3dz')
#a11, a12, a13, a21, a22, a23, a31, a32, a33 = symbols('a11 a12 a13 a21 a22 a23 a31 a32 a33')
u_U11, u_U12, u_U13, u_U21, u_U22, u_U23, u_U31, u_U32, u_U33 = symbols('u1-U1 u2-U2 u3-U3 u1-U1 u2-U2 u3-U3 u1-U1 u2-U2 u3-U3')
U = Matrix([[U11, U12, U13], [U21, U22, U23], [U31, U32, U33]])
A = Matrix([[u_U11, u_U12, u_U13], [u_U21, u_U22, u_U23], [u_U31, u_U32, u_U33]])

# Compute the matrix multiplication of U with itself
A = A + A.transpose()
U = U + U.transpose()

# Print the result
print(A)
print(U)

# Compute the double dot product of U with itself
A_dot_U = 0.25 * (A * U).trace()

# Print the result
print(A_dot_U)