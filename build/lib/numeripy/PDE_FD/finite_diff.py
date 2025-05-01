import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


def step_rk2(u, dt, rhs_func, t_n):
    """
    Performs a single RK2 step.
    
    Parameters
    ----------
    u : ndarray
        Current solution vector
    dt : float
        Time step size
    rhs_func : callable
        Function to compute the right-hand side of the ODE system
    t_n : float
        Current time
    
    Returns
    -------
    u_next : ndarray
        Updated solution vector after one RK2 step
    """
    k1 = rhs_func(u, t_n)
    k2 = rhs_func(u + dt * k1, t_n + dt)
    
    return u + (dt / 2) * (k1 + k2)



def step_rk4(u, dt, rhs_func, t_n):
    """
    Performs a single RK4 step.
    
    Parameters
    ----------
    u : ndarray
        Current solution vector
    dt : float
        Time step size
    rhs_func : callable
        Function to compute the right-hand side of the ODE system
    t_n : float
        Current time
    
    Returns
    -------
    u_next : ndarray
        Updated solution vector after one RK4 step
    """
    k1 = rhs_func(u, t_n)
    k2 = rhs_func(u + 0.5 * dt * k1, t_n + 0.5 * dt)
    k3 = rhs_func(u + 0.5 * dt * k2, t_n + 0.5 * dt)
    k4 = rhs_func(u + dt * k3, t_n + dt)
    
    return u + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)


def step_euler(u, dt, rhs_func, t_n):
    """
    Performs a single Euler step.
    
    Parameters
    ----------
    u : ndarray
        Current solution vector
    dt : float
        Time step size
    rhs_func : callable
        Function to compute the right-hand side of the ODE system
    t_n : float
        Current time
    
    Returns
    -------
    u_next : ndarray
        Updated solution vector after one Euler step
    """
    k1 = rhs_func(u, t_n)
    
    return u + dt * k1



# Implicit finite difference method with implicit time stepping via Crank-Nicholson 

def fdm_heat_cn(a, b, N, T, dt, u0_func, f_src):
    """
    Solves the 1D heat equation using finite differences and Crank–Nicolson.
    u_t = u_xx + f(x,t), with u(a)=u(b)=0 and u(x,0)=u0(x)
    
    Parameters
    ----------
    a, b : floats
        Domain endpoints
    N : int
        Number of interior points (total points = N+2)
    T : float
        Final time
    dt : float
        Time step size
    u0_func : callable
        Initial condition function
    f_src : callable
        Source term function f(x,t)

    Returns
    -------
    x : ndarray
        Spatial grid points
    ts : ndarray
        Time grid points
    U : ndarray
        Solution array, shape (N+2, nt+1)
    """
    # 1) Spatial grid
    x = np.linspace(a, b, N+2)
    h = x[1] - x[0]
    
    # 2) Time grid
    nt = int(np.ceil(T / dt))
    ts = np.linspace(0, nt*dt, nt+1)
    
    # 3) Initialize solution array
    U = np.zeros((N+2, nt+1))
    U[:, 0] = u0_func(x)

    # 4) Crank–Nicolson coefficients
    r = dt / (2 * h**2)

    # 5) Tridiagonal system setup: A*u^{n+1} = B*u^n + RHS
    # Matrix A (implicit part)
    A_upper = -r * np.ones(N-1)
    A_diag  = (1 + 2*r) * np.ones(N)
    A_lower = -r * np.ones(N-1)
    ab_A = np.zeros((3, N))
    ab_A[0,1:] = A_upper
    ab_A[1,:]  = A_diag
    ab_A[2,:-1]= A_lower

    # Matrix B (explicit part)
    B_upper = r * np.ones(N-1)
    B_diag  = (1 - 2*r) * np.ones(N)
    B_lower = r * np.ones(N-1)

    # 6) Time stepping loop
    for n in range(nt):
        t_n   = ts[n]
        t_np1 = ts[n+1]

        # Interior values only (u[1:-1])
        u_n = U[1:-1, n]

        # Source term (average at time t_n and t_np1)
        x_inner = x[1:-1]
        F_n   = f_src(x_inner, t_n)
        F_np1 = f_src(x_inner, t_np1)
        F_avg = 0.5 * dt * (F_n + F_np1)

        # Right-hand side: B * u^n + F_avg
        rhs = B_diag * u_n
        rhs[:-1] += B_upper * u_n[1:]   # upper diagonal
        rhs[1:]  += B_lower * u_n[:-1]  # lower diagonal
        rhs += F_avg

        # Fix boundaries
        rhs[0]  += r * U[0,   n] + r * U[0,   n+1]
        rhs[-1] += r * U[-1,  n] + r * U[-1,  n+1]

        # Solve tridiagonal system
        u_next = solve_banded((1,1), ab_A, rhs)
        U[1:-1, n+1] = u_next

    return x, ts, U


