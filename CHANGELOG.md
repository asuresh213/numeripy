# Changelog

## v 0.1.6

### Feature
 - Added an implicit finite difference BVP solver for second order linear ODE to numeripy.ODE_solvers
 - Added implicit finite difference 1-D PDE solvers with explicit and implicit time-evolution support
    - Explicit time integrators: Euler, RK2, RK4
    - Implicit time integrators: Implicit Euler, Crank-Nicholson
 - Updated the relevant help() functions to document use cases for the new methods.