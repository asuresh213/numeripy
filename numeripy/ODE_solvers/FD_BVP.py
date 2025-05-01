import numpy as np

# Implicit BVP solver for a general linear second-order ODE
def ODE_BVP_Linear(p,q,r,t, h,alpha,beta,N):
    t_interior = t[1:-1]

    # Precompute p, q, r at interior points
    P = p(t_interior)
    Q = q(t_interior)
    R = r(t_interior)

    # Initialize A matrix and RHS vector
    A = np.zeros((N, N))
    b_vec = np.zeros(N)

    for i in range(N):
        if i > 0:
            A[i, i - 1] = 1/h**2 - P[i]/(2*h)
        A[i, i] = -2/h**2 + Q[i]
        if i < N - 1:
            A[i, i + 1] = 1/h**2 + P[i]/(2*h)
        b_vec[i] = R[i]

    # Include boundary values
    b_vec[0] -= (1/h**2 - P[0]/(2*h)) * alpha
    b_vec[-1] -= (1/h**2 + P[-1]/(2*h)) * beta

    # Solve linear system
    y_interior = np.linalg.solve(A, b_vec)
    y = np.concatenate(([alpha], y_interior, [beta]))
    return t, y