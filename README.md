# Numeripy

Numeripy is a numerical methods package that includes various numerical methods often encountered in senior year Numerical Analysis + Optimization courses. It is written with the motivation to provide flexibility to the user in selecting a certain scheme and having a good precision control. It also helps one compare and contrast the performances of different schemes for a certain problem. Another potential avenue of use would be for pedagogical purposes - with a pre-compiled library, real time analysis of rather involved methods in class is made possible

# Ver 0.1.6 comes with
### ODE solvers
    numeripy.ODE_solvers
 ##### Methods included
 IVP solvers:
  - Euler
  - Modified Euler
  - Taylor (orders 2,3, 4 and 5)
  - Runge-Kutta
    - Orders 3, 4 and 6
    - Adaptable to systems of ODE (and therefore, higher order ODE)
  - Runge-Kutta Fehlberg (R-K with variable step size)
  - Adam-Bashforth m-step explicit method (m = 2, 3, 4 or 5)
  - (multi-step) Predictor Corrector schemes
    - Predictor: Adam-Bashforth; Corrector: Adam-Moulton
    - Predictor steps supported: m = 2, 3, 4 or 5
    - Corrector steps supported: m = 2, 3 or 4
    - Accomodates variable step size with
         - Predictor: 4 step Adam-Bashforth
         - Corrector: 3 step Adam-Moulton

BVP solver:
  - Implicit **finite difference** solver for second order linear ODE
    of the form 
    $$\frac{d^2 y}{dt^2} + p(t)\frac{dy}{dt} + q(t) = r(t)$$
        

### Matrix methods
    numeripy.matrix_methods
 ##### Methods included
  - Matrix multiplication
  - Determinant
  - Gaussian Elimination by backward substitution (GEBS)
     - Normal GEBS
     - GEBS with partial pivoting
     - GEBS with scaled pivoting
  - Factorization
    - LU factorization
    - LDL^T  factorization
    - Cholesky factorization
 - Iterative matrix methods
    - Jacobi
    - Gauss-Seidel
    - Successive order relaxation (SOR)

numeripy also comes with some post-processing tools for numerical ODE solutions.
  - `numeripy.Latexit()` creates latex formatted tables (when passed with array inputs)
  - `numeripy.plotit()` plots all the solutions (when passed with ODE solutions as inputs)    


### 1-dimensional PDE solvers
    numeripy.PDE_FD
  #### Methods included
  1 dimensional PDE (finite difference) solvers for the heat-equation 
  $$u_t = u_{xx} + f(x,t)$$
  - Time-explicit **finite difference** solvers with explicit time evolution support via 
    - Euler's method
    - Runge-Kutta 2-step
    - Runge-Kutta 4-step

  - Time-implicit **finite difference** solvers with implicit time evolution support via
    - Implicit Euler
    - Crank Nicholson

## Getting numeripy
(Assuming, the user already has pip installed - otherwise, follow [this][dsf] first to get pip)

Getting numeripy is as simple as opening command prompt and entering
```
$ pip install numeripy
```

## Working with numeripy
#### Dependencies
`numeripy` requires
 - ``numpy``
 - ``matplotlib``
 - ``tabulate``

 to be able to function properly

#### numeripy.help()
``numeripy.help()`` takes a keyword argument about any of the above methods and prints the subdirectory that needs to be imported along with information pertaining to function input and output. `.help()` can also be accessed from any of the subdirectory (that is to say, `numeripy.help()` provides information about all functionality inside `numeripy`, whereas, `numeripy.matrix_methods.help()` provides information only about the matrix methods.)

## What to expect in numeripy 0.2
#### Optimization schemes
`numeripy` plans to include a subdirectory containing standard optimization algorithms such as Gradient descent, Gradient descent for higher order multidimensional problems, Secant method, Line search, Newton's method and a few others.

#### Example problem set
`numeripy` also plans to include a folder with many example problems that the user is invited to try out. The Examples folder will be located along with the user's `numeripy` installation. (This update will be released shortly).


[dsf]: <https://pip.pypa.io/en/stable/installing/>