# Implicit finite difference method with implicit time stepping via implicit Euler

def fdm_heat_implicit_euler(a, b, N, T, dt, u0_func, f_src):
    """
    Solves u_t = u_xx + f(x,t) using finite differences and Implicit Euler.
    Dirichlet BCs: u(a) = u(b) = 0.
    """
    # 1) Spatial grid
    x = np.linspace(a, b, N+2)
    h = x[1] - x[0]
    nt = int(np.ceil(T / dt))
    ts = np.linspace(0, nt*dt, nt+1)

    # 2) Initial condition
    U = np.zeros((N+2, nt+1))
    U[:, 0] = u0_func(x)

    # 3) Discrete Laplacian A using finite differences (interior points only)
    main_diag = -2.0 * np.ones(N)
    off_diag  = 1.0 * np.ones(N - 1)
    A = diags([off_diag, main_diag, off_diag], offsets=[-1, 0, 1], format="csr") / h**2

    I = diags([1.0] * N, 0, format="csr")
    LHS = I - dt * A  # (I - dt * A)

    # 4) Time stepping
    for n in range(nt):
        t_np1 = ts[n+1]

        # Right-hand side: u^n + dt*f(t^{n+1})
        u_n = U[1:-1, n]  # interior
        f_vec = f_src(x[1:-1], t_np1)
        rhs = u_n + dt * f_vec

        # Solve linear system
        u_next = spsolve(LHS, rhs)

        # Store solution
        U[1:-1, n+1] = u_next  # Dirichlet BCs: 0 at both ends

    return x, ts, U

# Implicit finite difference method with explicit time stepping via RK2, RK4, or Euler

def fdm_heat(a, b, N, T, dt, u0_func, f_src, method = 'rk4'):

    """
    Solves u_t = u_xx + f(x,t) using finite differences and RK (or Euler) time stepping.
    Dirichlet BCs: u(a) = u(b) = 0.
    """
    if(method == 'cn'):
        return fdm_heat_cn(a, b, N, T, dt, u0_func, f_src)
    if(method == 'implicit_euler'):
        return fdm_heat_implicit_euler(a, b, N, T, dt, u0_func, f_src)

    # 1) Spatial grid
    x = np.linspace(a, b, N+2)
    h = x[1] - x[0]
    nt = int(np.ceil(T / dt))
    ts = np.linspace(0, nt*dt, nt+1)

    # 2) Initial condition
    U = np.zeros((N+2, nt+1))
    U[:, 0] = u0_func(x)

    # 3) Discrete Laplacian (internal points only)
    A = (np.diag(-2*np.ones(N)) +
         np.diag(1*np.ones(N-1), k=1) +
         np.diag(1*np.ones(N-1), k=-1)) / h**2

    # 4) Time stepping
    for n in range(nt):
        t_n = ts[n]
        u_n = U[1:-1, n]  # interior values

        # RHS function: du/dt = A*u + f
        def rhs(u, t):
            f_vec = f_src(x[1:-1], t)
            return A @ u + f_vec

        if method == 'rk2':
            u_next = step_rk2(u_n, dt, rhs, t_n)
        elif method == 'rk4':
            u_next = step_rk4(u_n, dt, rhs, t_n)
        elif method == 'euler':
            u_next = step_euler(u_n, dt, rhs, t_n)
        # Apply boundary conditions (Dirichlet: u=0)
        U[1:-1, n+1] = u_next

    return x, ts, U