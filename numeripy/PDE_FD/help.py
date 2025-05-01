dict2 = {
"fd_key" : ["finitedifference", "heatequation", "heat_equation", "PDE",
              "fd", "CrankNicholson"]
}

def help(kw = " "):

  if((kw.lower()).replace(" ", "") in dict2["fd_key"]):
    print("Method located in numeripy.Heat_FD \\n")
    Notes = '''
    Finite difference method for the (PDE) 1D-heat-equation
    f(x, t) = u_xx + f(x, t)
      function name: 

      Inputs: a: Left end point
              b: Right end point
              N: Number of segments (spatially)
              T: Maximum time
              dt: Time-step
              u0_func: Initial condition
              f_src: Source term in the def of heat equation 
              method: Time stepping method. 
                      One of 'rk2' - Runge Kutta 2nd order explicit, 
                             'rk4' - Runge Kutta 4th order explicit, 
                             'euler' - Euler's method explicit or 
                             'implicit_euler' - implicit euler time-evolution
                             'cn' - Crank-Nicholson's implicit time-evolution 
      Outputs: x: The spatial grid points (1D array)
              ts: The time grid points (1D array)
              U: The solution array (2D array) of shape (N+2, nt+1)
                    where nt = T/dt = number of time steps
    '''
    print(Notes)
  return 0
